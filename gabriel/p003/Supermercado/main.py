import produtos as prod


def main():
    produtos = []
    op = "x"
    while( op!="0"):
        print()
        print("1 - Adiciona produto")
        print("2 - Remove produto")
        print("3 - Lista produtos")
        print("4 - consultar produto")
        print("0  - Sair")
        op = input("Digite uma das opções acima: ")
        match op:
            case "1":
                prod.addProduto(produtos)
            case "2":
                prod.removeProduto(produtos)
            case "3":
                prod.listaProdutos(produtos)
            case "4":
                prod.consultarProduto(produtos)


if __name__ == "__main__":
    main()


