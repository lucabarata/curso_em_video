
def lin():
    print('-'*30)


def mensagem(msg):
    print('-'*20)
    print(msg)
    print('-'*20)


mensagem('   Sistema é foda')


def soma(a, b):
    s = a + b
    print(s)


soma(b=3, a=5)


def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print()


contador(2, 5, 4, 4)
contador(1, 2, 3, 4, 5)


def contador2(*num):
    tam = len(num)
    print(f'{num} -> {tam}')


contador2(1, 2, 3, 4, 5, 6, 7, 8)
contador2(1, 3, 5, 7)
contador2(2, 4, 6, 8)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


lista = [1, 2, 3, 4]
dobra(lista)
print(lista)


def soma2(* valores):
    som = 0
    for n in valores:
        som += n
    print(f'Soma de {valores} é {som}')


soma2(1, 3, 5)
soma2(2, 4, 6)


# Programa principal
