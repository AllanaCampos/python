def lerArquivo():
    id = 0
    lista = []
    try:
        tarefas = open("tarefas.txt", "r")
        for tarefa in tarefas:
            lista.append(tarefa.split("\n")[0])
            id+=1
        tarefas.close()
        return id, lista
    except:
        return id, lista

def salvarArquivo(lista):
    tarefas = open("tarefas.txt", "w")
    for i in lista:
        tarefas.write(i + "\n")

def existeTarefa(listaTarefas, identificador):
    for tarefa in listaTarefas:
        idtfcd = tarefa.split(".")[0]
        status = tarefa.find("[ ]")
        if idtfcd == identificador and status != -1:
            return True
    return False


def main():
    id, listaTarefas = lerArquivo()
    while True:
        print("<----------MENU---------->")
        print("1- Nova Tarefa")
        print("2- Marcar como Realizada")
        print("3- Editar Tarefa")
        print("4- Listar Tarefas")
        print("0- Sair")
        op = int(input())

        match op:
            case 0:
                salvarArquivo(listaTarefas)
                break
            case 1:
                print("Informe a descricao da tarefa")
                descricao = input()
                tarefa = str(id) + ".\t" + descricao.capitalize() + "[ ]"
                listaTarefas.append(tarefa)
                id+=1
            case 2:
                print("Informe o ID da tarefa")
                identificador = int(input())
                try:
                    listaTarefas[identificador] = listaTarefas[identificador].replace("[ ]", "[X]")
                    print("Tarefa realizada com sucesso!")
                except:
                    continue
            case 3:
                print("Informe o ID da tarefa")
                identificador = int(input())
                try:
                    status = "[X]" if listaTarefas[identificador].find("[X]") != -1 else "[ ]"
                    print("Informe a nova descricao")
                    descricao = input()
                    listaTarefas[identificador] = str(identificador) + ".\t" + descricao.capitalize() + status
                except:
                    print("Tarefa não encontrada")
            case 4:
                for i in range(len(listaTarefas)):
                    if listaTarefas[i].find("[X]") != -1:
                        print(listaTarefas[i])
                for i in range(len(listaTarefas)):
                    if listaTarefas[i].find("[ ]") != -1:
                        print(listaTarefas[i])
            case _:
                print("Opção inválida")
                
if __name__ == "__main__":
    main()