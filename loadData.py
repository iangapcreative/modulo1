import csv
import pymongo
from pymongo import MongoClient

#Datos de conexion a MongoDB
client = MongoClient('localhost', 27017)
db = client['newsdb']
db.authenticate('cic', 'cic1234*')
collection=db["news"]

#lectura de archivo CSV
with open('TodasLasNoticias.csv', 'r', encoding="utf8") as csvfile:
    fileReader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONE)
#contadores de registros procesados
    item=0;
    item2=0;
#For para iterar todos los registros del CSV
    for row in fileReader:
#Se asume que un registro bien formado debe tener exactamente 5 elementos
       if len(row) == 5:
           data = {"date": row[0], "title": row[1], "url": row[2], "new": row[3], "categoria": row[4]}
           x = collection.insert_one(data)
           item2+=1
       else:
#Se considera que un registro del CSV con un numero de elementos distindo a 5 es erroneo y no se guarda en Base de Datos
           #print("len: {}, row: {}".format(len(row), row))
           item+=1
#Los registros OK_data son los registros guardados en BD
    print("OK_data:{}".format(item2))
#Los registros bad_data son los que no cumplieron con los criterios de aceptacion y por lo tanto no se guardaron en BD.
    print("bad_data:{}".format(item))
