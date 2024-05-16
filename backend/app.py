from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Substitua as credenciais e nome do banco de dados com as suas informações
try:
    client = MongoClient("mongodb://root:1234@cluster0-shard-00-00.mongodb.net:27017,cluster0-shard-00-01.mongodb.net:27017,cluster0-shard-00-02.mongodb.net:27017/Cluster0?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client['Cluster0']  # Nome do banco de dados
    print("Conexão bem-sucedida com MongoDB Atlas")
except Exception as e:
    print("Erro ao conectar com MongoDB Atlas:", e)
    exit(1)

@app.route('/add', methods=['POST'])
def add_record():
    data = request.get_json()
    result = db.livros.insert_one(data)  # Substitua your_collection_name pelo nome da sua coleção
    return jsonify({"result": str(result.inserted_id)})

@app.route('/get', methods=['GET'])
def get_records():
    records = list(db.livros.find())
    for record in records:
        record['_id'] = str(record['_id'])
    return jsonify(records)

if __name__ == '__main__':
    app.run(debug=True)
