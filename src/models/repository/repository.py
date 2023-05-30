from typing import Dict, List
from flask import jsonify
from bson import json_util


class Repository:

    def __init__(self, db_connection, collection_name) -> None:
        self.__db_connection = db_connection
        self.__collection_name = collection_name

    def insert_document(self, document: Dict) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)
        return document

    def select_many(self, filter) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(filter)
        serialized_data = json_util.dumps(data)
        return serialized_data, 200

    def select_many_not_id(self):
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({})        
        serialized_data = json_util.dumps(data)
        return serialized_data, 200

    def edit_many_registries(self, filtro, propriedades) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_many(
            filtro, #Filtro
            { "$set": propriedades }
        )

    def delete_registry(self, filtro) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_one(filtro)