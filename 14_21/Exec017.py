#Ler o cateto oposto, o cateto adjescente de um triangulo retangulo, e calcula o comprimento da hipotenusa#
import math

catop = int(input("Digite o cateto oposto: "))
catadj = int(input("Digite o cateto adjescente: "))

calc = math.pow(catop, 2)
calc2 = math.pow(catadj, 2)
soma = math.sqrt(calc + calc2)

print(soma)