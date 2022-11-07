#Ler um valor em metros e converte em centimetros e milimetros#

qtd_m = float(input('Digite aqui quantos metros serão calculados: '))

calc_cm = qtd_m * 100
calc_mm = qtd_m * 1000

print('{} metros em centimetros equivale a {:.0f}cm, e em milimetros equivale a {:.0f}mm'.format(qtd_m, calc_cm, calc_mm))
