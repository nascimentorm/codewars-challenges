# Retorna o número (contagem) de vogais na string fornecida.

# Consideraremos a, e, i, o, ucomo vogais para este Kata (mas não y).

# A sequência de entrada consistirá apenas de letras minúsculas e/ou espaços.

def get_count(sentence):
    vogais = 'aeiou'
    return sum(1 for letra in sentence if letra in vogais)
