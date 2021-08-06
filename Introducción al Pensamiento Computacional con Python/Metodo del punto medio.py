objetivo=int(input("Escribe el numero que quieres saber la raiz: "))
epsilon = 0.1
#defino los extremos
ex_inferior = 0.0
ex_superior = objetivo
respuesta = (ex_superior + ex_inferior) / 2


#Si el valor abs del punto medio al cruadrado menos el objetivos, es menor que el epsilon
while abs(respuesta**2 - objetivo) >= epsilon and objetivo>0:
    print(f'extremo Superior={ex_inferior}, extremo superior={ex_superior}, respuesta={respuesta}')
    if respuesta**2>objetivo:
        ex_superior=respuesta
    elif respuesta**2<objetivo:
        ex_inferior=respuesta
    
    respuesta = (ex_superior + ex_inferior) / 2
        
    

print(f'La raiz cuadrada de {objetivo} es {respuesta}')