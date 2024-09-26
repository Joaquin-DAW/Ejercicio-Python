#Crea una clase base llamada FiguraGeometrica con atributos ancho y altura, y un método area que calcule el área de la figura. 
#Luego, crea clases derivadas como Rectangulo y Triangulo que hereden de FiguraGeometrica y sobrescriban el método area para calcular el área 
#específica de cada figura.

class FiguraGeometrica():
    def __init__(self, ancho=0.0, altura=0.0):
        self.ancho=ancho
        self.altura=altura
    
    def area(self):
        return 0.0
        
        
class Rectangulo(FiguraGeometrica):
    
    def area(self):
        return self.ancho*self.altura


class Triangulo(FiguraGeometrica):
    
    def area(self):
        return (self.ancho*self.altura)/2
    

figura1= Rectangulo(3, 6)
figura2= Triangulo (5,7)

print(figura1.area())

print(figura2.area())