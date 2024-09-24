#Calcula el factorial de un número.

num = int(input("Por favor, introduzca un número: "))

factorial=1
i=1

while (i <= num):
    factorial = factorial * i
    i = i + 1

print("El facotiral del número "+str(num)+" es "+str(factorial))