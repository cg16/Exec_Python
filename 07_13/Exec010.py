#Insira um valor em dolares para ser convertido em reais(valor de conversão fixo)#
n = float(input('Quantos reais você quer converter? '))

calc = n * 5.10
print('Você tem agora R${:.2f}'.format(calc))