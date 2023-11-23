
'''
Declare uma variável nome atribuindo a ela seu nome completo;
'''
nome = "gabriel dos santos sousa"
print(nome)


'''
Pesquise por funcionalidades já implementadas nas strings e separe
em duas variáveis novas seu nome do seu sobrenome;
'''
print(50*"-")
n = nome.split();
prenome = n[0];
sobrenome = ' '.join(n[1:])
print(prenome)
print(sobrenome)


'''
Verifique qual das duas novas variáveis antecede a outra na ordem
alfabética;
'''
print(50*"-")
if nome>sobrenome:
    print("sobrenome vem primeiro")
else:
    print("nome vem primeiro")

'''
Verifique a quantidade de caracteres de cada uma das novas variáveis;
'''
print(50*"-")
print("quantidade de caracteres do nome:", prenome.__len__())
print("quantidade de caracteres do sobrenome:", sobrenome.__len__())
'''
Verifique se seu nome é uma palíndromo
'''
print(50*"-")
for i in range(prenome.__len__()//2):
    if prenome[i] != prenome[-i]:
        print(prenome,"não é um palindromo")
        break
else:
    print(prenome,"é um palimodro")