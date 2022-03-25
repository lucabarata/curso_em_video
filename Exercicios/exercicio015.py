d = float(input('Quilômetros: '))
dias = int(input('Dias: '))
valord = float(input('Valor por km rodado: '))
diaria = float(input('Valor da diária:  '))
valor = (diaria * dias) + (valord * d)
print(f'Distância: {d}km\nTempo: {dias} dias\nValor da diária: R${diaria:.2f}\nValor por km rodado: R${valord:.2f}\n'
      f'Valor cobrado: R${valor:.2f}')
