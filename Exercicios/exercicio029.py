vl = 80
cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m'}
print('\033[32mO limite de velocidade é 80km/h\033[m')
v = int(input('Digite a velocidade do carro: '))
if v > vl:
    print('Você ultrapassou o limite de velocidade! Sua multa será de {}R${:.2f}{}'
          .format(cores['vermelho'], v * 7, cores['limpa']))

else:
    print('{}Você está dentro do limite de velocidade!'.format(cores['verde']))
