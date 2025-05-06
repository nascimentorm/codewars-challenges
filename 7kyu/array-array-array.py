# Você recebe uma matriz inicial de 2 valores (x). Você a usará para calcular uma pontuação.

# Se ambos os valores em (x) forem números, a pontuação será a soma dos dois. Se apenas um for um número, a pontuação será esse número. Se nenhum for um número, retorne 'Void!'.

# Após obter sua pontuação, você deve retornar uma matriz de matrizes. Cada submatriz será igual a (x) e o número de submatriz deve ser igual à pontuação.

# Por exemplo:

# se (x) == ['a', 3] você deve retornar [['a', 3], ['a', 3], ['a', 3]]

def explode(arr):
    a, b = arr
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        score = a + b
    elif isinstance(a, (int, float)):
        score = a
    elif isinstance(b, (int, float)):
        score = b
    else:
        return 'Void!'
    return [arr] * int(score)
