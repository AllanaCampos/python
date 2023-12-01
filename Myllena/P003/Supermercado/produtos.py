listaProdutos ={'Nome': '', 'Codigo': 0, 'Preco': 0}
listaGeral = []

def inserirProduto():
    print("Insira o nome do produto que deseja adicionar. ")
    listaProdutos['Nome'] = input().capitalize()
    print("Insira o código do produto.")
    listaProdutos['Codigo'] = str(len(listaGeral)).zfill(13)
    listaProdutos['Codigo'] = input().capitalize()
    print("Digite o preço do produto.")
    listaProdutos['Preco'] = round(float(input()), 2)
    listaGeral.append(dict(listaProdutos))

def excluirProduto():
    print("Digite o nome do produto que deseja excluir")
    excluirNome = input()
    for p in range(len(listaGeral)):
        if listaGeral [p]['Nome'] == excluirNome:
            del listaGeral[p]
            print("O produto foi excluido com sucesso. ")
            break
        
def listarProduto ():
    listaG = sorted(listaGeral, key=lambda p: p['Preco'])
    for i in range(0, len(listaG), 10):
        print("\n Lista de Produtos")
        for produto in listaG[i:i+10]:
            print(f"{produto['Nome']} - R${produto['Preco']: .2f}")
        continuar = input("Deseja exibir mais 10 produtos? (S/N)")
        if continuar.lower() != 's':
            break

def consultarProduto():
    print ("Digite o código do produto que deseja consultar")
    consultarCodigo = input(input())
    for produto in listaGeral:
        if int (produto['Codigo']) == consultarCodigo:
            print(produto ['Nome'] + " - R$" + str(produto['Preco']))
            break   
        