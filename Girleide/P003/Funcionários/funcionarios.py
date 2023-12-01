def carregaDados(arquivo):
    leDados = []

    with open(arquivo, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            Dados = {
                'nome': data[0],
                'sobrenome': data[1],
                'anoNascimento': int(data[2]),
                'rg': data[3],
                'anoAdmissao': int(data[4]),
                'salario': float(data[5])
            }
            leDados.append(Dados)    
    return leDados

def imprimeDados(leDados):
    print("Dados atuais:")
    for Dados in leDados:
        print(f"Nome: {Dados['nome']} {Dados['sobrenome']}, Ano de Nascimento: {Dados['ano_nascimento']}, RG: {Dados['rg']}, Ano de Admissão: {Dados['ano_admissao']}, Salário: R${Dados['salario']:.2f}")

def escreveDados(arquivo, leDados):
    try:
        with open(arquivo, 'w') as file:
            for Dados in leDados:
                line = f"{Dados['nome']},{Dados['sobrenome']},{Dados['anoNascimento']},{Dados['rg']},{Dados['anoAdmissao']},{Dados['salario']}\n"
                file.write(line)
        print("Dados escritos com sucesso.")
    except Exception as e:
        print(f"Erro ao escrever no arquivo: {e}")

def reajustaDezPorcento(leDados):
    for Dados in leDados:
        Dados['salario'] *= 1.1