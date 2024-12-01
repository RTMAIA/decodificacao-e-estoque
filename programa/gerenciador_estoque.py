import os

produtos = dict()
while True:
    print('---PROGRAMA GERENCIAMENTO ESTOQUE---')
    print('Digite "Q" para sair do programa!')
    print('''
|-----------------------------------|
|         1 - Cadastrar             |
|         2 - Listar                |
|         3 - Valores               |
|-----------------------------------|'''.strip())
    opcao = input('>> ')
    if opcao == 'Q'.lower():
        break
    else:
        os.system('cls')
        opcao = int(opcao)
        if opcao == 1:
            while True:
                arquivo = open('arquivo.txt', 'a+')
                print('------------CADASTRAR---------------')
                print('Digite "Q" para voltar')
                produtos['Item'] = str(input('Item: >> ').title())
                if produtos['Item'].title() == 'Q':
                    os.system('cls')
                    break
                else:
                    produtos['Preco'] = float(input('Preco: >> '))
                    produtos['Quantidade'] = int(input(f'Quantidade: >> '))
                    produtos['Valor total'] = produtos['Preco'] * produtos['Quantidade']
                    arquivo.write(f'{str(produtos)} \n')
                    arquivo.close()
                    print('Item cadastrado!')

                    continue
            continue
        if opcao == 2:
            print('--------------LISTAR-----------------')
            print('Digite "Q" para sair')
            print('''
|-----------------------------------|
|         1 - Listar Tudo           |
|         2 - Listar Item           |
|-----------------------------------|'''.lstrip())
            op = input('>> ')
            if op == 'Q'.lower():
                os.system('cls')
                continue
            else:
                op = int(op)
                if op == 1:
                    with open('arquivo.txt', 'r') as arquivo:
                        os.system('cls')
                        print('------------------------------------LISTAR TUDO---------------------------------------')
                        print('Digite "Q" para voltar')
                        print('-' * 86)
                        linhas = arquivo.readlines()
                        for linha in linhas:
                            dados = eval(linha)
                            for c, v in dados.items():
                                if type(v) == str or type(v) == int:
                                    print(f'{c}: {v:<10} |', end='')
                                if type(v) == float:
                                    print(f'{c}: {v:<10,.2f} |', end='')
                            print('')
                            print('-' * 86)
                    voltar = str(input('>> '))
                    if voltar.upper() == 'Q':
                        os.system('cls')
                        continue
                elif op == 2:
                    with open('arquivo.txt', 'r') as arquivo:
                        os.system('cls')
                        print('------------LISTAR ITEM---------------')
                        print('Digite "Q" para voltar')
                        print('Pesquisar item: ')
                        linhas = arquivo.readlines()
                        item = str(input('>> ').title())
                        for linha in linhas:
                            if item in linha:
                                dados = eval(linha)
                                print('-' * 86)
                                for c, v in dados.items():
                                    if type(v) == str or type(v) == int:
                                        print(f'{c}: {v:<10} |', end='')
                                    if type(v) == float:
                                        print(f'{c}: {v:<10,.2f} |', end='')
                                print('')
                                print('-' * 86)
                                voltar = str(input('>> ').upper())
                    if voltar == 'Q':
                        os.system('cls')
                        continue
                    if item == 'Q':
                        os.system('cls')
                        continue
        if opcao == 3:
            with open('arquivo.txt', 'r') as arquivo:
                os.system('cls')
                print('------------VALORES---------------')
                print('Digite "Q" para voltar')
                valor_total = 0
                linhas = arquivo.readlines()
                for linha in linhas:
                    dados = eval(linha)
                    valor_total += dados['Valor total']
                print(f'Valor total: R${valor_total:_.2f}'.replace('_', ','))
                voltar = str(input('>> ').upper())
                if voltar == 'Q':
                    os.system('cls')
                    continue
            break
    break
