from conexao import MongoConnect

class Aluno():

    def __init__(self):
        self.conexao = MongoConnect()

    def cadastrar(self,json):
        return self.conexao.save(json)

    def excluir(self,nome):

        self.conexao.delete({"nome": nome})

    def mostrar(self,achar):
        #Passa os campos que não quer motrar...
        recebe_var = self.conexao.read({"nome": achar}, {"_id": 0})
        return recebe_var

    def atualizar(self,nome, json):
        # aluno = {'nome': nome, 'sobrenome': sobrenome, 'profissao': profissao}
        self.conexao.update({"nome": nome}, {"$set": json})


