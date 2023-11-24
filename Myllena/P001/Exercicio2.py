'''
EXERCICIO 2: Manipulação de variáveis de tipo inteiro, explorando as características
e os limites.
'''
  

#2.1 OS OPERADORE ARIRMÉTICOS SÃO:

# Adição

x = 5
y = 8
z = x + y

print("z = x + y: ", z, " = ", x, " + ", y,)

# Subtraçõa
#Mesmo operador em C++

z = x - y
print("z = x - y: ", z, " = ", x, " - ", y)

# Multiplicação
#Mesmo operador em C++

z = x * y
print("z = x * y: ", z, " = ", x, " * ", y)

# Divisão (irá retornar a um ponto flutuante)
#Mesmo operador em C++

z = x / y
print("z = x / y: ", z, " = ", x, " / ", y)

# Divisão truncada (retorna a um inteiro, ou seja remove a parte fracionária)
#Em C++ não tem esse operador

z = x // y
print("z = x // y: ", z, " = ", x, " // ", y)

# Modulo
#Mesmo operador em C++

z = x % y 
print("z = x % y: ", z, " = ", x, " % ", y)

# Potencia
#Em C++ não tem esse operador

z = x ** y
print("z = x ** y: ", z, " = ", x, " ** ", y)

# Unário negativo (retorna a o valor negativo da variavel)

z = -x

print("z = -x: ", z, " = - ", x)

#OS OPERADORE ARIRMÉTICOS COMPOSTOS SÃO:

x = 5
y = 8

#maisIgual
#Mesmo operador em C++

z += y 
print("z += y: ", z, " = ", x, " + ", y)

#menorIgual
#Mesmo operador em C++

z -= y 
print("z -= y: ", z, " = ", x, " - ", y)

#vezesIgual
#Mesmo operador em C++

z *= y 
print("z *= y: ", z, " = ", x, " * ", y)

#divididoIgual
#Em C++ só quando as variavéis for do tipo int.
z /= y 
print("z /= y: ", z, " = ", x, " / ", y)

#moduloIgual
#Mesmo operador em C++

z %= y 
print("z %= y: ", z, " = ", x, " % ", y)

#exponeciaçãoIgual
#Mesmo operador em C++

z **= y 
print("z **= y: ", z, " = ", x, " * ", y)

#2.2 calculo de fatorial

a = 30
fatorial = 1
while (a > 1):
    fatorial = fatorial * a
    a = a - 1
print ("O fatorial de 30 é: ", fatorial)

'''
Em C++ o mair valor que seria apresentado é: 2147493647, o que mostra 
uma enorme diferença nas duas linguagens.
'''

# 2.3 variaveis númericas mutáveis

''' Isso significa dizer que o valor de determinada variável 
não pode ser alterada após ser atribuida.
Isso é apresentado a seguir, definindo o valor de K e apontando L para K
o valor de K será incrementado em 1, mas o valor de L que aponta para K não será mudado.
'''

K = 19
L = K
print("K = ", K, "e L que aponta para K recebe : ", L)
K += 1
print ("O valor de K é: ", K, ", e o valor de L é: ", L)

# 2.4 Metodos para Variaveis inteiras

print("Os métodos disponíveis para variáveis inteiras são:")
print(dir(int))