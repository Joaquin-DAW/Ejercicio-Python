#Calcula el máximo común divisor (MCD) de dos números. 

num1 = int(input("Por favor, introduzca un número: "))

num2 = int(input("Por favor, introduzca otro número: "))

for i in range(1,num1):
    if (num1%i==0):
        divisor1=i
for j in range(1, num2):
    if(num2%j==0):
        divisor2=j
        if divisor1==divisor2:
            print(divisor2)