import funcionarios as f

def main():
    funcionarios = []
    nomeDoArquivo = 'C:/Users/Gabriel Sousa/Desktop/tic18/python/gabriel/p003/questao2/funcionarios.txt'
    f.lerDadosFuncionarios(nomeDoArquivo ,funcionarios)
    f.reajustaDezPorcento(funcionarios)
    op = "x"
    while( op!="0"):
        print()
        print("1 - Adiciona funcionario")
        print("2 - Remove funcionario")
        print("3 - Lista funcionarios")
        print("4 - ler dados funcionarios")
        print("5 - salvar dados arquivos")
        print("6 - reajusta 10% do salario")
        print("0  - Sair")
        op = input("Digite uma das opções acima: ")
        match op:
            case "1":
                f.addFuncionario(funcionarios)
            case "2":
                f.removeFuncionario(funcionarios)
            case "3":
                f.listaFuncionarios(funcionarios)
            case "4":
                f.lerDadosFuncionarios(nomeDoArquivo,funcionarios)
            case "5":
                f.salvarDadosFuncionarios(nomeDoArquivo,funcionarios)
            case "6":
                f.reajustaDezPorcento(funcionarios)




if __name__ == "__main__":
    main()