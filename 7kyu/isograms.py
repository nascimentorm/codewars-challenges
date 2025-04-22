# Um isograma é uma palavra sem letras repetidas, consecutivas ou não. Implemente uma função que determine se uma string contendo apenas letras é um isograma. Suponha que a string vazia seja um isograma. Ignore maiúsculas e minúsculas.

# Exemplo: (Entrada --> Saída)

# "Dermatoglyphics" --> true
# "aba" --> false
# "moOse" --> false (ignore letter case)


def is_isogram(string):
    string = string.lower()  # Ignora maiúsculas e minúsculas
    return len(string) == len(set(string))  # Compara o tamanho da string com o conjunto de caracteres únicos
