# O codigo abaixo é uma lista de compras!

#A função abaixo faz aparecer um menu de opções!
def menu():
    print("1 - adionar item na lista")
    print("2 - para excluir item da lista")
    print("0 - para sair!")


#O for abaixo permite passa pelos elemntos da lista e se encontrar apagar o item!
def remover(item):
    for item in lista1:
        if item in lista1:
            remover=input("deseja remover da lista?")=="sim"
            if remover == "sim":
                lista.remove(itens)
        else:
            print("Não encontrado!...")
            return lista1

# o funcao abaixo permite adicionar um elemento a lista1 de compras!
def adicionar_lista1(prod):
    lista1.append(prod)
    return lista1  

lista1 = []
continuar = True
#a função abaixo importa uma outra função do sistema operacional!
import os
#abaixo chamamos a função para mostrar o menu!
menu()
#Abaixo temos um input para selecionar uma das opçoes do menu!
opcao = int(input("Digite a opção desejada:\n"))

#Começa o codigo principal!
while continuar:
    os.system('clr')
    input("Press any key...!")
    if opcao == 1:
        rept = True
        while rept:
            adicionar_lista1(prod = input("Digite item:\n"))
            rept = input("Adionar mais um item? (s/n)") == "s"
        menu()
        opcao = int(input("Digite a opção desejada:\n"))
    elif opcao == 2:
        remover(item = input("Digite item a apagar:\n"))
        print(lista1)
        
    elif opcao == 0:
        continuar = False
    else:
        print("Opçao invalida!")
        opcao = int(input("Digite a opção desejada:\n"))
