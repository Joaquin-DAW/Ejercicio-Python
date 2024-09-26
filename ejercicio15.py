#Crea una clase llamada Coche con atributos marca y modelo. Crea un método que imprima la información del coche en un formato legible. 

class Coche():
    
    def __init__(self, marca="", modelo=""):
        self.marca=marca
        self.modelo=modelo
    
    def infoCoche(self):
        return print("El coche es de la marca "+self.marca+" modelo "+self.modelo)
    

coche1=Coche("Audi", "A3")

coche1.infoCoche()