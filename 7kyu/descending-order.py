# Sua tarefa é criar uma função que possa receber qualquer número inteiro não negativo como argumento e retorná-lo com seus dígitos em ordem decrescente. Basicamente, reorganize os dígitos para criar o maior número possível.

# Exemplos:
# Entrada: 42145 Saída:54421

# Entrada: 145263 Saída:654321

# Entrada: 123456789 Saída:987654321


def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))
