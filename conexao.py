from pymongo import MongoClient
from pprint import pprint
# pip install pymongo

class MongoConnect():

    def __init__(self):
        self.cliente = MongoClient('localhost', 27017)
        self.banco = self.cliente.flask_bd_mongo  # nome do banco
        self.colecao = self.banco.aluno  # nome da coleção

    def save(self, json):
        try:
            meu_retorno = self.colecao.insert_one(json)
            minhaVar = (self.colecao.find_one({"_id": meu_retorno.inserted_id}))
            return minhaVar
        except Exception as e:
            print("problema ao salvar registro")
            print(json)
            print(e)

    def update(self, json, fields):#query, field
        try:
            self.colecao.update(json, fields)
        except Exception as e:
            print("problema ao UPDATE registro")
            print(json)#query
            print(e)


    def delete(self, json):
        try:
            self.colecao.remove(json)
        except Exception as e:
            print("problema ao DELETAR registro")
            print(json)
            print(e)

    def read(self, query=None, projection=None): #,escondido=None
        try:
            for vai_la in self.colecao.find(query, projection): #,escondido
                return vai_la
        except Exception as e:
            print("problema ao MOSTRAR registro")
            print(query, projection)
            print(e)
