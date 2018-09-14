from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.json_util import dumps

client = MongoClient('localhost', 27017)
db = client['newsdb']
db.authenticate('cic', 'cic1234*')
collection = db["news"]

app = Flask(__name__)

@app.route("/")
def hello():
  return "hola mundo"

@app.route('/noticias/<categoria>/<palabra_clave>',  methods=['GET'])
def getData(categoria, palabra_clave):
    response = collection.find({"categoria": categoria, "$text": {"$search": palabra_clave}})
    l = list(response)
    dumps(l)
    return dumps(l)


if __name__ == "__main__":
  app.run(host='localhost', port=5000, debug=True)