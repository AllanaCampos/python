listaProdutos ={'nome': '', 'codigo': 0, 'preco': 0}
listaGeral = []

def inserirProduto():
    print("Insira o nome do produto que deseja adicionar. ")
    listaProdutos['nome'] = input().capitalize()
    print("Insita o código do produto.")
    listaProdutos['codigo'] = str(len(listaGeral)).zfill(13)
    print("Digite o preço do produto")
    listaProdutos['preco'] = round(float(input()), 2)
    listaGeral.append(dict(listaProdutos))

def excluirProduto():
    print("Digite o nome do produto que deseja excluir")
    excluirNome = input()
        