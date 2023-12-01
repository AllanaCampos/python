import produtos

def main():
    while True:
        
        print("____________SUPERMERCADO_________")
        print("O que deseja realizar? ")
        print (" 1. Inserir Produto.")
        print (" 2. Excluir Produto.")
        print (" 3. Listar Produto.")
        print (" 4. Consultar Produto.")
        print(" 0. Encerrar")
        print("__________________________________")
        choice  = int(input())
        
        if choice == 1:
            produtos.inserirProduto()
            
        elif choice == 2:
            produtos.excluirProduto()
        elif choice == 3:
            produtos.listarProduto()
        elif choice == 4:
            produtos.consultarProduto()
        elif choice == 0:
            print("Encerrando Programa.")
            break

if __name__ == "__main__":
    main()
           
