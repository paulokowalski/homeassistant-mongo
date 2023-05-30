from typing import Dict, List
import json

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
        response = []
        for elem in data: response.append(elem)
        return response

    def select_many_not_id(self, filter) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        
        data = collection.find(
            filter,
            {"_id": 0}
        )
        return json.dumps(list(data))

    def edit_many_registries(self, filtro, propriedades) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_many(
            filtro, #Filtro
            { "$set": propriedades }
        )

    def delete_registry(self, filtro) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_one(filtro)