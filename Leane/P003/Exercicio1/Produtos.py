def validarCodigo(codigo):
    if len(codigo) != 13:
        return False

    return codigo.isnumeric()


def inserir_produto():
    codigo = input("Digite o código do produto contendo 13 caracteres numéricos: ")
    while not validarCodigo(codigo):
        codigo = input("Código inválido. Digite o código do produto com 13 caracteres numéricos: ")

    nome = input("Digite o nome do produto: ").capitalize()
    

    print("Informe o preço")
    preco = float(input())
    
    produto = {'Código': codigo, 'Nome': nome, 'Preço': preco}
    produtos.append(produto)
    print("Produto cadastrado com sucesso!")

def excluir_produto():
    codigo = input("Digite o código do produto a ser excluído: ")
    while not validarCodigo(codigo):
        codigo = input("Código inválido. Digite o código do produto com 13 caracteres numéricos: ")
    for produto in produtos:
        if produto['Código'] == codigo:
            produtos.remove(produto)
            print("Produto removido com sucesso!")
            return
    print("Produto não encontrado.")


def listar_produtos():
    print("Lista de produtos:")
    for produto in produtos:
        print(f"Código: {produto['Código']} - Nome: {produto['Nome']} - Preço: R${produto['Preço']:.2f}")


def consultar_preco():
    codigo = input("Digite o código do produto para consultar o preço: ")
    while not validarCodigo(codigo):
        codigo = input("Código inválido. Digite o código do produto com 13 caracteres numéricos: ")
    for produto in produtos:
        if produto['Código'] == codigo:
            print(f"O preço do produto '{produto['Nome']}' é R${produto['Preço']:.2f}")
            return
    print("Produto não encontrado.")

