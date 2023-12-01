def lerDadosFuncionarios(nomeDoArquivo,funcionarios):
    with open(nomeDoArquivo, 'r') as file:
        lines = file.readlines()
        for line in lines:
            dados = line.strip().split(',')
            funcionario = {
                'nome': dados[0],
                'sobrenome': dados[1],
                'anoDeNascimento': int(dados[2]),
                'RG': dados[3],
                'anoDeAdmissao': int(dados[4]),
                'salario': float(dados[5])
            }
            funcionarios.append(funcionario)


def salvarDadosFuncionarios(nomeDoArquivo, funcionarios):
    with open(nomeDoArquivo, 'w') as file:
        for funcionario in funcionarios:
            file.write(f"{funcionario['nome']},{funcionario['sobrenome']},{funcionario['anoDeNascimento']},{funcionario['RG']},{funcionario['anoDeAdmissao']},{funcionario['salario']}\n")


def reajustaDezPorcento(funcionarios):
    for funcionario in funcionarios:
        funcionario['salario'] = round(funcionario['salario']*1.1,2)


def addFuncionario(funcionarios):
    rg = input("informe o RG do funcionario ")
    if not rg.isdigit():
        print("RG invalido")
        return
    for funcionario in funcionarios:
        if funcionario["rg"] == rg:
            print("RG ja existente")
            print("Funcionario não adicionado")
            return
    nome  = input("digite o nome do funcionario: ")
    sobrenome  = input("digite o sobrenome do funcionario: ")
    anoDeNascimento = int( input("digite o ano de nascimento: ") )
    anoDeAdmissao = int( input("digite o ano de admissão: ") )
    salario = float( input("digite o salario do funcionario") )
    funcionarios.append({"nome": nome, "sobrenome": sobrenome, "anoDeNascimento": anoDeNascimento, "RG": rg, "anoDeAdmissao": anoDeAdmissao, "salario": salario})

def removeFuncionario(funcionarios):
    rg = input("informe o rg do funcionario: ")
    for funcionario in funcionarios:
        if funcionario["RG"] == rg:
            funcionarios.remove(funcionario)
            print("Funcionario excluido")
            return
    print("Funcionario não encontrado")

def listaFuncionarios(funcionarios):
    funcionariosOrdenados = sorted(funcionarios, key=lambda x: x['salario'])
    i=0
    for funcionario in funcionariosOrdenados:
        print(funcionario)
        i+=1
        if(i%10 == 0):
            op = input("deseja exibir mais funcionarios? (s/n)").lower()
            if op!="s":
                return