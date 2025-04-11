# Escreva uma função que receba um array de números e retorne a soma deles. Os números podem ser negativos ou não inteiros. Se o array não contiver nenhum número, você deverá retornar 0.

# Exemplos
# Entrada: [1, 5.2, 4, 0, -1]
# Saída:9.2

# Entrada: []
# Saída:0

# Entrada: [-2.398]
# Saída:-2.398

# Suposições
# Você pode assumir que só lhe são fornecidos números.
# Você não pode presumir o tamanho do array.
# Você pode assumir que obtém um array e, se o array estiver vazio, retorna 0.


def sum_array(a):
    total = 0
    for num in a:
        total += num
    return total
