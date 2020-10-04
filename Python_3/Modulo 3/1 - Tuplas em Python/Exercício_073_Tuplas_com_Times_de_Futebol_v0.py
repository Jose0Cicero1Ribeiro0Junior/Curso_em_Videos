#Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

#a) Os 5 primeiros times.

#b) Os últimos 4 colocados.

#c) Times em ordem alfabética.

#d) Em que posição está o time da Chapecoense.

times = 'INTERNACIONAL' , 'ATLÉTICO-MG','SÃO PAULO','VASCO','FLAMENGO','PALMEIRAS','SANTOS','FLUMINENSE','CEARÁ','FORTALEZA','ATLÉTICO-GO','GRÊMIO','ATHLETICO-PR','SPORT','CORINTHIANS','BAHIA','BOTAFOGO','GOIÁS','CORITIBA','BRAGANTINO'

print('Os 5 primeiros times são {}'.format(times[0:5]))
print('Os 4 últimos colocados são {}'.format(times[-1: -5: -1]))
print('Os times em ordem alfabetica são {}'.format(sorted(times)))
print('A posição da Chapecoense é {} posição'.format(times.index('Chapecoense')))
