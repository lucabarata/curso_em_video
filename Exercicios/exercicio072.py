numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
n = 0
while True:
    n = int(input('Digite um número [1-10]: '))
    if 0 <= n <= 10:
        print('*' * 7)
        print(numeros[n])
        print('*' * 7)
        break
    print('Tente novamente.', end=' ')
