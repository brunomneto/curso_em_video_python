"""
Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando
os espaços. Exemplos de palíndromos:
"""
print('='*50)
print('{:^50}'.format('DETECTOR DE PALÍNDROMO'))
print('='*50)
print()
frase = str(input('Digite uma frase, sem acentos: ')).strip().upper()
frase = frase.replace('Á', 'A').replace('À', 'A').replace('Â', 'A').replace('Ã', 'A')
frase = frase.replace('Ó', 'O').replace('Ò', 'O').replace('Ô', 'O').replace('Õ', 'O')
frase = frase.split()
frase = ''.join(frase)
# aqui é possível eliminar o **for** **tamanho** e **marcador** usando inverso = frase[::-1]
tamanho = len(frase)
marcador = 0
for c in range(0, tamanho):
    if frase[c] == frase[tamanho - 1 - c]:
        marcador += 1
if marcador == tamanho:
    print('A frase escrita é um palíndromo! ')
else:
    print('A frase escrita não é palíndromo')
