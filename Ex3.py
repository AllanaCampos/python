'''
Imprima na tela, utilizando print, cada um dos caracteres
numéricos eseu correspondente código numérico. 
Pesquise como modificar o comportamento do print para 
imprimir como caractere e como número
'''
for i in range(10):
    char = str(i)
    char_code = ord(char)
    print(f"'{char}' - {char_code}")

'''
Modifique o exercício anterior para que a saída imprima também o
código numérico em octal e em hexadecimal.
'''
for i in range(10):
    char = str(i)
    char_code = ord(char)
    print(f"'{char}' - Dec: {char_code}, Oct: {oct(char_code)}, Hex: {hex(char_code)}")
'''
Acrescente ao código do exercício anterior a possibilidade de ler um
caractere qualquer e imprima no mesmo formato do inciso anterior.
Pesquise como ler um valor da entrada padrão.


Em Python, os caracteres especiais, como 'ç' e 'ã', são tratados
de acordo com a codificação de caracteres usada. Python 3 utiliza 
strings Unicode por padrão, o que significa que pode manipular uma 
vasta gama de caracteres, incluindo acentos, caracteres especiais 
e símbolos de vários idiomas. Assim o codigo abaixo tambem funciona
para caracteres especiais
'''
char = input()
char_code = ord(char)
print(f"'{char}' - Dec: {char_code}, Oct: {oct(char_code)}, Hex: {hex(char_code)}")

char = 'ç'
char_code = ord(char)
print(f"'{char}' - Dec: {char_code}, Oct: {oct(char_code)}, Hex: {hex(char_code)}")
char = 'ã'
char_code = ord(char)
print(f"'{char}' - Dec: {char_code}, Oct: {oct(char_code)}, Hex: {hex(char_code)}")