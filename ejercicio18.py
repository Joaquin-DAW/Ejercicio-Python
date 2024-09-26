#Crea una clase base llamada Vehiculo con atributos marca y modelo, y un método informacion que imprima la información del vehículo. 
#Luego, crea clases derivadas como Coche y Bicicleta que hereden de Vehiculo y añadan atributos y métodos específicos de cada tipo de vehículo.

class Vehiculo():
    def __init__(self, marca="", modelo=""):
        self.marca=marca
        self.modelo=modelo
    
    def info(self):
        return print("La marca es "+self.marca+" con modelo "+self.modelo)
        
        
class Coche(Vehiculo):
    
    def __init__(self, marca="", modelo="", kilometraje=0.0):
        super().__init__(marca, modelo)
        self.kilometraje=kilometraje
        
    def info(self):
        return print("La marca es "+self.marca+" con modelo "+self.modelo+ " cuyo kilometraje es "+str(self.kilometraje)+" km")
    
    def cambiar_aceite(self):
        if self.kilometraje >= 10000:
            print("Es hora de cambiar el aceite.")
        else:
            print("Aún no es necesario cambiar el aceite.")
    

vehiculo1= Coche("Audi", "A3", 1000)

print(vehiculo1.info())