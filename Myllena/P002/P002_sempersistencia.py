tarefas = []

def adicionarTarefas():
    newTarefa = input ("Digite a descrição da tarefa que deseja cadastrar. ").capitalize()
    tarefas.append({'descricao': newTarefa, 'concluida': False})
    print("Tarefa registrada com sucesso! ")
    
def listarTarefas():
    if not tarefas:
        print("Não há nenhuma tarefa registrada. ")
    else:
        print("Lista de Tarefas: ")
        for idx, tarefa in enumerate(tarefas, start = 1):
            status = "[x]" if tarefa['concluida'] else "[ ]"
            print(f"{idx}.{tarefa['descricao']}{status}")
            
def concluirTarefa():
    listarTarefas ()
    id = int(input("digite o ID da tarefa que gostaria de marcar como concluída: ")) - 1
    if 0 <= id < len(tarefas):
        if not tarefas[id]['concluida']:
            tarefas.insert(0, tarefas.pop(id))
            tarefas[0]['concluida'] = True
            print ("Tarefa marcada como realizada! ")
        else:
            print("Esta tarefa já foi concluída. ")
    else:
        print ("ID de tarefa inválido. ")
        
def editarTarefa():
    listarTarefas()
    id = int(input("Digite o ID da tarefa que deseja editar. ")) - 1
    if 0 <= id < len(tarefas):
        newDescricao = input("Digite a nova descrição da tarefa: ").capitalize()
        tarefas[id]['descricao'] = newDescricao
        print("Tarefa editada com sucesso! ")
    else:
        print("ID de tarefa inválido. ")
        
while True:
    print ("__________ TO-DO LIST __________")
    print ("1 - Nova Tarefa.")
    print ("2 - Listar Tarefas. ")
    print ("3 - Marcar como Realizada.")
    print ("4 - Editar Tarefa. ")
    print ("0 - Sair")
    print ("__________________________________")
    
    opcao = input("Digite a opção que deseja realizar. ")
    
    if opcao == '1':
        adicionarTarefas()
    elif opcao == '2':
        listarTarefas()
    elif opcao == '3':
        concluirTarefa()
    elif opcao == '4':
        editarTarefa()
    elif opcao == '0':
        print("Programa encerrado. ")
        break
    else:
        print("Opção inválida, tente novamente. ")