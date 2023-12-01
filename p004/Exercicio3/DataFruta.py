
from abc import ABC, abstractmethod

class Data:
    
    def __init__(self, dia = 1, mes = 1, ano = 2000):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, dia):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, mes):
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano
    
    def __str__(self):
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        return  self.__dia == outraData.__dia and \
                self.__mes == outraData.__mes and \
                self.__ano == outraData.__ano
    
    def __lt__(self, outraData):
        if self.__ano < outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes < outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia < outraData.__dia:
                    return True
        return False
    
    def __gt__(self, outraData):
        if self.__ano > outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes > outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia > outraData.__dia:
                    return True
        return False
    
class AnaliseDados(ABC): 

    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados

    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def mostraMediana(self):
        pass
    
    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass

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
	
class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []        
    
    def addData(self):
        print("Informe a data no seguinte formato: DD/MM/YYYY")
        data = input()
        dia = int(data.split(("/"))[0])
        mes = int(data.split(("/"))[1])
        ano = int(data.split(("/"))[2])
        data = Data(dia, mes, ano)
        self.__lista.append(data)

    def entradaDeDados(self):
        print("Quantos elementos existirão na lista de datas?")
        qtd = int(input())
        for i in range(qtd):
            print(f"Digite o a data {i + 1} no seguinte formato: DD/MM/YYYY")
            valor = input()
            dia = int(valor.split(("/"))[0])
            mes = int(valor.split(("/"))[1])
            ano = int(valor.split(("/"))[2])
            data = Data(dia, mes, ano)
            self.__lista.append(data)
    
    def mostraMediana(self):
        listaOrdenada = self.ordena()
        if listaOrdenada.__len__() % 2 == 0:
            pos = (listaOrdenada.__len__() // 2) -1
        else:
            pos = listaOrdenada.__len__() // 2
        print(f"Mediana das datas: {listaOrdenada[pos]}")    
     
    def mostraMenor(self):
        listaOrdenada = self.ordena()
        print(f"Primeira data: {listaOrdenada[0]}")
    
    def mostraMaior(self):
        listaOrdenada = self.ordena()
        print(f"Última data: {listaOrdenada[listaOrdenada.__len__() - 1]}")
    
    def modificaDataAnterior2019(self):
        for i in filter((lambda d : Data(ano=2019).__gt__(d)), self.__lista):
            print(f"Deseja alterar o dia da data {i} para qual dia?")
            dia = int(input())
            i.dia = dia
    
    def __str__(self):
        listaStr = []
        separador = ", "
        for i in self.__lista:
            listaStr.append(str(i))
        string = separador.join(listaStr)
        return string

    def ordena(self):
        listaOrdenada = self.__lista.copy()
        for i in range(listaOrdenada.__len__()):
            for j in range(listaOrdenada.__len__() - i - 1):
                if(listaOrdenada[j].__gt__(listaOrdenada[j + 1])):
                    aux = listaOrdenada[j]
                    listaOrdenada[j] = listaOrdenada[j + 1]
                    listaOrdenada[j + 1] = aux
        return listaOrdenada

class ListaSalarios(AnaliseDados):

    def __init__(self):
        super().__init__(type(float))
        self.__lista = []   

    @property
    def lista(self):
        return self.__lista
    
    def addSalario(self):
        print("Informe o salário")
        salario = float(input())
        self.__lista.append(salario)     

    def entradaDeDados(self):
        print("Quantos elementos existirão na lista de salários?")
        qtd = int(input())
        for i in range(qtd):
            print(f"Digite o salário {i+1}:")
            valor = float(input())
            self.__lista.append(valor)

    def mostraMediana(self):
        listaOrdenada = sorted(self.__lista)
        if listaOrdenada.__len__() % 2 == 0:
            resultado = ListaSalarios.calculaMedia(listaOrdenada[(listaOrdenada.__len__()//2)-1], listaOrdenada[(listaOrdenada.__len__()//2)])
        else:
            resultado = listaOrdenada[listaOrdenada.__len__() // 2]
        print(f"Mediana dos salários: {resultado}")     

    def mostraMenor(self):
        listaOrdenada = sorted(self.__lista)
        print(f"Menor salário: {listaOrdenada[0]}")

    def mostraMaior(self):
        listaOrdenada = sorted(self.__lista)
        print(f"Maior salário: {listaOrdenada[listaOrdenada.__len__() - 1]}") 
    
    def reajusteDezPorcento(self):
        for i in map((lambda s : s + s*0.1), self.__lista):
            print(i)
    
    def __str__(self):
        listaStr = []
        separador = ", "
        for i in self.__lista:
            listaStr.append(str(i))
        string = separador.join(listaStr)
        return string
    
    def calculaMedia(a, b):
        media = (a + b) / 2
        return media

class ListaIdades(AnaliseDados):
    
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []  

    def addIdade(self):
        print("Informe a idade")
        idade = int(input())
        self.__lista.append(idade)
    
    def entradaDeDados(self):
        print("Quantos elementos existirão na lista de idades?")
        qtd = int(input())
        for i in range(qtd):
            print(f"Digite a idade {i+1}:")
            valor = int(input())
            self.__lista.append(valor)
    
    def mostraMediana(self):
        listaOrdenada = sorted(self.__lista)
        if listaOrdenada.__len__() % 2 == 0:
            resultado = ListaIdades.calculaMedia(listaOrdenada[(listaOrdenada.__len__()//2)-1], listaOrdenada[(listaOrdenada.__len__()//2)])
        else:
            resultado = listaOrdenada[listaOrdenada.__len__() // 2]
        print(f"Mediana das idades: {resultado}")     
    
    def mostraMenor(self):
        listaOrdenada = sorted(self.__lista)
        print(f"Menor idade: {listaOrdenada[0]}")
    
    def mostraMaior(self):
        listaOrdenada = sorted(self.__lista)
        print(f"Maior idade: {listaOrdenada[listaOrdenada.__len__() - 1]}") 

    def __str__(self):
        listaStr = []
        separador = ", "
        for i in self.__lista:
            listaStr.append(str(i))
        string = separador.join(listaStr)
        return string
    
    def calculaMedia(a, b):
        media = (a + b) / 2
        return media

def percorrerListas(nomes, salarios):
    for i in zip(nomes.lista, salarios.lista):
        print(i)

def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()
    op = 0
    while(op != 8):
        print("<----------MENU---------->")
        print("1- Incluir um nome na lista de nomes")
        print("2- Incluir um salário na lista de salários")
        print("3- Incluir uma data na lista de datas")
        print("4- Incluir uma idade na lista de idades")
        print("5- Percorrer as listas de nomes e salários")
        print("6- Calcular o valor da folha com um reajuste de 10%")
        print("7- Modificar o dia das datas anteriores a 2019")
        print("8- Sair")
        op = int(input())

        match(op):
            case 1:
                nomes.addNome()
            case 2:
                salarios.addSalario()
            case 3:
                datas.addData()
            case 4:
                idades.addIdade()
            case 5:
                percorrerListas(nomes, salarios)
            case 6:
                salarios.reajusteDezPorcento()
            case 7:
                datas.modificaDataAnterior2019()


if __name__ == "__main__":
    main()