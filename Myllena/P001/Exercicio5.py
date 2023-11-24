'''
EXERCICIO 5 :  Manipulação de variáveis de ponto flutuante, explorando as
características e os limites.
'''

import sys
import math

#5.1 operadores

x = float(2.5)
y = float(1.7)

z = x + y

print("z = x + y: ", z, " = ", x, " + ", y,)

z = x - y
print("z = x - y: ", z, " = ", x, " - ", y)

z = x * y
print("z = x * y: ", z, " = ", x, " * ", y)

z = x / y
print("z = x / y: ", z, " = ", x, " / ", y)

z = x // y
print("z = x // y: ", z, " = ", x, " // ", y)

z = x % y 
print("z = x % y: ", z, " = ", x, " % ", y)

z = x ** y
print("z = x ** y: ", z, " = ", x, " ** ", y)

z = -x

print("z = -x: ", z, " =- ", x)

z += y 
print("z += y: ", z, " = ", x, " + ", y)

z -= y 
print("z -= y: ", z, " = ", x, " - ", y)

z *= y 
print("z *= y: ", z, " = ", x, " * ", y)

z /= y 
print("z /= y: ", z, " = ", x, " / ", y)

z %= y 
print("z %= y: ", z, " = ", x, " % ", y)

z **= y 
print("z **= y: ", z, " = ", x, " * ", y)

#5.2 

maiorPotenciaDoisFloat = 2.0 ** sys.float_info.max_10_exp
menorPotenciaDoisFloat = 2.0 ** sys.float_info.min_10_exp

print("A Maior Potência de 2:", maiorPotenciaDoisFloat)
print(" A Menor Potência de 2:", menorPotenciaDoisFloat)

#5.3 

A = float(19.4)
B = A
print("A = ", A, "e B que aponta para A recebe : ", B)
A += 1
print ("O valor de K é: ", A, ", e o valor de L é: ", B)

#5.4

#conversao para inteiro 
c = float(5.5)
d = int(c)
print("O valor convertido é : ", d)

#arrendondamento

c = float(5.5)
d = round(c)
print("O valor arrendondado é : ", d)

#arrendondamento para cima e para baixo 
c = float(5.56)
d = math.ceil(c)
e = math.floor(c)

print("Arrendondado para cima temos: ", d)
print("Arrendondado para baixo temos: ", e)

#formatando para uma string

c = float(5.5689617)
d = "{:.3f}".format(c)

print("O valor com 3 casas decimais é : ", d)

# verificando se é um inteiro

c = float(7.75)
d = c.is_integer()

print (d)

#operação matematica

c = float(7.75)
d = math.sqrt(c)

print (d)