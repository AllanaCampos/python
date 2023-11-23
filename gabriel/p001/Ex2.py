'''
Em python os numeros inteiros são representados pela classe int. 
As pricipais diferenças entre python e C++ é que em Python não há
declaração do tipo, dado que toda variavel é um ponteiro para um objeto.
'''

a = 7
b = 3
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
É Importante notar que a Divisão Real sempre retornará
um numero de ponto flutuante, assim caso queira que o resultado
seja um inteiro se torna necessario utilizar a Divisão Truncada
'''
print("tipo de a/b:",type(a/b))
'''
Os operadores aritimeticos compostos são formados pela composição
de um dos operadores aritimeticos com o operador de atribuição '='
Assim dado a operação: a #= b, onde # é um dos operadores aritimeticos
a operação equivalente é: a = a # b
'''
c = 0
print (50*"-")
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
Em python é possivel apresentar numericos muito grandes,
como por exemplo 30!
'''
print (50*"-")
fat = 1
n =30
for i in range(1,n+1,):
    fat*=i
print(n,"! = ", fat)
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
a = 1
b = a
print("a = ", a, "b = ", b)
a = 5 #se dados numericos fossem multaveis b tambem deve ser 5 ja que ambos apontam para o mesmo objeto
print("a = ", a, "b = ", b)

print (50*"-")
print("Metodos disponiveis para variaveis inteiras")
print(dir(int))