import funcionarios as f

def main():
    funcionarios = f.lerFuncionarios()
    op = -1
    while(op != 0):
        print("<-----------MENU----------->")
        print("1- Inserir Funcionarios")
        print("2- Excluir Funcionarios")
        print("3- Listar Funcionarios")
        print("4- Consultar Funcionarios")
        print("0- Sair")
        op = int(input())
        match op:
            case 1:
                f.novoFuncionario(funcionarios)
            case 2:
                f.deletaFuncionario(funcionarios)
            case 3:
                f.listarFuncionarios(funcionarios)
            case 4:
                f.consultarFuncionario(funcionarios)
            case 0:
                f.salvarFuncionarios(funcionarios)
    
if __name__ == "__main__":
    main()


