'''
Em python os numeros de ponto flutuante são representados pela classe float. 
As pricipais diferenças entre python e C++ é que em Python não há
declaração do tipo, dado que toda variavel é um ponteiro para um objeto.
'''

a = 7.5
b = 3.3
print( "classe que representa os numeros inteiros: ", type(a) )

'''
As operacoes aritimeticas são de Adição, Subtração
Multiplicação, Divisão Real, Divisão Truncada, Módulo, 
Exponenciação e Unário negativo
'''
print (50*"-")
print("Sendo a = ",a,", b = ",b)
print("Adição (a+b) = ",a+b)
print("Subtração (a-b) = ",a-b)
print("Multiplicação (a*b) = ",a*b)
print("Divisão Real (a/b) = ",a/b)
print("Divisão Truncada (a//b) = ",a//b)
print("Módulo (a%b) = ",a%b)
print("Exponenciação (a**b) = ",a**b)
print("Unário negativo (-a) = ",-a)

'''
Os operadores aritimeticos compostos são formados pela composição
de um dos operadores aritimeticos com o operador de atribuição '='
Assim dado a operação: a #= b, onde # é um dos operadores aritimeticos
a operação equivalente é: a = a # b
'''
print (50*"-")

c = 0.0
print("c = ",c,", b = ",b)
c+=b
print("c += b => c = c+b, c =",c)
c*=b
print("c *= b => c = c*b, c =",c)
c-=b
print("c -= b => c = c-b, c =",c)
c//=b
print("c //= b => c= c//b, c =",c)
c**=b
print("c **= b => c= c**b, c =",c)
c%=b
print("c %= b => c= c%b, c =",c)
c/=b
print("c /*= b => c=c/b, c =",c)

'''
Maior e menor potencia de 2 representada em python
'''
print(50*"-")
menorValor = float(2)
maiorValor = float(2)
while True:
    try:
        maiorValor **= 2
        menorValor **= -2
    except:
        break
print("maior potencia de 2",maiorValor)
print("menor potencia de 2",menorValor)
'''
Como citado anteriormente, em python são criados ponteiros
para um objeto quando declaramos uma variavel, contudo temos
dados multaveis e imultaveis, de modo que quando fazemos uma
alteração em um dado do tipo multavel é realizada a modificação
do proprio objeto. Para dados imultaveis quando é realizada a
modificação no mesmo é criado um novo objeto com o novo valor 
e o ponteiro que representa a variavel passa a apontar para esse
novo objeto
'''
print (50*"-")
a = 1.5
b = a
print("a = ", a, "b = ", b)
a = 5.222 #se dados numericos fossem multaveis b tambem deve ser 5 ja que ambos apontam para o mesmo objeto
print("a = ", a, "b = ", b)

print (50*"-")
print("Metodos disponiveis para variaveis inteiras")
print(dir(int))