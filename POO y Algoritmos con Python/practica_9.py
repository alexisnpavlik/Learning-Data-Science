class Cuadrilatero:

    def __init__(self,lados):
        self.lados =lados
        self.suma_angulos=360

    def perimetro(self):
        return sum(self.lados)

class Cuadrado(Cuadrilatero):
    def __init__(self,lados):
        super().__init__(lados)


cuadrado_1=Cuadrado([1,1,2,2])

perimetro_1=cuadrado_1.perimetro()
print(perimetro_1)
print(cuadrado_1.suma_angulos)