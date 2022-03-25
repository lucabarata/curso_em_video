d = float(input('Distância: '))
if d <= 200:
    preco = d * 0.5
else:
    preco = d * 0.45
print(f'Preço: \33[32mR${preco:.2f}')
