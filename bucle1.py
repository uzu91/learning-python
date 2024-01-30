'''
Bucle: Ciclo, Loop, repetir una acción N veces, iteraciones (Cantidad de ejecuciones.)
Contadores (cuenta o incrementa)
Acumuladores (acumulación de valores, sumar valores)
Contar valores es diferente de sumar valores 
'''

# Función Bucle para imprimir los números del 1 al 10 en pantalla
def list_numbers():
    #Bucle que imprime lista de números por pantalla
    i = 1
    while i <= 100:
        print(i)
        i+=1 #i = i + 1

    print("i:", i) #101

def list_numbers2():
    #Bucle que imprime lista de números por pantalla (1 al 10)
    i = 1
    status = True
    while status: #while status == True
        if i == 11:
            break 
        print(i)
        i+=1 #i = i + 1

    print("i:", i) #101

def list_numbers3():
    #Bucle que imprime lista de números por pantalla (1 al 10)
    i = 1
    status = True
    while status: #while status == True 
        print(i)
        i+=1 #i = i + 1
        if i > 10 : # i == 11
            status = False

    print("i:", i) #11

def list_numbers4():
    #Bucle que imprime lista de números por pantalla (1 al 10)
    i = 1
    status = False
    while not status: #while status != False 
        print(i)
        i+=1 #i = i + 1
        if i > 10 : # i == 11
            status = True

    print("i:", i) #11

#list_numbers()
#ist_numbers2()
#list_numbers3()
list_numbers4()    