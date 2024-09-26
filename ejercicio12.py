#Crea una clase llamada Rectangulo con atributos ancho y altura. Agrega un método para calcular el área del rectángulo y otro para calcular su perímetro. 

class Rectangulo():
    
    def __init__(self,ancho=0, alto=0):
        self.ancho=ancho
        self.alto=alto
    
    def area(self):
        return self.ancho*self.alto
    
    def perimetro(self):
        return 2*self.ancho+2*self.alto
    
rectangulo1 = Rectangulo(10,8)

print("El área del rectángulo es "+str(rectangulo1.area()))
print("El perímetro del rectángulo es "+str(rectangulo1.perimetro()))