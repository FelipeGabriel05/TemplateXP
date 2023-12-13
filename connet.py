import main
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://felipegabrielgb271:felipe123@cluster0.rsejnr3.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Conexão realizada com sucesso")
    db = client['corretagem_db']
    db.create_collection('xp')
    db.xp.insert_one(main.Main())
except Exception as e:
    print(e)