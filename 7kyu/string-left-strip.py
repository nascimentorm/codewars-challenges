# Dada uma string de destino gravável e uma string de caracteres somente leitura, remova no local todos os caracteres iniciais da string que estão presentes na string de caracteres.

# Os caracteres iniciais formam um prefixo da string de destino. Esse prefixo tem comprimento n , onde n é o número de caracteres do início da string até o primeiro caractere da string que não está contido na string de caracteres somente leitura.

# Caso a sequência de caracteres somente leitura seja NULL, remova o espaço em branco inicial na sequência de destino.

# Caso a sequência de caracteres somente leitura esteja vazia, não remova nada.

# Exemplo:

# char s[] = "!!!!###@hello";
# const char *chars = "!#@";
# if (stringLeftStrip(s, chars)) { // returns "hello"
#   (void)puts(s);
# }
# Adendo: A string de destino sempre será definida (não NULL). No entanto, pode estar vazia.

# Certifique-se de fazer a remoção no local. Não há necessidade de este kata alocar ou desalocar memória.

# Lembre-se de que você só precisa remover os caracteres iniciais, ou seja, os caracteres fornecidos const char *chars = " "e char s[] = "Hello, world!", nada deve ser removido e a string sretornada intacta. 
# Isso ocorre porque o primeiro caractere que não está contido no charsé o primeiro caractere da string de destino.


def string_left_strip(target: str, chars: str | None) -> str:
    if target is None:
        return None

    if chars is None:
        chars = ' '
    elif chars == '':
        return target

    i = 0
    while i < len(target) and target[i] in chars:
        i += 1

    return target[i:]
