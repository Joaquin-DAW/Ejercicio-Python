#Crea una clase base llamada Animal con un método hablar que imprima un mensaje genérico. Luego, crea dos clases derivadas, Perro y Gato, 
#que hereden de Animal y sobrescriban el método hablar para imprimir mensajes diferentes. 

class Animal():
    
    def __init__(self, onomatopeya=""):
        self.onomatopeya=onomatopeya
        
    def hablar(self):
        return self.onomatopeya
    
class Perro(Animal):
    
    def __init__(self):
        super().__init__("Guadu")
        
class Gato(Animal):
    
    def __init__(self):
        super().__init__("Miau")


animal1 = Perro()

print(animal1.hablar())

animal2 = Gato()

print(animal2.hablar())