# Nesta tarefa simples, você recebe um número e precisa torná-lo negativo. Mas talvez o número já seja negativo?

# Exemplos
# make_negative(1);  # return -1
# make_negative(-5); # return -5
# make_negative(0);  # return 0
# Notas
# O número já pode ser negativo, caso em que nenhuma alteração é necessária.
# Zero (0) não é verificado para nenhum sinal específico. Zeros negativos não fazem sentido matemático.


def make_negative( number ):
    if number == 0:
      return 0
    
    return -abs(number)