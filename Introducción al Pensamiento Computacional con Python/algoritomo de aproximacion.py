import os

os.system ("cls")
objetivo=int(input("Escribe el numero que quieres saber la raiz: "))
epselon=0.00001
arranque=0
paso=0.001

while abs(arranque**2-objetivo)>=epselon and objetivo>0:
    print(arranque)
    arranque=arranque+paso

print(f"La raiz cuadrada de {objetivo} es: {arranque}")