import pymongo
import requests
import json

client = pymongo.MongoClient("mongodb://localhost:27017/")
Feriados = client["MongoDB"]

peticion = requests.get("https://apis.digital.gob.cl/fl/feriados/2020", headers={"User-Agent": "Chrome" })
peticionJSON = json.loads(peticion.text)
Dias = Feriados["feriados2020"]
Dias.insert_many(peticionJSON)

print ("======= Todos los feriados de 2020 =======")
for x in Dias.find():
    print ("El dia de", x['nombre'],"es un feriado de tipo", x['tipo'],"y se celebra el",x['fecha'])
print ("======= Fin Todos los feriados de 2020 =======")

print("============================================================================================")

print ("======= Solo los feriados Civiles de 2020 =======")
for x in Dias.find():
    if x['tipo'] == "Civil":
        print ("El dia de", x['nombre'],"es un feriado de tipo", x['tipo'],"y se celebra el",x['fecha'])
print ("======= Fin Solo los feriados Civiles de 2020 =======")

print("============================================================================================")

print ("======= Solo los Feriados Irrenunciables de 2020 =======")
for x in Dias.find():
    if x['irrenunciable'] == "1":
        print ("El dia de", x['nombre'],"es un feriado de tipo", x['tipo'],"y se celebra el",x['fecha'])
print ("======= Fin Solo los Feriados Irrenunciables de 2020 =======")

print("============================================================================================")

print ("======= Solo los Feriados que incluyen Santo o Santos =======")
for x in Dias.find({'nombre': {"$regex": "Santo"}}):
    print("El dia de", x['nombre'],"es un feriado de tipo", x['tipo'],"y se celebra el",x['fecha'])
print ("======= Fin Solo los Feriados que incluyen Santo o Santos =======") 

print("============================================================================================")

print ("======= Leyes relacionadas con el Plebiscito de Abril =======")
for x in Dias.find({'nombre': {"$regex": "Plebiscito"}}):
    print("Las leyes involucradas en el día del Plebiscito Constitucional son las siguientes:")
    for y in x['leyes']:
        print(y['nombre'], "revisar en:",y['url'])    
print ("======= Fin Leyes relacionadas con el Plebiscito de Abril =======") 

