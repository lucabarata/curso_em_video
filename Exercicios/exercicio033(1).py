a = int(input('1° Valor: '))
b = int(input('2° Valor: '))
c = int(input('3° Valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor é \33[31m{}\33[m .'.format(menor))
print('O maior valor é \33[32m{}\33[m .'.format(maior))
