#Calcula el máximo común divisor (MCD) de dos números. 

num1 = int(input("Por favor, introduzca un número: "))

num2 = int(input("Por favor, introduzca otro número: "))

if (num1 > num2):
    menor=num2
else:
    menor=num1
    
for i in range(1, menor+1):
    if num1%i==0 and num2%i==0:
        mcd=i
        
print(mcd)