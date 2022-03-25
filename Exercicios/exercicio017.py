from math import hypot
cax = float(input('Qual o comprimento do cateto adjacente do triangulo retangulo? '))
cox = float(input('Qual o comprimento do cateto oposto triangulo retangulo?' ))
# hipx = (cax ** 2 + cox ** 2) ** (1/2)
hipx = hypot(cax, cox)
print(f'O valor da hipotenusa é igual {hipx:.2f}')
