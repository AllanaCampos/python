def insereProdutos(Produtos):
    
    Codigo = input("Digite o código do produto (13 caracteres, incluindo 0 a esquerda): ")
    if len(Codigo) == 13 and Codigo.isdigit():
        Nome = input("Digite o nome do produto: ")
        if Nome and Nome[0].isupper():
            
            Preco = float(input("Digite o preço do produto (xx.xx): "))
            
            novoProduto = {
                'codigo': Codigo,
                'nome': Nome,
                'preco': float(Preco)
            }
            Produtos.append(novoProduto)
            print("Produto inserido com sucesso")
        else:
            print("Nome inválido. Deve começar com uma letra maiúscula.")
    else:
        print("Código inválido. Deve conter 13 caracteres numéricos .")
    
def excluiProdutos(Produtos):
    cod = input("Digite o código do produto que deseja excluir:")
    
    produtosRemove = []
    for produtoExcluir in Produtos:
        if produtoExcluir['codigo'] == cod:
            produtosRemove.append(produtoExcluir)

    if produtosRemove:
        for produto in produtosRemove:
            Produtos.remove(produto)
        print("Produto(s) excluído(s)!")
    else:
        print("Produto não encontrado")

    
def listarProdutos(Produtos):
    
    print("Lista de Produtos:")
    
    listaProd = sorted(Produtos, key=lambda x: x['preco'])
    for i, Produtos in enumerate(listaProd, start=1):
        print(f"{i}. Código: {Produtos['codigo']}, Nome: {Produtos['nome']}, Preço: R${Produtos['preco']:.2f}")
        if i % 10 == 0:
            input("Pressione Enter para continuar")

def consultaProdutos(Produtos):
    cod = input("Digite o código do produto para consultar o preço: ")

    for produto in Produtos:
        if produto['codigo'] == cod:
            print(f"Preço do produto {produto['nome']}: R${produto['preco']:.2f}")
            input("Pressione Enter para continuar...")
            return
        
    print("Produto não encontrado.")

