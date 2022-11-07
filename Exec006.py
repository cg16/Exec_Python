#Ler um numero e calcula o seu dobro, triplo, e sua raiz#
import math

n = int(input('Digite um numero: '))
raiz = math.sqrt(n)
print('O dobro de {} é {}, o  triplo é {}, e a raiz quadrada é {}'.format(n, n * 2, n * 3, raiz))