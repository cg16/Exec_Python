#Lê um nome de uma pessoa e mostra se esse nome possui "SILVA" ou não#
nome = str(input("Digite o seu nome: "))
cond = "silva" in nome.lower()
if cond == True:
    print('O seu nome tem Silva')
else:
    print('O seu nome não tem Silva')