#O Codigo abaixo é uma lista de compras feita com metodos de listas e funções!

#A função abaixo faz aparecer um menu de opções!
def menu():
    print("1 - adionar item na lista")
    print("2 - para excluir item da lista")
    print("0 - para sair!")
    print(lista1)


#O funçao abaixo permite apagar o item!
def remover(item):
        if item in lista1:
             lista1.remove(item)
        else:
            print("Não encontrado...")
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
    print(lista1)
    if opcao == 1:
        rept = True
        while rept:
            adicionar_lista1(prod = input("Digite item:\n"))
            rept = input("Adionar mais um item? (s/n)") == "s"
        menu()
        opcao = int(input("Digite a opção desejada:\n"))
    elif opcao == 2:
        remover(item=input("Digite item a apagar:\n"))
        menu()
        opcao = int(input("Digite a opção desejada:\n"))
    elif opcao == 0:
        continuar = False
    else:
        print("Opçao invalida!")
        opcao = int(input("Digite a opção desejada:\n"))
