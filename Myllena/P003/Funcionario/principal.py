import funcionarios as f

def main():
    funcionarios = f.lerFuncionarios()
    opcao = -1
    
    while(opcao != 0):
        print("_________________MENU________________")
        print("O que deseja realizar? ")
        print (" 1. Inserir Funcionário.")
        print (" 2. Excluir Funcinários.")
        print (" 3. Listar Funcinários.")
        print (" 4. Consultar Funcionários")
        print (" 5. Reajuste.")
        print(" 0. Encerrar")
        print("__________________________________")
        opcao = int(input())
        
        match opcao:
            
            case 1:
                f.novoFuncionario(funcionarios)
            
            case 2:
                f.excluirFuncionario(funcionarios)
            
            case 3:
                f.listarFuncionarios(funcionarios)
            
            case 4:
                f.consultarFuncionario(funcionarios)
            
            case 5:
                f.ReajustaDezPorcento(funcionarios)
           
            case 0:
                f.salvarFuncionarios(funcionarios)    
                
if __name__ == "__main__":
    main()