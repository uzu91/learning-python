import os 
os.system("clear")

#def calculator(n1, n2, opc)
def calculator(x, y, z):
    if z == '1':
        return x + y
    elif z == '2':
        return x - y
    elif z == '3':
        return x * y
    elif z == '4':
        if y == 0:
            return 'No es posible dividir entre cero (0)'
        else:
            return x / y
    elif z == '5':
        if y == 0:
            print('Suma = ', x + y, 'Resta = ', x - y, 'Muliplicación: = ', x * y, 'División = No es posible dividir entre cero (0)')
        else:
            print('Suma = ', x + y, 'Resta = ', x - y, 'Muliplicación: = ', x * y, 'División = ', x / y)
    else:
        return '::: Fail, invalid option :::'
    
n1 = float(input("Digite primer valor: "))
n2 = float(input("Digite segundo valor: "))

print("::::: MENÚ CALCULADORA :::::")
print("[1]. Sumar")
print("[2]. Restar")
print("[3]. Multiplicar")
print("[4]. Dividir")
print("[5]. Todas")
opc = input("Digite una opcion del menú: ")

ans = calculator(n1, n2, opc) 
if ans != None:
    print("Resultado: ", ans)