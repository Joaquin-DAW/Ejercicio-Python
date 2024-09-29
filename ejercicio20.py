#Crea una clase base llamada Empleado con atributos nombre y salario, y un método calcular_salario_anual que calcule el salario anual del empleado. 
#Luego, crea clases derivadas como Gerente y Programador que hereden de Empleado y añadan atributos y métodos específicos de cada tipo de empleado.

class Empleado():
    def __init__(self, nombre="", salario=0):
        self.nombre=nombre
        self.salario=salario
    
    def calcular_salario_anual(self):
        return print("El salario anual es de "+str(self.salario*12))
    
class Gerente(Empleado):
    
    def __init__(self, nombre="", salario=0, departamento=""):
        super().__init__(nombre, salario)
        self.departamento=departamento
        
    def info(self):
        return print("El empleado "+self.nombre+" con salario "+str(self.salario)+ " es un gerente del departamento de "+self.departamento)
    
    
class Programador(Empleado):
    def __init__(self, nombre="", salario=0, lenguajes=""):
        super().__init__(nombre, salario)
        self.lenguajes=lenguajes
        
    def info(self):
        return print("El empleado "+self.nombre+" con salario "+str(self.salario)+ " tiene un conocimiento sobre del siguiente lenguaje: "+self.lenguajes)
    
    
empleado1= Gerente("Jorge", 1350, "Informática")

empleado1.info()
empleado1.calcular_salario_anual()

empleado2= Programador("Laura", 1200, "Python")

empleado2.info()
empleado2.calcular_salario_anual()