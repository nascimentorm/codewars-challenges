# O ácido desoxirribonucleico (DNA) é uma substância química encontrada no núcleo das células e carrega as "instruções" para o desenvolvimento e funcionamento dos organismos vivos.

# Se você quiser saber mais: http://en.wikipedia.org/wiki/DNA

# Em sequências de DNA, os símbolos "A" e "T" são complementares um do outro, assim como "C" e "G". Sua função recebe um lado do DNA (sequência, exceto para Haskell); você precisa retornar o outro lado complementar. A sequência de DNA nunca está vazia ou não há DNA algum (novamente, exceto para Haskell).

# Mais exercícios semelhantes podem ser encontrados aqui: http://rosalind.info/problems/list-view/ (fonte)

# Exemplo: ( entrada --> saída )

# "ATTGC" --> "TAACG"
# "GTAT" --> "CATA"

def DNA_strand(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in dna)
