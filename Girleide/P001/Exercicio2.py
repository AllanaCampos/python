# o tipo de dado que representa o subconjunto dos inteiros é o tipo int

#---- Exemplos como operadores aritméticos----
# soma
a = 1
b = 2
c = a + b
print("a + b = ", c)

# multiplicação
d = a * b
print ("a * b = ", d)

# divisão
e = a / b
print ("a / b = ", e)

# divisão inteira
f = a // b
print("a // b = ", f)

# resto da divisão
g = a % b
print("a % b = ", g)

# ---- Operadores aritimeticos compostos ----
# adição cumulativa
a += b
print("a = a + b = ", a)

# subtração cumulativa
a -= b
print("a = a - b = ", a)

# multiplicação cumulativa
a *= b
print("a = a * b = ", a)

# divisão cumulaiva
a /= b
print("a = a / b = ", a)

# divisão inteira cumulativa
a //= b 
print("a = a // b = ", a)

# resto da divisão cumulativa
a %= b 
print("a = a % b = ", a)

# ----- diferenças em python em relação a C++ -----

# divisão com Resultado em Ponto Flutuante:
'''Em Python, a divisão de inteiros resulta em um número de ponto flutuante se tiver 
parte fracionária. Em C/C++, a divisão de inteiros gera um resultado truncado, descartando
a parte fracionária.

Exemplo em Python
resultado = 5 / 3  # Resultado: 1.6666666666666667

Exemplo em C/C++
int resultado = 5 / 3;  // Resultado: 1 (sem a parte fracionada)'''

# divisão inteira com //:
'''Em Python, // é usado para realizar a divisão inteira,
enquanto em C/C++, / é usado para divisão inteira truncada.

Exemplo em Python
result = 5 // 3  # Resultado: 1

Exemplo em C/C++
int result = 5 / 3;  // Resultado: 1 (parte fracionária truncada)'''

# ---- representar inteiros signficativamentes grandes ----
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

fatorial_30 = fatorial(30)
print(f"Fatorial de 30: {fatorial_30}")

'em C++ um int pode representar valores no intervalo de -2147483648 a 2147483647, portanto este fatorial não seria suportado'

# ---- variáveis imutáveis ----
'''Em Python, as variáveis numéricas são imutáveis, o que significa que,
quando se atribui um valor a uma variável, ele não pode ser alterado diretamente.
Exemplo:'''

x = 5
y = x

print(f'Antes de alterar: x = {x}, y = {y}')
x = x + 1
print(f'Depois de alterar: x = {x}, y = {y}')

# ---- métodos para variáveis inteiras ----

x = 42
print(x.bit_length()) #Retorna o número mínimo de bits necessário para representar o número.

x = 5
print(x.conjugate())  #Retorna o conjugado complexo do número (não tem efeito em inteiros reais).

x = 255
print(x.to_bytes(2, byteorder='big')) #Retorna uma representação de bytes do número inteiro.

bytes_data = b'\x00\xff'
print(int.from_bytes(bytes_data, byteorder='big'))  # Cria um novo inteiro a partir de uma representação de bytes.

x = 3 + 4j
print(x.real)  # Saída: a parte real do número.

x = 3 + 4j
print(x.imag)  # Saída: a parte imaginária do número.







    

