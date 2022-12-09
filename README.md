En este proyecto se realiza la ingesta de dato y limpieza de una serie de Datasets.
Se crea un api con la libreria FastApi y luego se crea una imagen en docker para su implementacion

El proyecto contiene un main.py que es donde se crea la api, el ReadData.py en el cual se lee los archivos
se le hace ETL(se eliminan las columnas que no se van a usar, se aplica cambio de tipo de datos) y lo guarda en un archivo.

Se trabaja unicamente con pandas y numpy para procesar los datos, debido a la poca cantidad de registros no se creyo conveniente crear una base de datos.

En el main.py estan todas las instancias para cada request:
    Pelicula con maxima duracion en base a plataforma y anio
    Genero que mas se repite en cada plataforma
    Cantidad de serie y pelicula en la plataforma elegida
    Actor con mas apariciones en plataforma y anio elegidos