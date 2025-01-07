'''
Cada função é uma regra que recebe zero ou mais entradas e retornaa  saída correspondente.
No python definimos a funação com def
'''

def double(x):
    return x * 2

print(double(3))

#========================================================#

'''
As funções do python são de primeira classe, ou seja, podemos atribuí-las a variáveis
e inseri-las nas funçoes como argumentos.
'''

def apply_to_one(f):
    return f(1)                 #Eleva o número


my_double = double              #refere-se à função x já definida
x = apply_to_one(my_double)     #igual a 2

print(x)

#=========================================================#

'''
Os parâmetros da função também podem receber argumentos padrão, que devem ser especificados 
se você queiser obter um valor diferente do padrão.
'''

def my_print(message = "message default"):
    print(message)

my_print('Hello')
my_print()