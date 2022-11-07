#Ler a largura e altura de uma parede e
#calcula a area e a tinta necessaria para pinta-la(cada litro de tinta pinta 2m²)#

Lp= float(input('Insira a largura da parede: '))
Ap= float(input('Insira a altura da parede: '))

calc_area = Lp* Ap

print('A parede possui {} de area, e para pinta-la será necessario {}L de tinta'.format(calc_area, calc_area / 2))