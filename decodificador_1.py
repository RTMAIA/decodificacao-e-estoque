import string

def decifrando_mensagem(codigo):
    decifrado = list()
    alfabeto = list(string.ascii_lowercase)
    positions = list()
    for letras in codigo:
        if letras in alfabeto:
            positions.append((alfabeto.index(letras)) - 1)
    for position in positions:
        decifrado.append(alfabeto[position])
    return f'{decifrado}'

print(decifrando_mensagem('uvep pv obeb'))