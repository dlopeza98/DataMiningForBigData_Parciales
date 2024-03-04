# Pacial 1 - Data Minning for Big Data

## Desarrollado por: 
* David Alejandro López Atehortúa

## Prerrequisitos

* Instalar Pyenv (Seguir las instrucciones de <https://github.com/pyenv/pyenv>. Nota: no hay Pyenv para Windows. Se recomienda usar WSL (Windows Subsystem for Linux). También tener en cuenta las dependencias de sistemas que hay que instalar antes de instalar cualquier versión de Python en <https://github.com/pyenv/pyenv/wiki>)
* Ejecutar `pyenv local` para verificar la versión local utilizada de Python e instalarla. Por ejemplo `pyenv install 3.11.4`.
* Una vez que se esté usando la versión local, actualizar pip (`pip install --upgrade pip`) para luego instalar Pipenv.
* Instalar Pipenv (`pip install pipenv`)
* Instalar dependencies/crear ambiente virtual (`pipenv install`)

## Cómo instalar nuevas dependencias

Por ejemplo si se quiere instalar Pandas, hacerlo mediante el comando `pipenv install pandas`.

## Contenido
.
├── `Pipfile`: Archivo que contiene los paquetes a instalar en el entorno virtual
├── `Pipfile.lock`
└── `primerParcial` : folder para los archivos del caso práctico del primer parcial.
    ├── `TF-iDF.py` : Aplicación auto-contenida que ejecuta el MapReduce para el indice **TF-iDF** en un entorno productivo.
    ├── `log_tf_idf.txt` : Logs de la ejecución de la aplicación auto-contenida.
    ├── `parcial1_practico.ipynb` : Notebook en PySpark donde se explica el proceso para calcular el **TF-iDF**
    ├── `pg100.txt` : ebook de texto que se usa como inpur para el ejercicio.
    └── `results_tfidf.txt` : Resultados de la ejecución de la aplicación auto-contenida.
