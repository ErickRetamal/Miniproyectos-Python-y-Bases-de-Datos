import csv 
import MySQLdb
import mysql.connector
import pandas as pd


Basedatos = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="3124",
    db="cine"
    )
#Carga de actores
with open("actors.csv") as carga_actor:
    lectorcsv=csv.reader(carga_actor,delimiter=";")
    listadoActores=[]
    salto_cabecera=next(lectorcsv)
    armadosqlsetence = []
    for i in lectorcsv:
        armadosqlsetence.append(tuple([int(i[0]),i[1],i[2]])) 


#Creando cursor para ejecutar query
cursor = Basedatos.cursor()
sqlSentence = "INSERT INTO actors (id, first_name, last_name) VALUES (%s, %s, %s)"
cursor.executemany(sqlSentence,armadosqlsetence)
# Fin Carga de actores
#Carga de directores
with open("directors.csv") as carga_actor:
    lectorcsv=csv.reader(carga_actor,delimiter=";")
    listadoActores=[]
    salto_cabecera=next(lectorcsv)
    armadosqlsetence = []
    for i in lectorcsv:
        armadosqlsetence.append(tuple([int(i[0]),i[1],i[2]])) 
#Creando cursor para ejecutar query

sqlSentence = "INSERT INTO directors (id, first_name, last_name) VALUES (%s, %s, %s)"
cursor.executemany(sqlSentence,armadosqlsetence)

# Fin Carga de directores

#Carga de peliculas
with open("movies.csv") as carga_actor:
    lectorcsv=csv.reader(carga_actor,delimiter=";")
    listadoActores=[]
    salto_cabecera=next(lectorcsv)
    armadosqlsetence = []
    for i in lectorcsv:
        if i[3] == "NULL":
            armadosqlsetence.append(([int(i[0]),i[1],i[2],0])) 
        else: 
            armadosqlsetence.append(([int(i[0]),i[1],i[2],float(i[3])])) 

sqlSentence = "INSERT INTO movies (id, name, year, ranked) VALUES (%s, %s, %s, %s)"
cursor.executemany(sqlSentence,armadosqlsetence)
# Fin Carga de peliculas

#Carga de actores en peliculas
with open("movies_actors.csv") as carga_actor:
    lectorcsv=csv.reader(carga_actor,delimiter=";",quoting=csv.QUOTE_NONE)
    listadoActores=[]
    salto_cabecera=next(lectorcsv)
    armadosqlsetence = []
    for i in lectorcsv:
        armadosqlsetence.append(tuple([int(i[0]),i[1],i[2]])) 

sqlSentence = "INSERT INTO movies_actors (actor_id, movie_id, role) VALUES (%s, %s, %s)"
cursor.executemany(sqlSentence,armadosqlsetence)
# Fin Carga de actores en peliculas


# Carga de directores en peliculas
with open("movies_directors.csv") as carga_actor:
    lectorcsv=csv.reader(carga_actor,delimiter=";")
    listadoActores=[]
    salto_cabecera=next(lectorcsv)
    armadosqlsetence = []
    for i in lectorcsv:
        armadosqlsetence.append(tuple([int(i[0]),i[1]])) 

sqlSentence = "INSERT INTO movies_directors (director_id, movie_id) VALUES (%s, %s)"
cursor.executemany(sqlSentence,armadosqlsetence)
# Fin Carga de directores en peliculas
Basedatos.commit()
