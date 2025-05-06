# Corrija este código para que ele receba um argumento, x, e retorne " xé maior que zero" se xfor positivo 
# (e diferente de zero) e, caso contrário, retorne " xé igual ou menor que zero". Em ambos os casos, 
# substitua xpelo valor real de x.

def corrections(x):
    if x > 0:
        return f"{x} is more than zero."
    else:
        return f"{x} is equal to or less than zero."

