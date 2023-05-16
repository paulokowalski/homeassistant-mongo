from bson.objectid import ObjectId
from flask import Flask, request

from models.connection_options.connection import DbConnectionHandler
from models.repository.repository import Repository

db_handle = DbConnectionHandler()
collection_name = "correios"
db_handle.connect_to_db()
db_connection = db_handle.get_db_connection()
correios_repository = Repository(db_connection, "correios")
monitoramento_repository = Repository(db_connection, "monitoramento")

app = Flask(__name__)

@app.route('/correios', methods=['GET'])
def correios():
    return correios_repository.select_many_not_id("")

@app.route('/correios', methods=['POST'])
def correios_salvar():
    correios_repository.insert_document(request.json)
    return "ok"

@app.route('/correios', methods=['PUT'])
def correios_atualizar():
    rastreio = request.json['data']['attributes']['rastreio']
    response = correios_repository.select_many({'data.attributes.rastreio': rastreio})
    for elem in response:
        codigo = elem['_id']
        correios_repository.edit_many_registries({'_id': ObjectId(codigo)}, request.json)
    return "ok"

@app.route('/correios/<rastreio>', methods=['DELETE'])
def correios_deletar(rastreio):
    response = correios_repository.select_many({'data.attributes.rastreio': rastreio})
    for elem in response:
        codigo = elem['_id']
        correios_repository.delete_registry({'_id': ObjectId(codigo)})
    return "ok"


app.run(host="192.168.68.125", port=5000)