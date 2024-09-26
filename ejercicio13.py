#Crea una clase llamada Estudiante con atributos nombre, edad y curso. Crea varios objetos de tipo Estudiante y almacénalos en una lista. 
#Luego, itera sobre la lista e imprime la información de cada estudiante.  

class Estudiante():
    
    def __init__(self, nombre="", edad=0, curso=""):
        self.nombre=nombre
        self.edad=edad
        self.curso=curso

estudiante1=Estudiante("Pablo", 27, "2ºASIR")
estudiante2=Estudiante("Laura", 20, "1ºTSAF")
estudiante3=Estudiante("Alex", 23, "2ºDAW")

ListaEstudiantes = [estudiante1, estudiante2, estudiante3]

for i in ListaEstudiantes:
    print(i.nombre, i.edad, i.curso)