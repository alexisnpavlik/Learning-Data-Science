class Prueba:
    def __init__(self):
        self.__Privado="Soy privado"

    def setPrivado(self,valor):
        self.__Privado = valor
    
    def ss(self):
        return self.__Privado
    
obj_1=Prueba()

#Modifico lo privado
(obj_1.setPrivado("Tengo un nuevo valor"))
print (obj_1.ss())

#cambiando set y get?