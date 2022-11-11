#Sorteia um aluno(a) entre 4 alunos#
import random
n1 = str(input("Insira o nome do primeiro aluno(a): "))
n2 = str(input("Insira o nome do segundo aluno(a): "))
n3 = str(input("Insira o nome do terceiro aluno(a): "))
n4 = str(input("Insira o nome do quarto aluno(a): "))

lista = [n1, n2, n3, n4]
rng = random.choice(lista)

print("O aluno(a) escolhido foi {}".format(rng))
