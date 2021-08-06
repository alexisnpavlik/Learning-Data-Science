class Retangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura

class Cuadrado(Retangulo):
    def __init__(self,lado):
        super().__init__(lado,lado)
    #hacemos referencia a la superclase y decimos que 
    #tanto nuesta base como altura es igual a los lados

rectangulo_1=Retangulo(base=2,altura= 4)
print(rectangulo_1.area())

cuadrado_1=Cuadrado(lado=5)
print(cuadrado_1.area())
