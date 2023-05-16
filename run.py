from models.connection_options.connection import DbConnectionHandler
from models.repository.correios_repository import CorreiosRepository

db_handle = DbConnectionHandler()
db_handle.connect_to_db()
db_connection = db_handle.get_db_connection()
correios_repository = CorreiosRepository(db_connection)

#home_assistant_repository.insert_document(order)
response = correios_repository.select_many({'data.attributes.rastreio': 'LX681995071CN'})
for elem in response:
    print(elem['_id'])