import os

def linha(str):
    palavra = len(str) + 2
    print('-' * palavra)
    print(f'{str.upper().strip()}')
    print('-' * palavra)

def clear():
    os.system('cls')

def menu():
    linha(f'''
1 - CADASTRAR
2 - LISTAR''')

def menu2():
    linha('''
1 - LISTAR TUDO
2 - LISTAR ITEM''')

def main():
    produtos = {}
    while True:
        menu()
        linha('Pressione qualquer tecla diferente das opçoes para sair')
        try:
            opcao = int(input('>> '))
            if opcao != 1 and opcao != 2:
                break
        except ValueError:
            break
        while True:
            if opcao == 1:
                clear()
                linha('CADASTRAR                ')
                linha('Pressione a tecla "Q" para voltar ao menu')
                produtos['item'] = str(input('Item: >> '))
                if produtos['item'] == 'q' and 'Q' :
                    clear()
                    break
                else:
                    produtos['preco'] = float(input('Preço: >> '))
                    produtos['quantidade'] = int(input('Quantidade: >> '))
                    with open('cadastrar.txt','a+') as cad:
                        cad.write(f'{str(produtos)}\n')
                        print('ITEM CADASTRADO!')
                        cad.close()
                        continue
            if opcao == 2:
                clear()
                menu2()
                try:
                    linha('Pressione qualquer tecla diferente das opçoes para volta ao menu')
                    opcao = int(input('>> '))
                    if opcao != 1 and opcao != 2:
                        clear()
                        break
                except ValueError:
                    clear()
                    break
                linha('LISTAR                    ')
                with open('cadastrar.txt', 'r') as cad:
                    if opcao == 1:
                        clear()
                        linha('LISTAR                    ')
                        linha('LISTAR TUDO               ')
                        linhas = cad.readlines()
                        for li in linhas:
                            dado = eval(li)
                            for c, v in dado.items():
                                print(f'{c}: {v:<10}',end=' | ')
                            print('')
                        try:
                            linha('Pressione a tecla "Q" para volta ao menu')
                            sair = str(input('>> '))
                            if sair == 'q' or 'Q':
                                clear()
                                break
                        except ValueError:
                            clear()
                            break
                    if opcao == 2:
                        clear()
                        linha('LISTAR                    ')
                        linha('LISTAR ITEM               ')
                        while True:
                            cad.seek(0)
                            item = str(input('Item: >> '))
                            if item == 'q' and 'Q':
                                clear()
                                break
                            else:
                                linhas = cad.readlines()
                                for i in linhas:
                                    if item in i:
                                        dado = eval(i)
                                        print('---------------------------------------------------------------')
                                        for c, v in dado.items():
                                            print(f'{c}: {v:<10}',end=' | ')
                                        print('\n---------------------------------------------------------------')
                                        print('')
                                        continue
                    break



if __name__ == '__main__':
    main()