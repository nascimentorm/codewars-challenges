# Escreva uma função que calcule a média dos números em uma determinada matriz.

# Observação: matrizes vazias devem retornar 0.


def find_average(numbers):
    if not numbers:
       return 0
    return sum(numbers) / len(numbers)
