from CargaBD import cursor
import pandas as pd

sentenciasql=   "SELECT m.name as 'Movie',\
    m.year AS 'Year',\
    d.last_name AS 'Director',\
    m.ranked AS 'Ranking'\
    FROM movies_directors AS md\
    JOIN movies AS m ON m.id = md.movie_id\
    JOIN directors AS d ON d.id = md.director_id\
    WHERE m.ranked >8\
    ORDER BY m.ranked\
    DESC;"

cursor.execute(sentenciasql)
filas=cursor.fetchall()
lista=[]
for i in filas:
    lista.append(i)
    

df=pd.DataFrame(lista, columns=["Pelicula","Año","Director","Puntaje"] )
print(df)
df2=df.loc[:10,["Pelicula","Puntaje"]] 
print(df2)

df=df.loc[20:50,["Pelicula","Año","Director","Puntaje"]] 
print(df)