# Desta vez, sem história, sem teoria. Os exemplos abaixo mostram como escrever uma função accum:

# Exemplos:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# O parâmetro de accum é uma string que inclui apenas letras de a..ze A..Z.

def accum(st):
    return '-'.join([char.upper() + char.lower() * i for i, char in enumerate(st)])
