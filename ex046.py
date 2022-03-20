from time import sleep

print()
print('\033[33m{:-^60}\033[m'.format(' CONTAGEM REGRESSIVA '))
for c in range(10, 0, -1):
    print('\033[32m{:^60}\033[m'.format(c))
    sleep(1)
print('\033[35m{:-^60}\033[m'.format(' FELIZ ANO NOVO! '))
