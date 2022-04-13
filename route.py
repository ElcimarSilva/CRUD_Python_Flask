'''Sistema que faz uma CRUD de aluno, sobrenome e profissão em Python com Mongo. '''
from flask import Flask, request, jsonify
from aluno import Aluno

meu_aluno =Aluno()
app = Flask(__name__)

@app.route("/")
def index():
   return "FAAAAlla GodLuck!"

@app.route("/minhaaplicacao/<nome>", methods=['GET']) #Listar
def get(nome):
    volta=meu_aluno.mostrar(nome)
    return volta

@app.route("/minhaaplicacao", methods=['POST'])#Cadastrar
def post():
    data = request.json
    puxa = meu_aluno.cadastrar(data)
    dict = { "id":str(puxa["_id"]),
            "nome": puxa["nome"],
            "sobrenome":  puxa["sobrenome"],
            "profissao": puxa["profissao"]}

    print (dict)
    return jsonify(dict)

@app.route("/minhaaplicacao/<nome>", methods=['PUT'])#Atualizar
def put(nome):
    data = request.json
    meu_aluno.atualizar(nome,data)

    return "Atualizado com sucesso"
@app.route("/minhaaplicacao/<nome>", methods=['DELETE'])
def delete(nome):
    meu_aluno.excluir(nome)
    return "Deletado com sucesso"



if __name__ == '__main__':
    app.run(debug=True)

