from fastapi import FastAPI
import uvicorn

app = FastAPI() #Instancia Fastapi

#Devuelve el titulo con mayor duracion
#fitra anio, plataforma, duracion y devuelve el mayor valor de la columna duration
@app.get("/dur") #Operador para un request.get()
def get_max_duration(year : int = 2018, platform : str = 'hulu', duration : str = 'Movie'):
    import pandas as pd 
    titles = pd.read_csv('../Datasets/Titles.csv') #Leo el archivo creado "Titles". La de la combinacion de DF
    duracion = titles[(titles.release_year == year) & (titles.platform == platform) & (titles.type == duration)].sort_values(by='duration').head(1)
    return duracion['title']
#Devuelve catidad de peliculas y series por plataforma elegida
@app.get("/count")
def get_count_plataform(platform : str = 'netflix'):
    import pandas as pd
    titles = pd.read_csv('../Datasets/Titles.csv')
    plataforma = titles[titles.platform == platform].groupby(['type']).agg({'type':'count'})
    Movie = plataforma.type.values[0]
    Tvshow = plataforma.type.values[1]
    return {'platform' : platform, 'Movie' : str(Movie), 'TV Show' : str(Tvshow)}
#Cantidad de titulos con genero espeifico
#Cuenta la cantidad de veces que se repite un texto seteado, en la columna listed_in separado por plataforma
@app.get("/list")
def get_listedin(listed : str = 'Comedy'):
    import pandas as pd
    titles = pd.read_csv('../Datasets/Titles.csv')
    genero = titles[titles['listed_in'].str.contains(listed)].groupby(by='platform').count().head(1)
    genero = genero[['listed_in']].reset_index()
    genero['listed_in'] = genero.listed_in.astype(str, copy=False)
    return genero
#Actor con mas titulo
#Crea un diccionario donde va guardando al actor con un conteo de frequencia
@app.get("/actor")
def get_actor(platform : str = 'netflix', year : int = 2018):
    import pandas as pd
    titles = pd.read_csv('../Datasets/Titles.csv')
    actor = titles[(titles.platform == platform) & (titles.release_year == year)]
    actor = actor.dropna(subset='cast')
    actor = actor['cast'].str.split(pat=',')
    diccionario_frecuencias = {}
    for i in actor:
        for palabra in i:
            if palabra in diccionario_frecuencias:
                diccionario_frecuencias[palabra] += 1
            else:
                diccionario_frecuencias[palabra] = 1
    actor = max(diccionario_frecuencias, key=diccionario_frecuencias.get)
    freq = diccionario_frecuencias.get(actor)
    return {'platform' : platform, 'frequency' : freq, 'actor' : actor}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)