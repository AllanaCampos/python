'''
EXERCICIO 6 :  Manipulando listas
'''

#6.1

L = [1,2,3,4,5,6,7,8,9]

print (L[::-1]) # Irá imprimir o inverso da lista, ou seja, de trás para frente.
print (L[-1::]) # Irá imprimir apenas o último da lista 
print (L[:-1:]) # Irá imprimir do primeiro até o penultimo
print (L[::-2]) # Irá imprimir o inverso de dois em dois
print (L[-2::]) # Irá imprimir apenas os dois último da lista 
print (L[:-2:]) # Irá imprimir do primeiro ate o antepenultimo

#6.2 animal do zodiaco chines

Signo = ['Macaco', 'Galo', 'Cão', 'Porco', 'Rato', 'Boi', 'Tigre', 'Coelho', 'Dragão', 'Serpente', 'Cavalo', 'Carneiro']
anoNasc = int(input("Digite o seu ano de nascimento: "))
anoBase = int(1900)
indAnimal = (anoNasc - anoBase) % 12
print("O seu signo chinês é: ", Signo[indAnimal])