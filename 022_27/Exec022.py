#Lê o nome completo de uma pessoa e mostra algumas variações com transformação de string#
nome = str(input('Digite o seu nome completo: ')).strip()

print('Nome todo em maiusculo:', nome.upper())
print('Nome todo em minusculo:', nome.lower())
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('O primeiro nome possui {} letras'.format(nome.find(' ')))