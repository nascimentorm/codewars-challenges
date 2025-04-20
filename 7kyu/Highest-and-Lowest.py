# Nesta pequena tarefa, você recebe uma sequência de números separados por espaços e deve retornar o maior e o menor número.

# Exemplos
# high_and_low("1 2 3 4 5") # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
# Notas
# Todos os números são válidos Int32, não há necessidade de validá-los.
# Sempre haverá pelo menos um número na string de entrada.
# A sequência de saída deve ter dois números separados por um único espaço, e o maior número vem primeiro.

def high_and_low(numbers):
    nums = list(map(int, numbers.split()))
    return f"{max(nums)} {min(nums)}"
