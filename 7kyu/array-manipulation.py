# Dado um conjunto de inteiros positivos, substitua cada elemento pelo menor elemento maior à sua direita. Se não houver nenhum elemento maior à sua direita, substitua-o por -1. Por exemplo, dado o conjunto

# [8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28],

# a saída desejada é

# [18, 63, 80, 25, 32, 43, 80, 93, 80, 25, 93, -1, 28, -1, -1].

# Sua tarefa é criar uma função que receba um array como argumento, manipule o array conforme descrito acima e, então, retorne o array resultante.

# Nota: Retorne uma nova matriz, em vez de modificar a matriz passada.


def array_manip(array):
    result = []

    for i in range(len(array)):
        min_greater = -1
        for j in range(i + 1, len(array)):
            if array[j] > array[i]:
                if min_greater == -1 or array[j] < min_greater:
                    min_greater = array[j]
        result.append(min_greater)

    return result

