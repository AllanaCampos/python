import funcionarios as f

def main():
    arquivo = "C:/Users/girle/Desktop/Residencia/MODULO 2/Python/python/Girleide/P003/Funcionários/dadosFuncionarios.txt"
    leDados = f.carregaDados(arquivo)
    
    print("Menu:")
    print("1. Reajustar salários em 10%")
    print("2. Imprimir dados atuais")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    while True:
        if opcao == "1":
            print("Dados antes do reajuste:")
            f.imprimeDados(leDados)
            f.reajustaDezPorcento(leDados)
            f.escreveDados(arquivo, leDados)
            print("Salários reajustados e dados escritos no arquivo.")
            break
        elif opcao == "2":
            f.imprimeDados(leDados)
            break
        elif opcao == "3":
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()