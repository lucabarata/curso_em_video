palavras = ('Arroz', 'Batata', 'Cebola', 'Damasco',)
for p in palavras:
    print(f'\n{p.upper()}', end=' = ')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(f'{letras}', end=' ')