# Paciales 1 y 2 - Data Minning for Big Data

## Desarrollado por: 
* David Alejandro López Atehortúa

## Prerrequisitos
En este proyecto se utiliza PDM como herramienta moderna para la gestión de dependencias en proyectos en Python. Documentacion https://pdm-project.org/en/latest/usage/dependency/

* Instalar pdm y clang:
curl -sSL https://pdm-project.org/install-pdm.py | python3 -
sudo apt install clang

* Inicialización e instalación de python y librerías
pdm python install 3.11.5
pdm init
pdm install

## Cómo instalar nuevas dependencias

Por ejemplo si se quiere instalar Pandas, hacerlo mediante el comando `pdm add pandas`.

## Nota sobre dependencias:

Se usó el comando `pdm export -o requirements.txt` para generar un archivo requirements.txt en caso de que no desee configurar PDM.


## Contenido

├── `pdm.lock`: Archivo que contiene los paquetes a instalar en el entorno virtual

├── `pyproject.toml`: Archivo que contiene la configuración del entorno virtual

└── `primerParcial` : folder para los archivos del caso práctico del primer parcial.

    ├── `TF-iDF.py` : Aplicación auto-contenida que ejecuta el MapReduce para el indice **TF-iDF** en un entorno productivo.
    
    ├── `log_tf_idf.txt` : Logs de la ejecución de la aplicación auto-contenida.
    
    ├── `parcial1_practico.ipynb` : Notebook en PySpark donde se explica el proceso para calcular el **TF-iDF**
    
    ├── `pg100.txt` : ebook de texto que se usa como inpur para el ejercicio.
    
    └── `results_tfidf.txt` : Resultados de la ejecución de la aplicación auto-contenida.

└── `segundoParcial` : folder para los archivos del caso práctico del segundo parcial.

    ├── `parcial2_practico.ipynb` : Notebook en con python donde se aplica el algoritmo **CUFE** en datos no convexos.