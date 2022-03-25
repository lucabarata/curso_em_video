# Se o salário for superior à R$1250,00 calcular aumento de 10%
# Inferiores ou igual, calcular aumento de 15%
salario = float(input('Salário: '))
if salario > 1250:
    salario = salario + (salario * 0.10)
else:
    salario = salario + (salario * 0.15)
print('Seu novo salário será no valor de R$\33[32m{:.2f} '.format(salario))
