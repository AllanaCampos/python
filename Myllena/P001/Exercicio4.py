'''
EXERCICIO 4 :  Manipulação de variáveis de tipo string e explorando os métodos da classe.
'''

#4.1 DECLARANDO VARIAVEL NOME 

Nome =  "Myllena Souza"

#4.2 separando string

splitNome = Nome.split()
firstNome = splitNome [0]
lastNome = splitNome [1]


print(splitNome)
print(firstNome)
print(lastNome)

#4.3 verificando qual antecede a outra em ordem alfabetica


ordem_alfabetica = min([firstNome, lastNome])

print ("O nome que vem primeiro em ordem alfabetica é: ", ordem_alfabetica)

#4.4 Verificando a quantidade de caracteres de cada uma das novas variáveis;

fComprimento = len(firstNome)
lComprimento = len(lastNome)

print("O primeiro nome contém ", fComprimento, " caracteres.")
print("O último nome contém ", lComprimento, " caracteres.")

#4.5 verificação se é palíndromo

def isPalindrome(firstNome):
    processedNome = firstNome.lower()
    
    return processedNome == processedNome[::-1]

print(firstNome, " É um palíndromo?: ", isPalindrome(firstNome))

