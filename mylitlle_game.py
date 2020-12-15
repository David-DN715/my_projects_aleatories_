continuar = True
import random
while continuar:
  comecar = input("deseja começar a rolar o dado?")=="sim"
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
