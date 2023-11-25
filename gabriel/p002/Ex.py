"""
Para implementar a persistencia de dados, torna-se necessario salvar a
lista listaDeTarefas em um arquivo. O principal modo de fazer isso é quando
for realizada qualquer alteração na lista, haja o upload da nova lista, a
dinamica do arquivo consiste em que cada linha representa uma tarefa da lista
"""
def adicionarTarefa(listaDeTarefas):
        id = listaDeTarefas.__len__()+1;
        descricao = input("digite a descrição tarefa: ")
        tarefa = str(id)+". "+descricao.capitalize()+" [ ]"
        listaDeTarefas.append(tarefa)
        print("Tarefa Registrada!")


def listarTarefas():
    for tarefa in listaDeTarefas:
        print(tarefa)


def marcaComoRealizada(listaDeTarefas):
    id = input("Digite o id da Tarefa que deseja marcar como realizada: ")
    for tarefa in listaDeTarefas:
       if tarefa.find(id) == 0:
            tarefaRealizada = tarefa.replace("[ ]","[x]")
            listaDeTarefas.remove(tarefa)
            listaDeTarefas.insert(0,tarefaRealizada)
            print("Tarefa Realizada")
            return
    print("Tarefa não encontrada")

def editaTarefa(listaDeTarefas):
    id = input("Digite o id da Tarefa que deseja alterar: ")
    for indice,tarefa in enumerate(listaDeTarefas):
       if tarefa.find(id) == 0:
            status = tarefa[-4::]
            descricao = input("digite a descrição tarefa: ")
            tarefa = str(id)+". "+descricao.capitalize()+status
            listaDeTarefas[indice] = tarefa
            print("Tarefa alterada")
            return
    print("Tarefa não encontrada")


def menu(listaDeTarefas):
    print("1 - Adicionar Tarefa")
    print("2 - Marcar Tarefa como Realizada")
    print("3 - Listar Tarefas")
    print("4 - Editar Tarefa")
    print("5 - Sair")
    op = int(input("Escolha uma das opçoes acima"))
    match op:
        case 1:
            sn = "S"
            while sn.upper() == "S":
                adicionarTarefa(listaDeTarefas)
                sn = input("Deseja adicionar mais tarefas? (S/N)")
        case 2:
            sn = "S"
            while sn.upper() == "S":
                marcaComoRealizada(listaDeTarefas)
                sn = input("Deseja marcar mais tarefas como realizada? (S/N)")
        case 3:
            listarTarefas()
        case 4:
            sn = "S"
            while sn.upper() == "S":
                editaTarefa(listaDeTarefas)
                sn = input("Deseja editar mais tarefas? (S/N)")
        case 5:
            return
        case _:
            print("Valor invalido")
            menu(listaDeTarefas)




listaDeTarefas = []
menu(listaDeTarefas)
