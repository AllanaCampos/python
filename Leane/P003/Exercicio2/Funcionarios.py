def CadastrarFuncionario(funcionarios):
    rg = input("Digite o rg do funcionario que deseja cadastrar ")

    nome = input("Digite o primeiro nome do funcionario: ").capitalize()
    sobreNome = input("Digite o sobrenome nome do funcionario: ").capitalize()
    
    print("Informe o ano de admissão do funcionário")
    admissao = input()
    
    print("Informe o ano de nascimento do funcionário")
    nascimento = input()
    
    salario = float(input("Informe o salario do funcionario"))
    
    funcionario = {'Rg': rg, 'Nome': nome, 'Sobrenome': sobreNome, 'Admissao': admissao, 'Nascimento': nascimento, 'Salario' : salario}
    funcionarios.append(funcionario)
    print("Funcionario cadastrado com sucesso!")

def excluir_funcionario(funcionarios):
    rg = input("Digite o rg do funcionario que deseja ser excluído: ")
    for funcionario in funcionarios:
        if funcionario['Rg'] == rg:
            funcionarios.remove(funcionario)
            print("Funcionario removido com sucesso!")
            return
    print("Funcionario nao encontrado.")

def listar_funcionarios(funcionarios):
    print("Lista de Funcionarios:")
    for funcionario in funcionarios:
        print(f"Rg: {funcionario['Rg']} - Nome: {funcionario['Nome']} - Sobrenome: {funcionario['Sobrenome']} - Admissao: {funcionario['Adimissao']} - Ano de nascimento: {funcionario['Nascimento']}- Salario: R${funcionario['Salario']}")


def consultar_funcionario(funcionarios):
    codigo = input("Digite o rg do funcionario para consulta: ")
    for funcionario in funcionarios:
        if funcionario['Rg'] == rg:
            print(f"Funcionario '{funcionario['Nome']}' Rg: {funcionario['Rg']} - Ano de admissão: {funcionario['Admissao']}")
            return
    print("Funcionario não encontrado.")

def Reajusta_dez_porcento(funcionarios):
    for funcionario in funcionarios:
        salario = funcionario["Salario"]
        salario += salario*0.1
        funcionario["Salario"] = salario
        return funcionarios

    
def carregar_funcionarios():
    funcionarios = []
    try:
        with open("funcionarios.txt", "r") as func_file:
            func = func_file.readlines()
            for i in range(0, len(func), 6):
                rg = func[i].strip()
                nome = func[i + 1].strip()
                sobrenome = func[i + 2].strip()
                admissao = func[i + 3].strip()
                nascimento = func[i + 4].strip()
                salario = float(func[i + 5].strip())
                funcionarios.append({"Rg": rg, "Nome": nome, "Sobrenome": sobrenome, "Admissao": admissao, "Nascimento": nascimento, "Salario": salario})
            func.close()
    except FileNotFoundError:
        print("Arquivo 'funcionarios.txt' não encontrado.")
    
def salvar(funcionarios):
    func = open("funcionarios.txt", "w")
    for funcionario in funcionarios:
        func.write(funcionario["RG"] + "\n")
        func.write(funcionario["Nome"] + "\n")
        func.write(funcionario["Sobrenome"] + "\n")
        func.write(funcionario["Admissao"] + "\n")
        func.write(funcionario["Nascimento"] + "\n")
        func.write(str(funcionario["Salario"]) + "\n")
    func.close()
