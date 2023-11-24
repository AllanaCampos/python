L = [1,2,3,4,5,6,7,8,9]
print(L[::-1])
print(L[-1::])
print(L[:-1:])
print(L[::-2])
print(L[-2::])
print(L[:-2:])

anoNasc = int (input("Digite o ano de nascimento"))
signos = ['Macaco', 'Galo', 'Cão', 'Porco', 'Rato', 'Boi', 'Tigre', 'Coelho', 'Dragão', 'Serpente', 'Cavalo', 'Cabra']
anoMacaco = 0
valor = (anoNasc - anoMacaco) % 12
print(f"Seu signo no zodíaco chines e: {signos[valor]}")