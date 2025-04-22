# Verifique se uma string tem a mesma quantidade de "x" e "o". O método deve retornar um booleano e não diferenciar maiúsculas de minúsculas. A string pode conter qualquer caractere.

# Exemplos de entrada/saída:

# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

def xo(s):
    s = s.lower()  # Ignora maiúsculas e minúsculas
    return s.count('x') == s.count('o')  # Conta o número de 'x' e 'o' e compara
