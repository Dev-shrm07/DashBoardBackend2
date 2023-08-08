from flask import Flask, jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://sharmakavyaop702:qsGaeuzAMbuWIQ6r@cluster0.zmpglyi.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))

app = Flask(__name__)

def get_data():
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    database = client["databse"]
    db = database["databse1"]

    data = list(db.find())

    
    for document in data:
        document['_id'] = str(document['_id'])

    return jsonify(data)

@app.route("/", methods=["GET"])
def hello_world():
    return get_data()


if __name__=="__main__":
    app.run()
