'''
Provavelmente a estrutura de dados mais fundamental do pythoné a lista.
uma lista  é apenas uma coleção ordenada (Parecida com o array das outras linguagens, mais com funcionalidaddes adicionais)
'''


integer_list = [1,2,3]

heterogeneous_list = ['String', 0.1, True]

list_of_lists = [integer_list, heterogeneous_list, []]

#print(integer_list)

#print(heterogeneous_list)

#print(type(heterogeneous_list[0])) #Acessando o tipo de um valor específigo da lista
#print(type(heterogeneous_list[1]))
#print(type(heterogeneous_list[2]))


#print(list_of_lists)

#print(list_of_lists[1][2]) #Acessando valor de uma lista dentro de outra.



#============================================================================================#


list_length = len(integer_list) #Quantidade exata de itens em uma lista.

#print(list_length)

list_sum = sum(integer_list) #Soma dos valores dentro de uma lista.

#print(list_sum)

# teste_soma_valores_diferentes = sum(heterogeneous_list) #A soma não funciona se na lista tiver ítens com tipos diferentes.


#print(integer_list[-1]) #'pythonic' para o último elemento da lista.


#===========================================================================================#

'''
Você também pode usar os colchetes para fatiar as listas.
A fatia i:j contém todos os elementos de i(incluído) a j(não incluido). Se o início da fatia não  for indicado,
ela começará no início da lista; se o final da fatia não for idicado, ela terminará no final da lista:
'''

x = [0,1,2,3,4,5,6,7,8,9]

first_three = x[:3]
three_to_end = x[3:]
one_to_four = x[1:5]
last_three = x[-3:]
without_first_and_last = x[1:-1]
copy_of_x = x[:]

'''
A fatia pode receber um terceiro argumento para indicar seu stride(passo), que pode ser negativo
'''

every_third = x[::3] #Traz tudo com o terceiro argumento setando os passos de 3 em 3.
five_to_three = x[5:2:-1]

#print(every_third)
#print(five_to_three)

#==============================================================================================#

''''
O python dispõe de um operador 'in' para verificar a associação à lista
'''

#print(1 in [1,2,3])
#print(0 in x)
#print(0 in [1,2,3])
