#Consultasssssssssss
from CargaBD import cursor

#Consulta 1
sentenciasql1="SELECT d.last_name,\
    d.first_name,\
    COUNT(movie_id) AS 'How Many'\
    FROM movies_directors AS md\
    JOIN directors AS d ON d.id = md.director_id\
    GROUP BY d.last_name, d.first_name\
    HAVING COUNT(movie_id) >3\
    ORDER BY COUNT(movie_id) DESC;"

cursor.execute(sentenciasql1)
filas=cursor.fetchall() 
print("-------------------Consulta Nº1------------------------------")
for i in filas:
    print(i)

#Consulta 2
sentenciasql2="SELECT a.last_name,\
    a.first_name,\
    COUNT(movie_id)\
    FROM actors AS a\
    JOIN movies_actors AS ma ON ma.actor_id = a.id\
    GROUP BY a.last_name, a.first_name\
    HAVING COUNT(movie_id) >3\
    ORDER BY a.last_name, a.first_name;"

cursor.execute(sentenciasql2)
filas=cursor.fetchall()
print("-------------------Consulta Nº2------------------------------")
for i in filas: 
    print(i)

#Consulta 3
sentenciasql3="SELECT m.name as 'Movie',\
    m.year AS 'Year',\
    d.last_name AS 'Director',\
    m.ranked AS 'ranked'\
    FROM movies_directors AS md\
    JOIN movies AS m ON m.id = md.movie_id\
    JOIN directors AS d ON d.id = md.director_id\
    WHERE m.ranked >8\
    ORDER BY m.ranked\
    DESC;"

cursor.execute(sentenciasql3)
filas=cursor.fetchall() 
print("-------------------Consulta Nº3------------------------------")
for i in filas: 
    print(i)

