from math import radians, sin, cos, tan
vangulo = float(input('Digite o valor do angulo: '))
senx = sin(radians(vangulo))
cosx = cos(radians(vangulo))
tgx = tan(radians(vangulo))
print(f'O angulo de {vangulo} graus tem como:\nSeno {senx:.2f} \nCosseno {cosx:.2f} \nTangente {tgx:.2f}')
