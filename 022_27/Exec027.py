#Ler um nome e mostra o primeiro e ultimo nome separadamente#

n = str(input('Digite o seu nome: ')).strip()
nome = n.split()

print('O primeiro nome é: {}'.format(nome[0]))
print('O ultimo nome é: {}'.format(nome[len(nome)-1]))

