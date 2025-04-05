#O primeiro século abrange do ano 1 até o ano 100, inclusive ; o segundo século, do ano 101 até o ano 200, inclusive , etc.

#Tarefa
#Dado um ano, retorne o século em que ele se encontra.

#Exemplos
#1705 --> 18
#1900 --> 19
#1601 --> 17
#2000 --> 20
#742 --> 28

def century(year):
    return (year + 99) // 100