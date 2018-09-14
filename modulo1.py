from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.json_util import dumps

#Datos de conexion a MongoDB
client = MongoClient('localhost', 27017)
db = client['newsdb']
db.authenticate('cic', 'cic1234*')
collection = db["news"]


app = Flask(__name__)

#ruta de test
@app.route("/")
def hello():
  return "hola mundo"

#Endpoint noticias que tiene los parametros "categoria" y "palabra clave"
@app.route('/noticias/<categoria>/<palabra_clave>',  methods=['GET'])
def getData(categoria, palabra_clave):
#Realiza una busqueda en MongoDb filtrando por el campo "categoria" y mediante el indice de busqueda de texto que trabaja sobre los campos "title" y "new"
    response = collection.find({"categoria": categoria, "$text": {"$search": palabra_clave}})
#Formatea la respuesta a un tipo lista
    l = list(response)
#Formatea la lista a tipo JSON
    dumps(l)
#Retorna la respuesta como JSON
    return dumps(l)

#inicia el servidor web
if __name__ == "__main__":
  app.run(host='localhost', port=5000, debug=True)
