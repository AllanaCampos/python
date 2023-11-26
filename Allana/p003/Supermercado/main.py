import produtos as p

def main():
    produtos = []
    op = -1
    while(op != 0):
        print("<-----------MENU----------->")
        print("1- Inserir Produto")
        print("2- Excluir Produto")
        print("3- Listar Produtos")
        print("4- Consultar Produto")
        print("0- Sair")
        op = int(input())
        match op:
            case 1:
                p.novoProduto(produtos)
            case 2:
                p.deletaProduto(produtos)
            case 3:
                p.listarProduto(produtos)
            case 4:
                p.consultarProduto(produtos)
    
if __name__ == "__main__":
    main()


