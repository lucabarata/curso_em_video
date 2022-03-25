aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input('Média: '))
if aluno['média'] < 6:
    aluno['situação'] = 'REPROVADO'
else:
    aluno['situação'] = 'APROVADO'
print(f'Nome: {aluno["nome"]}\nMédia: {aluno["média"]}\nSituação: {aluno["situação"]}')
