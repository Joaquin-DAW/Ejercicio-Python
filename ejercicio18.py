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
        return print("La marca del coche es "+self.marca+" con modelo "+self.modelo+ " cuyo kilometraje es de "+str(self.kilometraje)+" km")
    
    def cambiar_aceite(self):
        if self.kilometraje >= 10000:
            print("Es hora de cambiar el aceite.")
        else:
            print("Aún no es necesario cambiar el aceite.")
    
class Bicicleta(Vehiculo):
    def __init__(self, marca="", modelo="", tipo="", distancia_recorrida=0):
        super().__init__(marca, modelo)
        self.tipo=tipo
        self.distancia_recorrida=distancia_recorrida
        
    def info(self):
        return print("La marca de la bicicleta es "+self.marca+" con modelo "+self.modelo+ " es una bici de "+self.tipo+" y tiene "+str(self.distancia_recorrida)+" km")
    
    def revisar_ruedas(self):
        if self.distancia_recorrida >= 100:
            print("Es necesario revisar las ruedas")
        else:
            print("Las ruedas están en buen estado")
    
    
vehiculo1= Coche("Audi", "A3", 15000)

vehiculo1.info()
vehiculo1.cambiar_aceite()


vehiculo2= Bicicleta("Scott", "Foil", "Montaña", 150)

vehiculo2.info()
vehiculo2.revisar_ruedas()