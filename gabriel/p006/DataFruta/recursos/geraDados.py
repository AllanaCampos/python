from ..listas.listaIdades import ListaIdades
from ..listas.listaSalarios import ListaSalarios
from random import randint, random

class GeraDados():
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



