#Crie uma função chamada _ifque recebe 3 argumentos: um valor boole 2 funções (que não recebem nenhum parâmetro): func1efunc2

#Quando boolfor verdade, func1deve ser chamado, caso contrário, chame o func2.

#Exemplo:
#def truthy(): 
#  print("True")
  
#def falsey(): 
#  print("False")
  
#_if(True, truthy, falsey)
# prints 'True' to the console


def _if(bool, func1, func2):
    if bool:
        func1()
    else:
        func2()