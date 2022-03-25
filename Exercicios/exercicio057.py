print('Para parar o programa digite \033[32mPARE\033[m.')
sexo = 1
male = female = 0
while sexo != 'PARE':
    sexo = str(input('Sexo: [M/F] ')).strip().upper()
    if sexo != 'PARE':
        if sexo == 'M':
            male += 1
        elif sexo == 'F':
            female += 1
        else:
            print('Opção inválida. Tente novamente.')
print(f'Foram contabilizados {male} pessoas do sexo masculino e {female} pessoas do sexo feminino.')
