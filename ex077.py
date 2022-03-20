"""
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

conjunto = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')

print()
"""
for c in range(0, len(conjunto)):
    print('Na palavra {} temos'.format(conjunto[c].upper()), end=' ')
    for k in range(0, len(conjunto[c])):
        if conjunto[c][k] in 'aeiou':
            print(conjunto[c][k], end=' ')
    print()
"""
for palavra in conjunto:
    print('Na palavra {} temos'.format(palavra.upper()), end=' ')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')
    print()
