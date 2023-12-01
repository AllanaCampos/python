
import Funcionarios as f


def main():
    funcionarios = f.carregar_funcionarios()
    while True:
        print("Funcionario")
        print("1. Inserir novo funcionario")
        print("2. Excluir funcionario")
        print("3. Listar todos os funcionarios")
        print("4. Consultar funcionario")
        print("5. Reajuste salarial")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            f.CadastrarFuncionario(funcionarios)
        elif opcao == '2':
            f.excluir_funcionario(funcionarios)
        elif opcao == '3':
            f.listar_funcionarios(funcionarios)
        elif opcao == '4':
            f.consultar_funcionario(funcionarios)
        elif opcao == '5':
            f.Reajusta_dez_porcento(funcionarios)
        elif opcao == '6':
            f.salvarFuncionarios(funcionarios)
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
