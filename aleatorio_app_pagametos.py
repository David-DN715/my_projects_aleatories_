def usuario():
  nome = input("digite seu nome:\n")
  senha = input("crie uma senha:\n")
  senha2 = input("redigite a senha criada:\n")
  if senha == senha2:
    print("SENHA OK!")
  else:
    print("invalid password!")
    return nome, senha, senha2

def conta():
  criar_conta = input("Deseja criar uma conta? s = sim e n = não!")
  identidade = 0 
  conta = 0
  while criar_conta == 's':
    identidade = identidade +1
    if conta < 999:
      conta = conta+1 
      print("sua conta:\t",conta, "sua Identidade:\t", identidade)
  else:
    print("Thats all follks !!!")
    return identidade, conta

def menu():
  print("1 - criar usuario")
  print("2 - gerar string de pagamento")

#Principal Code
continuar = True
while continuar:
  menu()
  opcao = int(input("O Que deseja fazer?"))
  if opcao == 1:
    usuario(), conta()
  
