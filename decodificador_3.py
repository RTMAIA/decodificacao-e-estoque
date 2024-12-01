import re
import string

def descifra_mensagem(frase):
    frase = frase.split()
    lista_palavras = []
    alfabeto = list(string.ascii_lowercase)
    for letra in frase:
        lista_palavras.append(list(letra))
    for c, v in enumerate(lista_palavras):
        for chave, valor in enumerate(v):
            if valor in alfabeto:
                print(f'{alfabeto[alfabeto.index(valor) - 1]}', end='')
        print(' ',end='')

def codifica_mensagem(frase):
        frase = frase.split()
        lista_palavras = []
        alfabeto = list(string.ascii_lowercase)
        for letra in frase:
            lista_palavras.append(list(letra))
        for c, v in enumerate(lista_palavras):
            for chave, valor in enumerate(v):
                if valor in alfabeto:
                    print(f'{alfabeto[alfabeto.index(valor) + 1]}', end='')
            print(' ', end='')
codifica_mensagem('eu sou o  cara')
print('')
descifra_mensagem('fv tpv p dbsb')