#Crea una clase base llamada InstrumentoMusical con un método tocar que imprima un mensaje genérico. Luego, crea clases derivadas como 
#Piano y Guitarra que hereden de InstrumentoMusical y sobrescriban el método tocar para imprimir mensajes diferentes.

class InstrumentoMusical():
    def __init__(self, musica="*musica*"):
        self.musica=musica
    
    def tocar(self):
        return self.musica
        
        
class Piano(InstrumentoMusical):
    
    def __init__(self):
        super().__init__("♩♫♪♬♪")
        
class Guitarra(InstrumentoMusical):
    
    def __init__(self):
        super().__init__("wawawawawawa")
        

instrumento1=Piano()
print ("Voy a tocar el piano: "+instrumento1.tocar())


instrumento2=Guitarra()
print ("Voy a tocar la guitarra: "+instrumento2.tocar())