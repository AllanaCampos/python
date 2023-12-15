from .analiseDados import AnaliseDados

class ListaNomes(AnaliseDados):
    
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []        

    @property
    def lista(self):
        return self.__lista
    
    def addNome(self):
        print("Informe o nome")
        nome = input()
        self.__lista.append(nome)
    
    def entradaDeDados(self):
        print("Quantos elementos existirão na lista de nomes?")
        qtd = int(input())
        for i in range(qtd):
            print(f"Digite o nome {i+1}:")
            valor = input()
            self.__lista.append(valor)

    def mostraMediana(self):
        listaOrdenada = sorted(self.__lista)
        if listaOrdenada.__len__() % 2 == 0:
            pos = (listaOrdenada.__len__() // 2) -1
        else:
            pos = listaOrdenada.__len__() // 2
        print(f"Mediana dos nomes: {listaOrdenada[pos]}")    

    def mostraMenor(self):
        listaOrdenada = sorted(self.__lista)
        print(f"Primeiro nome: {listaOrdenada[0]}")

    def mostraMaior(self):
        listaOrdenada = sorted(self.__lista)
        print(f"Último nome: {listaOrdenada[listaOrdenada.__len__() - 1]}")   

    def __str__(self):
        separador = ", "
        string = separador.join(self.__lista)
        return string
