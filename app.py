from flask import Flask, jsonify, request

app = Flask(__name__)
usuarios = [
  {
    "id": 1,
    "name": "Beatriz Rocha",
    "email": "beatriz.rocha@outlook.com",
    "phone": "11 982334455"
  },
  {
    "id": 2,
    "name": "Eduardo Mendes",
    "email": "edu.mendes@uol.com.br",
    "phone": "21 977665544"
  },
  {
    "id": 3,
    "name": "Fernanda Oliveira",
    "email": "fernanda.oliveira@gmail.com",
    "phone": "31 991223344"
  },
  {
    "id": 4,
    "name": "Gabriel Santos",
    "email": "gabriel.santos@hotmail.com",
    "phone": "19 988776655"
  },
  {
    "id": 5,
    "name": "Isabela Vieira",
    "email": "isabela.v@yahoo.com",
    "phone": "41 995551122"
  },
  {
    "id": 6,
    "name": "Ricardo Nunes",
    "email": "ricardo.nunes@gmail.com",
    "phone": "51 984443322"
  },
  {
    "id": 7,
    "name": "Letícia Duarte",
    "email": "leticia.duarte@icloud.com",
    "phone": "61 992228877"
  },
  {
    "id": 8,
    "name": "Thiago Barbosa",
    "email": "thiago.b@gmail.com",
    "phone": "81 981110099"
  },
  {
    "id": 9,
    "name": "Vanessa Ribeiro",
    "email": "vane.ribeiro@outlook.com",
    "phone": "71 993334455"
  },
  {
    "id": 10,
    "name": "Marcos Silveira",
    "email": "marcos.silveira@live.com",
    "phone": "48 996667788"
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
