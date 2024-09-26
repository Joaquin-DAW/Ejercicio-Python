#Crea una clase llamada CuentaBancaria con atributos titular y saldo. Agrega métodos para depositar y retirar dinero de la cuenta.  

class CuentaBancaria():
    
    def __init__(self, titular="", saldo=0.0):
        self.titular=titular
        self.saldo=saldo
    
    def depositar(self, saldo):
        self.saldo=self.saldo+saldo
        return self.saldo
        
    def retirar(self, saldo):
        self.saldo=self.saldo-saldo
        return self.saldo
    
persona1 = CuentaBancaria("Julian", 100.50)

persona1.depositar(30)

print(persona1.titular, persona1.saldo)

persona1.retirar(50)

print(persona1.titular, persona1.saldo)