nomeCompleto = "Girleide Macario dos Santos"
nome, sobrenome = nomeCompleto.split(maxsplit=1)
print("Nome: ", nome)
print("Sobrenome: ", sobrenome)

ordemAlfabetica = sorted([nome, sobrenome])
print("Ordem Alfabética: ", ordemAlfabetica)

tamanhoNome = len(nome)
tamanhoSobrenome = len(sobrenome)
print("Tamanho do Nome: ", tamanhoNome)
print("Tamanho do Sobrenome: ", tamanhoSobrenome)

palindromo = nome == nome[::-1]
print("É Palíndromo: ", palindromo)