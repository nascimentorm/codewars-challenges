# você precisa elevar ao quadrado cada algarismo de um número e concatená-los.

# Por exemplo, se executarmos 9119 na função, sairá 811181, porque 9 2 é 81 e 1 2 é 1. (81-1-1-81)

# Exemplo nº 2: Uma entrada de 765 retornará/deveria retornar 493625 porque 7 2 é 49, 6 2 é 36 e 5 2 é 25. (49-36-25)

# Nota: A função aceita um inteiro e retorna um inteiro.





def square_digits(num):
    return int(''.join(str(int(digit) ** 2) for digit in str(num)))
