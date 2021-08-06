#Esto evaluara si un numero es divisor de 3
def multiplo3(numero):
    if numero%3==0:
        return True

lista_numero=[1,2,3,4,5,6,7,8,9]

#Esta funcion recibe como parametros "una funcion" y  una "lista"
lista_multiplos=filter(multiplo3,lista_numero)

#La funcion arroja un objeto que debemos tranformar a lista
print(list(lista_multiplos))

#Esta es la version simplificada con lambda
print(list(filter(lambda numero:numero%3==0, lista_numero)))

#Esta función trabaja de una forma muy similar a filter()
#Con la diferencia que en lugar de aplicar una condición a un elemento de una lista o secuencia
#Aplica una función sobre todos los elementos
def doblar(numero):
    return numero*2

numeros = [2, 5, 10, 23, 50, 33]

print(list(map(doblar, numeros)))

#Fomato lambda
print(list( map(lambda x: x*2, numeros)))
