from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = [
  {
    "id": 1,
    "name": "Ana Lú",
    "email": "ana.lucia@gmail.com",
    "phone": "14 981469782"
  },
  {
    "id": 2,
    "name": "Carlos Henrique",
    "email": "carlos.henrique@gmail.com",
    "phone": "14 997845612"
  },
  {
    "id": 3,
    "name": "Mariana Souza",
    "email": "mariana.souza@gmail.com",
    "phone": "14 996321478"
  },
  {
    "id": 4,
    "name": "Felipe Martins",
    "email": "felipe.martins@gmail.com",
    "phone": "14 981234567"
  },
  {
    "id": 5,
    "name": "Juliana Costa",
    "email": "juliana.costa@gmail.com",
    "phone": "14 994567812"
  },
  {
    "id": 6,
    "name": "Rafael Lima",
    "email": "rafael.lima@gmail.com",
    "phone": "14 992145678"
  },
  {
    "id": 7,
    "name": "Camila Ferreira",
    "email": "camila.ferreira@gmail.com",
    "phone": "14 998741236"
  },
  {
    "id": 8,
    "name": "Bruno Almeida",
    "email": "bruno.almeida@gmail.com",
    "phone": "14 987456321"
  },
  {
    "id": 9,
    "name": "Patrícia Gomes",
    "email": "patricia.gomes@gmail.com",
    "phone": "14 991236547"
  },
  {
    "id": 10,
    "name": "Lucas Andrade",
    "email": "lucas.andrade@gmail.com",
    "phone": "14 995874123"
  }
]

@app.route('/')
def home():
    return jsonify({"message": "API de Usuários", "endpoints": {"/usuarios": "GET - Lista todos os usuários"}})

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios)

if __name__ == '__main__':
    app.run(debug=True)
