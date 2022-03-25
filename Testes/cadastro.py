print('Olá! Seja bem-vindo(a) ao site Barata!\nPara começarmos faça o login. Se ja estiver cadastrado'
      'ou registre-se agora!')
cadastro = input('Você ja é cadastrado? ')
cadastro = cadastro.upper()
if cadastro == 'sim'.upper():
    login = input('Digite seu login: ')
    senha = input('Digite sua senha: ')
else:
    registro = input('Ok. Então vamos fazer o seu registro!\nCrie um nome de usuário: ')
    csenha = input('Crie uma senha: ')
    c2senha = input('Confirme sua senha: ')
    if csenha != c2senha:
        print('As senhas não conferem! ')
        csenha = input('Digite a senha novamente: ')
        c2senha = input('Confirme novamente: ')
    nome = input('Nome: ')
    email = input('Email: ')