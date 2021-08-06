class Cliente:
    def __init__(self):
        self.__codigo=5474

    def getcodigo(self):
        return self.__codigo
    
    def __cuenta(self):
        print ("Monto")

persona=Cliente()

"""si quiero imprimir una variable privada"""

#Con una estructura especial
print(persona._Cliente__codigo) 

#Con el metogo get
print(persona.getcodigo())

#Para acceder a un metodo privado
persona._Cliente__cuenta()
