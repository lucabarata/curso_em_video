somatoria = 0
num = 0
digitados = 0
while num != 999:
    digitados += 1
    somatoria += num
    num = int(input('Digite um número [999 para parar]: '))
print(f'''Somatória: {somatoria}
Digitados: {digitados - 1}''')