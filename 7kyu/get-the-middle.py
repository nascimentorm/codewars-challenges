# Você receberá uma string não vazia . Sua tarefa é retornar o(s) caractere(s) do meio da string.

# Se o comprimento da string for ímpar, retorne o caractere do meio.
# Se o comprimento da string for par, retorne os 2 caracteres do meio.
# Exemplos:
# "test" --> "es"
# "testing" --> "t"
# "middle" --> "dd"
# "A" --> "A"

def get_middle(s):
    meio = len(s) // 2
    if len(s) % 2 == 0:
        return s [meio - 1:meio + 1]
    else:
        return s[meio]