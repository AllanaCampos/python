# Operadores aritméticos e aritméticos compostos em python com float
# Operadores Aritméticos

a = 5.0
b = 2.0

soma = a + b
print("soma: ", soma)
subtracao = a - b
print("subtracao: ", subtracao)
multiplicacao = a * b
print("multiplicacao: ", multiplicacao)
divisao = a / b
print("divisao: ", divisao)

a += 1
b *= 2

# Maior e menor potência de 2 com variáveis float

import sys

maior_potencia_de_2 = sys.float_info.max 
menor_potencia_de_2 = sys.float_info.min 

print("Maior potência de 2:", maior_potencia_de_2)
print("Menor potência de 2:", menor_potencia_de_2)

# Variáveis numéricas de ponto flutuante são imutáveis

x = 3.14
y = x 

print(f'Antes da alteração: x = {x}, y = {y}')
x = 2.71

print(f'Depois da alteração: x = {x}, y = {y}')

# Métodos para variáveis float

numero = 3.14159
print("Valor Absoluto:", abs(numero))
print("Parte Inteira:", int(numero))
print("Arredondamento para Cima:", round(numero))
print("Exponenciação:", numero.__pow__(2)) 
