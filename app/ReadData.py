#Este script se encarga de leer los archivos individualmente y unirlos en una sola tabla, tambien se encarga del ETL 
#y guardar la tabla en un archivo
import pandas as pd
import numpy as np
#Funcion para leer los Datasets y aplicar ETL. Devuelve un DataFrame
def ReadData(direccion, dfp, plataforma, tipo = 'csv'):
    #Depende de la extension del archivo lee de forma diferente
    if tipo == 'csv':
        df = pd.read_csv(direccion, dtype= {'cast' : np.object0}) #cambia el tipo de dato de la columna cast
    elif tipo == 'json':
        df = pd.read_json(direccion)
    df.drop(columns=['show_id','director','country','rating','description'], inplace=True) #elimina columnas que no se van a usar
    df['platform'] = plataforma
    df = pd.merge(dfp, df, how= 'outer')
    df.reset_index()
    return df
#Variables con direccion de los archivos
amazon = '../Datasets/amazon_prime_titles.csv'
disney = '../Datasets/disney_plus_titles.csv'
hulu = '../Datasets/hulu_titles.csv'
netflix = '../Datasets/netflix_titles.json'
#Junta los datos en un unico DataFrame. Devuelve DataFrame
def TitlesTable():
    #DF vacio en el que se va a ir sumando los diferentes datasets
    dfe = pd.DataFrame(columns=['type','title','cast','date_added','release_year','duration','listed_in'])
    titles = ReadData(amazon, dfe, 'amazon')
    titles = ReadData(disney, titles, 'disney')
    titles = ReadData(hulu, titles, 'hulu')
    titles = ReadData(netflix, titles, 'netflix', 'json')
    return titles

csv = TitlesTable()#Guardo el DF en una variable
csv.to_csv('../Datasets/Titles.csv', index_label=False)#guardo en un archivo CSV