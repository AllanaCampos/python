L = [1,2,3,4,5,6,7,8,9]
'''
[a:b:c] onde a é o elemento inicial, b = o elemento final,
c = o passo, Quando omisso a =0, b=tamanho da lista, c=1 assim:
quando c=-1 a lista seja percorrida ao contrario
[9, 8, 7, 6, 5, 4, 3, 2, 1]
quando a = -1 ele atribui a ao tamanho da lista-1
[9]
quando b = -1 ele atribui ao ultimo valor da lista-1
[1, 2, 3, 4, 5, 6, 7, 8]
De maneira analoga c=-2 a lista é percorrida ao contrario,
mas com o passo de 2
[9, 7, 5, 3, 1]
para a = -2 ele abribui à a o tamanho da lista-2
[8, 9]
para b=-2 ele atribui à b o tamnaho da lista-2
[1, 2, 3, 4, 5, 6, 7]
'''
print(L[::-1]) 
print(L[-1::])
print(L[:-1:])
print(L[::-2])
print(L[-2::])
print(L[:-2:])

'''
Descubra qual o signo de um usuário de acordo com seu ano de nascimento.
'''
print(50*"-")
signo = ("macaco","galo","cão","porco","rato","boi","tigre","coelho","dragao","serpente","cavalo","carneiro")
ano = input("Digite seu ano de nascimento: ")
ano = int(ano)

print("Seu signo é:",signo[ano%12])
