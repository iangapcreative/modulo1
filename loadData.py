import csv
import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['newsdb']
db.authenticate('cic', 'cic1234*')
collection=db["news"]

with open('TodasLasNoticias.csv', 'r', encoding="utf8") as csvfile:
    fileReader = csv.reader(csvfile, delimiter='|', quoting=csv.QUOTE_NONE)
    item=0;
    item2=0;
    for row in fileReader:
       if len(row) == 5:
           data = {"date": row[0], "title": row[1], "url": row[2], "new": row[3], "categoria": row[4]}
           x = collection.insert_one(data)
           item2+=1
       else:
           print("len: {}, row: {}".format(len(row), row))
           item+=1
    print("OK_data:{}".format(item2))
    print("bad_data:{}".format(item))