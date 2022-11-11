#Sorteador de ordem#
import random
n1 = str(input("Escolha um nome: "))
n2 = str(input("Escolha um nome: "))
n3 = str(input("Escolha um nome: "))
n4 = str(input("Escolha um nome: "))

lista = [n1, n2, n3, n4]
rng = random.shuffle(lista)

print("A ordem será ", lista)

