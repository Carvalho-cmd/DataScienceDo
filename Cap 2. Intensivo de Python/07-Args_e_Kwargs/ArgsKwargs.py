
# Exemplo de uso de função passando um parâmetro:

def  doubler(f): #Função que recebe função como pâmetro.
    def g(x):    #Retorna outra função, multiplicando por dois o resultado da função recebida.
        return 2 * f(x)
    return g

def f1(x):       #Criando função para passar em doubler.
    return x + 1

g = doubler(f1)  #Criando uma variável g que chama a função doubler, passando a função f1 como parametro e recebendo uma função como resultado.

print(g(2))      #g é do tipo função.


'''
O *args é usado para receber uma lista de argumentos de comprimento variável sem a palavra-chave (keyword) na função.

Aqui está um exemplo pra facilitar o entendimento:
'''

def função_com_argumentos_variaveis(arg, *args):
    print("Primeiro argumento:", arg)
    
    for argumento in args:
        print("Argumento de *args", argumento)

função_com_argumentos_variaveis('primeiro_arg', 'arg2', 'arg3', 'arg3')



'''
O **kwargs possibilita verificarmos os parâmetros nomeados da função, isto é, aqueles parâmetros que são passados com um nome!

Eles estarão disponíveis como um dicionário ({'chave': 'valor'}) dentro da função.
'''

def concatena (**kwargs):
    print(f'Valores recebidos: {kwargs}')
    resultado = ""

    for valor in kwargs.values():
        resultado += f'{valor} '
    return resultado

print(concatena(a="Python", b="Academy",  c="Rules!"))
print()
print(concatena(a="Python", b="é", c="na", d="Python", e="Academy!"))
