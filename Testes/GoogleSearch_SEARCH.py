try:
    from googlesearch import search
except ImportError:
    print('No module named ¨google¨ found')

query = 'Monte Carmelo'

for j in search(query, tld='com.br', num=10, stop=10, pause=2):
    print(j)