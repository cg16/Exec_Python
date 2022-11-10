#Ler um valor, e aumenta esse valor em 15%#

n = float(input('Insira aqui o seu salario: '))
calc = (n * 15) / 100
final_n = calc + n

print('O valor do seu salario com o aumento de 15% passa a ser {}'.format(final_n))