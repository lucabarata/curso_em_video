num = int(input('\33[4mDigite um número:\33[m '))
r = num % 2
if r == 1:
    print('\33[7;43mIMPAR\33[m')
else:
    print('\33[30;47mPAR\33[m')
