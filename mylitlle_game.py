continuar = True
# o import abaixo nos permite usar a função random!
import random
#Aqui começa o codigo principal!
while continuar:
  comecar = input("deseja começar a rolar o dado?")=="sim"
  #O print abaixo permite realizar o random nos numero dos dados e imprimir para o usuario!
  print("Dado lançado!\ndado nº\t", random.randint(1, 6))
  continuar = input("deseja continuar a rolar os dados?\n")== "sim"
  if continuar == 'não':
    break
  elif continuar == int:
   comecar = input("deseja começar a rolar o dado?")=="sim"
   print("Dado lançado!\ndado nº\t", random.randint(1, 6))
   continuar = input("deseja continuar a rolar os dados?\n")== "sim" 
  else:
    print("look at the river!")
