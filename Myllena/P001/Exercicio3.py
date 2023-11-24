'''
EXERCICIO 3: : Manipulação de variáveis de tipo 
string e explorando o uso de print.
'''

#3.1 

for i in range(10):
    print(f"'{chr(ord('0') + i)}' - {ord('0') + i}")
    
#Para imprimir o caractere e seus códigos numéricos em decimal, octal e hexadecimal
for i in range(10):
   
    char = chr(ord('0') + i)
    decimal_code = ord(char)
    octal_code = oct(decimal_code)
    hexadecimal_code = hex(decimal_code)

    
    print(f"'{char}' - Decimal: {decimal_code}, | Octal: {octal_code},  | Hexadecimal: {hexadecimal_code}")
 
 
# 3.2 Solicita e imprime o caractere e seus códigos numéricos em decimal, octal e hexadecimal   
caractere = input("Digite um caractere: ")

decimal_code = ord(caractere)
octal_code = oct(decimal_code)
hexadecimal_code = hex(decimal_code)


print(f"'{caractere}' - Decimal: {decimal_code}, | Octal: {octal_code}, | Hexadecimal: {hexadecimal_code}")

#3.3 

cString = input("Insira um caractere: ")
cInteiro = ord(cString)
print("Em caractere: ", cString, " | Em valor numérico: ", cInteiro, " | Em octal: ", oct(cInteiro), " | Em hexadecimal: ", hex(cInteiro))

#3.4 

'''
Em python os caracteres especiais 'ç' e 'ã', podem ser tratados como unicode
o python suporta esses tipos de caracter se estiver usando a codificação padrão UTF-8, 
que permite caractere acentuados
'''