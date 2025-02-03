'''
Iterável:
Um objeto Python que pode ser submetido a um loop ou iterado em um loop. Exemplos de iteráveis incluem listas, conjuntos, tuplas, dicionários, strings etc. 

Iterador:
Um iterador é um objeto que pode ser iterado. Assim, os iteradores contêm um número contável de valores. 

Gerador:
Um tipo especial de função que não retorna um único valor: retorna um objeto iterador com uma sequência de valores.

'''



# instantiate a list object
list_instance = [1, 2, 3, 4]

# convert the list to an iterator
iterator = iter(list_instance)

# return items one at a time
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


def factors(n):
  for val in range(1, n+1):
      if n % val == 0:
          yield val #Gerador yeld. Gera itens em tempo real
         
factors_of_20 = factors(20)
print(next(factors_of_20))
