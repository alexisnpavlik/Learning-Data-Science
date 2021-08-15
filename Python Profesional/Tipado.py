#Definimos el tipo de datos
x: int =5
z= str ="hola"
c: bool = True

#Definimos el typado y el output
def suma(a:int , b:int) -> int: 
    return a+b

print (suma(3,2))


from typing import dict , list

#Listas
numeros_positivos:list[int] = [1,2,3,4,5]
#Diccionarios
usuarios: dict[str , int] = {
    'argentina':1,
    'paraguay':3,
    'brasil':4}
#tuplas
from typing import tuple

number: tuple[int,float,str]=[1,0.5,"s"]

#Estructuras complejas

#Lista de diccionarios
pobracion: list[dict[str , int]] = [
    {'argentina':1,
    'people':52878},
     {'paraguay':3,
    'people':55958}, 
    {'brasil':4,
    'people':52878}]

#Listas de diccionarios con tuplas con Keys
coordenadas: list[dict[str, tuple[int,int]]]=[
    {'coor_1': (45,25),
    'coor_2': (85,55)},

    {'coor_3': (25,25),
    'coor_4': (85,55)},
]
