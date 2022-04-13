from aluno import Aluno

aluno = Aluno()

def menu():
    op = int(input('MENU\n'
                   '=-=-=-=-=-=-=-=-=-=-=-=-\n'
                   '1 - CADASTRO\n'
                   '2 - MOSTRAR \n'
                   '3 - ATUALIZAR\n'
                   '4 - DELETAR \n'
                   '5 - SAIR\n'
                   '=-=-=-=-=-=-=-=-=-=-=-=-\n'
                   'DIGITE A OPÇÃO DESEJADA: '))
    return op

p = Aluno()

while True:
    op = menu()

    if op == 1:
        print("Cadastro de nome")
        p.cadastrar()
        print("Sucesso!")

    if op == 2:
        print("Mostrar nome")
        p.mostrar()
        print("Sucesso!")

    if op == 3:
        print("Atualizar nome")
        p.atualizar()
        print("Sucesso!")

    if op == 4:
        print("Deletar nome")
        p.excluir()
        print("Sucesso!")

    if op == 5:
        print("Finalizando...")
        break

print("FIM!")