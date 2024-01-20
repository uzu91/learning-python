'''crear una calculadora que reciba dos valores 
por consola, y realice las operaciones aritméticas básicas'''

import os 

os.system('clear')

print("Digite el primer valor: ")
n1 = int(input())
n2 = int(input("Digite el segundo valor: \n"))
suma = n1 + n2
print("suma: ", suma)