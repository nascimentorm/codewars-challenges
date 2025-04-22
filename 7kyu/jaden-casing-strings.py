# Jaden Smith, filho de Will Smith, é o astro de filmes como Karatê Kid (2010) e Depois da Terra (2013). Jaden também é conhecido por algumas de suas filosofias, que ele transmite via Twitter . Ao escrever no Twitter, ele é conhecido por quase sempre usar letras maiúsculas em todas as palavras. Para simplificar, você terá que usar letras maiúsculas em cada palavra. Veja como as contrações devem ser feitas no exemplo abaixo.

# Sua tarefa é converter strings para como seriam escritas por Jaden Smith. As strings são citações reais de Jaden Smith, mas não são escritas com maiúsculas da mesma forma que ele as digitou originalmente.

# Exemplo:

# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())
