"""TF-iDF.py"""

#Librerías
from pyspark.sql import SparkSession
from math import log
from operator import add

#Nombre librerías
text_file="pg100.txt"


spark = SparkSession.builder.appName('TF-IDF').getOrCreate()

lines = spark.read.text(text_file).rdd.map(lambda r: r[0])

total_documents = lines.count()

tf = lines.zipWithIndex() \
          .flatMap(lambda x: [((word.lower(), x[1]), 1) for word in x[0].split()]) \
          .reduceByKey(add) \
          .map(lambda x: (x[0][0], (x[0][1], x[1]))) # ((palabra, (id_documento, tf)))

df = tf.map(lambda x: (x[0], 1)) \
       .reduceByKey(add)

idf = df.map(lambda x: (x[0], log(total_documents / float(x[1]))))  

tf_idf = tf.join(idf).map(lambda x: ((x[0], x[1][0][0]), x[1][0][1] * x[1][1]))

results_tfidf = tf_idf.collect()

# Convertimos los resultados en strings y los escribimos en un archivo
with open("results_tfidf.txt", "w") as file:
    for result in results_tfidf:
        # Convertimos cada tupla a string
        line = str(result) + "\n"
        file.write(line)

# Detenemos la sesión de Spark
spark.stop()
