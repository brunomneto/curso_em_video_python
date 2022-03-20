"""
Exercício Python 73 adaptado para 2021: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato
Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 6 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time do Bragantino.
"""

tabela = ('Internacional', 'Atlético-MG', 'Flamengo', 'São Paulo', 'Fluminense', 'Palmeiras', 'Grêmio', 'Athletico-PR',
          'Ceará', 'Corinthians', 'Santos', 'Atlético-GO', 'Bragantino', 'Vasco', 'Bahia', 'Sport', 'Fortaleza',
          'Goiás', 'Coritiba', 'Botafogo')

print('\n===== Os times no G6 do Brasileirão 2020/2021 =====')
print(tabela[:6], '\n')
print('\n===== Zona de Rebaixamento =====')
print(tabela[-4:], '\n')

print('\n===== Times da Série A 2020/2021 em Ordem Alfabética =====\n')
ordem = sorted(tabela)
for c in ordem:
    print(c)

print('\n===== Classificação Geral Série A do Campeonato Brasileiro 2020/2021 =====\n')
for pos, time in enumerate(tabela):
    if pos + 1 <= 6:
        print(f'\033[34m{pos + 1}° - {time}\033[m')
    elif pos + 1 <= 8:
        print(f'\033[36m{pos + 1}° - {time}\033[m')
    elif pos + 1 <= 14:
        print(f'\033[32m{pos + 1}° - {time}\033[m')
    elif pos + 1 <= 16:
        print(f'{pos + 1}° - {time}')
    else:
        print(f'\033[31m{pos + 1}° - {time}\033[m')
print('\n\033[34mLibertadores\033[m \033[36mPré-Libertadores\033[m \033[32mSul-Americana\033[m '
      '\033[31mRebaixamento\033[m')

print('\nO Bragantino está na {}ª posição.'.format(tabela.index('Bragantino') + 1))
