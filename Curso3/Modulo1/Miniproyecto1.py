import mysql.connector

Basedatos =mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="124",
    db="Miniproyecto1"
    )

cursor = Basedatos.cursor()
sqlSentence = "INSERT INTO aeropuertos(id, ident, type,name, elevation_ft, municipality, iata_code, score) VALUES( %s,%s,%s,%s,%s,%s,%s,%s)"
fila = [
    (39340,"SHCC","heliport","Clinica Las Condes Heliport",2461,"Santiago","",25),
    (39379,"SHMA","heliport","Clinica Santa Maria Heliport",2028,"Santiago","",25),
    (39390,"SHPT","heliport","Portillo Heliport",9000,"Santiago","",25)
]
cursor.executemany(sqlSentence, fila)

Basedatos.commit()

sqlSentence = ("Select name,type,municipality,elevation_ft from aeropuertos where elevation_ft > 5000")

cursor.execute(sqlSentence)

resultado = cursor.fetchall()
for x in resultado:
    print(x)