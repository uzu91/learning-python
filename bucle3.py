import os
import random

os.system('clear')

def number_generator(cant):
    i = 0
    pares = 0
    impares = 0
    positivos = 0
    negativos = 0
    sum_pos = 0
    sum_neg = 0

    while i < cant:
        num = random.randint(-10,10)
        print(num)

        if num %2 == 0:
            pares = pares + 1
        else:
            impares +=1

        if num > 0: 
            positivos = positivos + 1
            sum_pos = sum_pos + num
        else:
            negativos +=1
            sum_neg += num

        i += 1
    
    print(f"Total números generados: {cant}")
    print(f"Total pares generados: {pares}")
    print(f"Total impares generados: {impares}")
    print(f"Total positivos generados: {positivos}")
    print(f"Total negativos generados: {negativos}")
    print(f"Suma positivos generados: {sum_pos}")
    print(f"Suma negativos generados: {sum_neg}")

cant_num = int(input("Digite la cantidad de números que desea generar: "))
number_generator(cant_num)