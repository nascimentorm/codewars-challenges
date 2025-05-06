# Crie um programa que filtre uma lista de strings e retorne uma lista contendo apenas o nome do seu amigo.

# Se um nome tem exatamente 4 letras, pode ter certeza de que é de um amigo seu! Caso contrário, pode ter certeza de que não é...

# Input = ["Ryan", "Kieran", "Jason", "Yous"]
# Output = ["Ryan", "Yous"]

# Input = ["Peter", "Stephen", "Joe"]
# Output = []
# As strings de entrada conterão apenas letras.
# Observação: mantenha a ordem original dos nomes na saída.

def friend(x):
    return [name for name in x if len(name) == 4]
