from ..listas.listaSalarios import ListaSalarios
from ..listas.listaIdades import ListaIdades
from random import randint, random

def geraListaIdade(n, iMin = 18, iMax = 65):
    idades = []
    for _ in range(n):
        idades.append(randint(iMin,iMax+1))
    return ListaIdades(idades)

def geraListaSalarios(n, sMin = 1320, sMax = 13200):
    salarios = []
    for _ in range(n):
        salarios.append( sMin + random*(sMax-sMin))
    return ListaSalarios(salarios)


def main():
    idades = geraListaIdade(5000)
    idades.mostraMediana()
    idades.mostraMenor()
    idades.mostraMaior()


if __name__ == "__main__":
    main()
