linha1 = []
linha2 = []
linha3 = []
for c in range(0, 3):
    num = int(input(f'Número [0] [{c}]: '))
    linha1.append(num)
for c in range(0, 3):
    num = int(input(f'Número [1] [{c}]: '))
    linha2.append(num)
for c in range(0, 3):
    num = int(input(f'Número [2] [{c}]: '))
    linha3.append(num)
print('-=' * 30)
print(f'''[ {linha1[0]} ] [ {linha1[1]} ] [ {linha1[2]} ]
[ {linha2[0]} ] [ {linha2[1]} ] [ {linha2[2]} ]
[ {linha3[0]} ] [ {linha3[1]} ] [ {linha3[2]} ]''')