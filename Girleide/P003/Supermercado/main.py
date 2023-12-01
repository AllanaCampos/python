import produtos

def main():
    
    Produtos = []
    
    while True:
        print("---- Menu ----")
        print("1. Inserir um novo produto")
        print("2. Excluir um produto cadastrado")
        print("3. Listar todos os produtos")
        print("4. Consultar o preço de um produto")
        print("0. Sair")

        opcao = input("Escolha uma opcao: ")
        if opcao == "1":
            produtos.insereProdutos(Produtos)
        elif opcao == "2":
            produtos.excluiProdutos(Produtos)
        elif opcao == "3":
            produtos.listarProdutos(Produtos)
        elif opcao == "4":
            produtos.consultaProdutos(Produtos)
        elif opcao == "0":
            break
        else:
            print("Opcao invalida. Digite outra opcao")

if __name__ == "__main__":
    main()