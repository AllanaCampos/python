import Produtos as p


def main():
    produtos = []
    while True:
        print("Supermercado")
        print("1. Inserir novo produto")
        print("2. Excluir produto")
        print("3. Listar todos os produtos")
        print("4. Consultar preço de um produto")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            inserir_produto()
        elif opcao == '2':
            excluir_produto()
        elif opcao == '3':
            listar_produtos()
        elif opcao == '4':
            consultar_preco()
        elif opcao == '5':
            print("Saindo do programa")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
