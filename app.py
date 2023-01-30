#  Api é um lugar para disponibilizar recursos e/ou funcionalidades

# 1 Objetivo - Criar um api para consultar, criar  e ecxluir livros

# 2 URL Base - dominio ou localhost

# 3 Endpoints -  localhost/livros (GET),localhost/livros/ (Post), localhost/id (GET),localhost/livros/id (PUT), localhost/livros/id (GET), localhost/livros/id (DELETE)

# 4 Quais recursos

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
  {
      "id": 1,
      "titulo": "O Senhor dos Anéis - A Sociedade do Anel",
      "autor": "J.R.R Tolkien"
  },
  {
      "id": 2,
      "titulo": "Harry Potter e a Pedra Filosodal",
      "autor": "J.K Howling"
  },
  {
      "id": 3,
      "titulo": "James Clear",
      "autor": "Hábitos Atômicos"
  },
]
# Consultar(todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
  return jsonify(livros)

# Consulta(id)
@app.route('/livros/<int:id>', methods=['GET'])
def obterLivroPorId(id):
  for livro in livros:
    if livro.get('id') == id:
      return livro
    
# Editar 
@app.route('/livros/<int:id>', methods=['PUT'])
def editarLivroPorId(id):
  livro_alterado = request.get_json()
  for indice,livro in enumerate(livros):
    if livro.get('id') == id:
      livros[indice].update(livro_alterado)

# Criar
@app.route('/livros', methods=['POST'])
def incluirNovoLivro():
  novo_livro = request.get_json()
  livros.append(novo_livro)
  
  return jsonify(livros)

# Ecluir 
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluirLivro(id):
  for indice, livro in enumerate(livros):
    if livro.get('id') == id:
      del livros[indice]
      
  return jsonify(livros)


app.run(port=5000, host='localhost', debug=True)