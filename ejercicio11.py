#Crea una clase llamada Persona con atributos nombre y edad. Luego, crea un objeto de tipo Persona e imprime sus atributos.

class Persona():
    
    def __init__(self, nombre="", edad=0):
        self.nombre=nombre
        self.edad=edad
        
persona1 = Persona("Juan", 25)
persona2 = Persona("Alba", 27)

print(persona1.nombre, persona1.edad)
print(persona2.nombre, persona2.edad)