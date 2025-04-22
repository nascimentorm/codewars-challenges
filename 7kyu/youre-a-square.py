# Um quadrado de quadrados
# Você gosta de blocos de montar. Você gosta especialmente de blocos de montar quadrados. E o que você gosta ainda mais é de organizá-los em um quadrado de blocos de montar quadrados!

# No entanto, às vezes, você não consegue organizá-los em um quadrado. Em vez disso, você acaba com um retângulo comum! Aquelas coisas malditas! Se você tivesse um jeito de saber se está trabalhando em vão... Espere! Pronto! Você só precisa verificar se o número de blocos de construção que você tem é um quadrado perfeito .

# Tarefa
# Dado um número inteiro, determine se ele é um número quadrado :

# Em matemática, um número quadrado ou quadrado perfeito é um número inteiro que é o quadrado de um número inteiro; em outras palavras, é o produto de algum número inteiro consigo mesmo.

# Os testes sempre usarão algum número integral, então não se preocupe com isso em linguagens de tipagem dinâmica.

def is_square(n):
    if n < 0:
        return False
    return int(n ** 0.5) ** 2 == n
