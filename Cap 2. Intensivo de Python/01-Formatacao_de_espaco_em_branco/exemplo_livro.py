'''
 o espaço em branco é ignorado quando aparece dentro de parênteses e colchetes, algo muito útil para 
 lidar com computação intermináveis.
'''


long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 
                           7 + 8)

print(long_winded_computation)


#==========================================================#

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

easier_to_read_list_of_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(list_of_lists)
print(easier_to_read_list_of_list)

#===========================================================#

'''
    Você também pode usar uma barra invertida para indicar que a instrução continua
    na próxima linha.
'''

two_plus_three = 2 + \
                 3

print(two_plus_three)