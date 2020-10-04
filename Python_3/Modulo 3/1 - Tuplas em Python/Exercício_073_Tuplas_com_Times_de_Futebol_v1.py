#Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

#a) Os 5 primeiros times.

#b) Os últimos 4 colocados.

#c) Times em ordem alfabética.

#d) Em que posição está o time da Chapecoense.

times = 'INTERNACIONAL' , 'ATLÉTICO-MG','SÃO PAULO','VASCO','FLAMENGO','PALMEIRAS','SANTOS','FLUMINENSE','CEARÁ','FORTALEZA','ATLÉTICO-GO','GRÊMIO','ATHLETICO-PR','SPORT','CORINTHIANS','BAHIA','BOTAFOGO','GOIÁS','CORITIBA','BRAGANTINO'

print('-='*15)
print(f'Lista de times do Brasileirão: {times}')
print('-='*15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-='*15)
print(f'Os 4 últimos são {times[-4:]}')
print('-='*15)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-='*15)
print(f'O Chapeconense está na {times.index('Chapecoense')} posição')