tarefas = []

def registraTarefa():
    descricao = input("Digite a descricao da tarefa: ").capitalize()
    tarefas.append(f"{len(tarefas) + 1}.{descricao} [ ]")
    print("Tarefa registrada com sucesso")

def listaTarefas():
    print("Lista de Tarefas:")
    for idx, tarefa in enumerate(tarefas, start=1):
        print(f"{tarefa}")
        
def marcarRealizada():
    listaTarefas()
    opc = int(input("Escolha a tarefa que deseja marcar como realizada "))
    if 1 <= opc <= len(tarefas):
        tarefa = tarefas.pop(opc - 1)
        tarefas.insert(0, tarefa.replace("[ ]", "[x]"))
    else:
        print("Invalido")

def editaTarefas():
    listaTarefas()
    opc = int(input("Escolha a tarefa que deseja editar "))
    
    if 1 <= opc <= len(tarefas):
        novaDescricao = input("Digite a nova descrição da tarefa: ").capitalize()
        tarefas[opc - 1] = f"{opc}.{novaDescricao} {tarefas[opc - 1][-3:]}"
        print("Tarefa editada com sucesso")
    else:
        print("Invalido")

while True:
    print("---- Menu ----")
    print("1. Registrar Nova Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Realizada")
    print("4. Editar Tarefa")
    print("0. Sair")

    opcao = input("Escolha uma opcao: ")
    if opcao == "1":
        registraTarefa()
    elif opcao == "2":
        listaTarefas()
    elif opcao == "3":
        marcarRealizada()
    elif opcao == "4":
        editaTarefas()
    elif opcao == "0":
        break
    else:
        print("Opcao invalida. Digite outra opcao")