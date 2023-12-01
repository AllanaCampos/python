def novoFuncionario(funcionarios):
    print("Informe o RG do funcionário")
    rg = input()
    if(any(f["RG"] == rg for f in funcionarios)):
        print("Este funcionário já está cadastrado")
        return
    print("Informe o nome do funcionário")
    nome = input().capitalize()
    print("Informe o sobrenome do funcionário")
    sobrenome = input().capitalize()
    print("Informe o ano de admissão do funcionário")
    admissao = input()
    print("Informe o salário do funcionário")
    salario = float(input())
    funcionarios.append({"RG": rg, "nome": nome, "sobrenome": sobrenome, "admissao": admissao, "salario": salario})

def deletaFuncionario(funcionarios):
    print("Informe o RG do funcionário")
    rg = input()
    for f in funcionarios:
        if f["RG"] == rg:
            funcionarios.remove(f)
            print("Funcionário deletado")
            return
    print("Funcionário não foi encontrado")

def listarFuncionarios(funcionarios):
    func = sorted(funcionarios, key = lambda f: f['nome'])
    for f in func:
        print(f"RG: {f["RG"]}")
        print(f"Nome: {f["nome"]}")
        print(f"Sobrenome: {f["sobrenome"]}")
        print(f"Ano de admissão: {f["admissao"]}")
        print(f"Salário: R${f["salario"]: .2f}")

def consultarFuncionario(funcionarios):
    print("Informe o RG do funcionário")
    rg = input()
    for f in funcionarios:
        if f["RG"] == rg:
            print(f"Nome: {f["nome"]}")
            print(f"Sobrenome: {f["sobrenome"]}")
            print(f"Ano de admissão: {f["admissao"]}")
            print(f"Salário: R${f["salario"]: .2f}")

def Reajusta_dez_porcento(funcionarios):
    for f in funcionarios:
        salario = f["salario"]
        salario += salario*0.1
        f["salario"] = salario

def lerFuncionarios():
    funcionarios = []
    try:
        func = open("funcionarios.txt", "r")
        func = func.readlines()
        for i in range(0, len(func), 5):
            rg = func[i].split("\n")[0]
            nome = func[i + 1].split("\n")[0]
            sobrenome = func[i + 2].split("\n")[0]
            admissao = func[i + 3].split("\n")[0]
            salario = float(func[i + 4].split("\n")[0])
            funcionarios.append({"RG": rg, "nome": nome, "sobrenome": sobrenome, "admissao": admissao, "salario": salario})
        func.close()
        return funcionarios
    except:
        return funcionarios
    
def salvarFuncionarios(funcionarios):
    func = open("funcionarios.txt", "w")
    for f in funcionarios:
        func.write(f["RG"] + "\n")
        func.write(f["nome"] + "\n")
        func.write(f["sobrenome"] + "\n")
        func.write(f["admissao"] + "\n")
        func.write(str(f["salario"]) + "\n")
    func.close()