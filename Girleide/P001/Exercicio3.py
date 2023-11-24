def imprimir_caracteres_numericos():

    for i in range(10):
        caractere = str(i)
        decimal = ord(caractere)
        octal = oct(decimal)
        hexadecimal = hex(decimal)

        print(f"'{caractere}' - Decimal: {decimal}, Octal: {octal}, Hexadecimal: {hexadecimal}")

    usuario = input("Digite um caractere: ")
    usuarioDecimal = ord(usuario)
    usuarioOctal = oct(usuarioDecimal)
    usuarioHexadecimal = hex(usuarioDecimal)

    print(f"'{usuario}' - Decimal: {usuarioDecimal}, Octal: {usuarioOctal}, Hexadecimal: {usuarioHexadecimal}")

if __name__ == "__main__":
    imprimir_caracteres_numericos()
