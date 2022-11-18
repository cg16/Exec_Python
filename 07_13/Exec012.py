#Ler o preço de um produto e calcula 5% de desconto#

preço = float(input('Insira aqui o preço do produto: '))

calc = (preço * 5) / 100

print('O seu desconto de 5% na compra, é de R${:.2f}'.format(calc))
