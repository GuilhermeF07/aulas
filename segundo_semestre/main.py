lista = []


def menu():
    opcao_valida = ('c', 'r', 'u', 'd','e')
    print("[c] para inserir um item\n[r] para mostrar toda a lista\n[u] substituir um item\n[d] revome um item\n[e] para sair")
    while True:
        opcao = input('Opção: ').lower()
        if opcao in opcao_valida:
            break
        else:
            print('opção inválida, tente novamente.')
    return opcao


def create():
    nome = str(input('Digite seu nome: '))
    lista.append(nome)


def read():
    print(lista)


def update():
    posicao = int(input('posiçao da lista que deseja substrituir: '))
    subs = input('Oque quer colocar na lista: ')
    del lista[posicao]
    lista.insert(posicao, subs)


def delete():
    remove = int(input('Qual item deseja remover: '))
    del lista[remove]


if __name__ == '__main__':
    while True:
        op = menu()

        if op == 'C' or op == 'c':
            create()
        elif op == 'r':
            read()
        elif op == 'u':
            update()
        elif op == 'd':
            delete()
        else:
            break
