'''script title: Basic calculator v1
Developer name: Andrés Pérez
Date: 18-01-2024'''

'''Description:
This calculator let you get the result of 4 
basic math operations from two numbers'''

#INPUTS (two static variables)
num1 = 20
num2 = 5

#PROCESS
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

#OUTPUTS
print("------ BASIC CALC V1 ------")
print("Number 1:", num1)
print("Number 2:", num2)
print("The addition is:", add)
print("The subtration is:", sub)
print("The multiplication is:", mul, type(mul))
print("The division is:", div, type(div))