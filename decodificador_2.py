import string

def decifra(codigo):
    codigo = codigo.split()
    codigo = [list(i) for i in codigo]
    alfabeto = list(string.ascii_lowercase)
    descifrado = []
    pos = []
    for letras in codigo:
        for l in letras:
            if l in alfabeto:
                pos.append(alfabeto.index(l) - 1)
    for p in pos:
        descifrado.append(alfabeto[p])
    return descifrado


print(decifra('uvep pv obeb'))