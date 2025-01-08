'''
Quando algo dá errado, o python gera uma excecao.
Para tratar uma excecao você pode utilizar o try except
'''

try:
    print(0/0)
except ZeroDivisionError:
    print('cannot divide by zero')

#Também funciona dessa forma
try:
    print(0/0)
except:
    print('cannot divide by zero')