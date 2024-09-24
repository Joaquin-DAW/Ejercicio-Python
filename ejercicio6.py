#Verifica si un número es par o impar. 

num = int(input("Por favor, introduzca un número: "))

if (num%2==0):
    print("El número "+str(num)+" es par")
else:
    print("El número "+str(num)+" es impar")