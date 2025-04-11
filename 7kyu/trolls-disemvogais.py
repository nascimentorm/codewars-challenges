# Trolls estão atacando sua seção de comentários!

# Uma maneira comum de lidar com essa situação é remover todas as vogais dos comentários dos trolls, neutralizando a ameaça.

# Sua tarefa é escrever uma função que receba uma string e retorne uma nova string com todas as vogais removidas.

# Por exemplo, a sequência de caracteres "Este site é para perdedores, LOL!" se tornaria "Ths wbst s fr lsrs LL!".

# Nota: para este kata o som ynão é considerado uma vogal.

def disemvowel(string_):
    vogais ='aeiouAEIOU'
    return ''.join(char for char in string_ if char not in vogais)
    