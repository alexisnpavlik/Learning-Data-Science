class Persona:
    def __init__(self,nombre):
        self.nombre = nombre
    
    def avanza(self):
        print("Ando caminando")

class Ciclista(Persona):
    def __init__(self,nombre):
        super().__init__(nombre)

    def avanza(self):
        print("Ando pedaleando")

persona_1=Persona("alex")
persona_1.avanza()

ciclista_1=Ciclista("Roberto")
ciclista_1.avanza()




