# Uma prisão pode ser representada como um conjunto de celas, onde cada cela contém exatamente um prisioneiro. Um "Verdadeiro" representa uma cela destrancada e um "Falso" representa uma cela trancada.

# [True, True, False, False, False, True, False]
# Começando na cela mais à esquerda, você tem a tarefa de determinar quantos prisioneiros consegue libertar, com uma condição. Você é o prisioneiro na primeira cela. Se a primeira cela estiver trancada (indicada como "Falso"), você não poderá libertar ninguém. Cada vez que você liberta um prisioneiro, as celas trancadas são destrancadas e as destrancadas são trancadas novamente.

# Então, se usarmos o exemplo acima:

# [True, True, False, False, False, True, False]
# // You free the prisoner in the 1st cell.

# [False, False, True, True, True, False, True] 
# // You free the prisoner in the 3rd cell (the 2nd one is locked).

# [True, True, False, False, False, True, False]
# // You free the prisoner in the 6th cell (the 3rd, 4th, and 5th cells are locked).

# [False, False, True, True, True, False, True]
# // You free the prisoner in the 7th cell - and you are done!
# Aqui, libertamos '4' prisioneiros no total.

# Crie uma função que, dado esse arranjo prisional exclusivo, retorne o número de prisioneiros libertados.

# Exemplos
# ([True, True, False, False, False, True, False]) ➞ 4

# ([True, True, True]) ➞ 1

# ([False, False, False]) ➞ 0

# ([False, True, True, True]) ➞ 0
# Notas
# Você é o prisioneiro na primeira cela. Você precisa ser libertado para libertar qualquer outro.
# Você precisa libertar um prisioneiro para trocar as fechaduras. Assim, no segundo exemplo, onde a entrada é [True, True, True], após libertar o primeiro prisioneiro, as fechaduras mudam para [False, False, False]. Como todas as celas estão trancadas, você não pode libertar mais prisioneiros.
# Você sempre começa com o elemento mais à esquerda do array (a primeira cela da prisão). Se todas as celas da prisão à sua direita forem "False", você não poderá libertar mais prisioneiros.


def libertar_prisioneiros(celas):
    libertados = 0
    i = 0
    
    while i < len(celas):
        if celas[i]:  # Se a cela está destrancada
            libertados += 1
            # Inverter todas as celas
            celas = [not cela for cela in celas]
        i += 1
    
    return libertados
