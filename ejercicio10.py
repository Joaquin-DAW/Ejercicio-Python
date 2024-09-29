#Crea una lista de números y calcula su promedio. 

long = int(input("Por favor, introduzca la longitud de la lista: "))

lista = []

for i in range(1, long+1):
    numeros = int(input("Por favor, introduzca su "+str(i)+"º número: "))
    lista.append(numeros)

promedio = sum(lista) /len(lista)

print(promedio)