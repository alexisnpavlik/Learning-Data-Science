#Clase, su primera letra mayuscula
class Lapiz:
#Declaramos sus atributos
    color="amarillo"
    contiene_grafito=True
    Contiene_borrador=False

#Metodos
    def dibujar (self):
        print("El lapiz esta dibujando")

Lapiz_generico=Lapiz()
print(Lapiz_generico.contiene_grafito)

print(Lapiz_generico.dibujar())
