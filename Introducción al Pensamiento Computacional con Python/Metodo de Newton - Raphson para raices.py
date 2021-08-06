import sympy as sp 

def derivada(y):
    x = sp.Symbol('x') 
    return sp.diff(y,x)

# def metodo_de_newton():
#     funcion_en_rn=y.replace(x,rn)
#     y_derivada = derivada(y)
#     derivada_funcion_en_rn=y_derivada.replace(x,rn)



def run():
    y=input("Ingresa la funcion: ")
    #rn=float(input("Ingresa el valor de arranque (Rn): "))
    y_derivada = derivada(y)
    print(y_derivada)
    print(type(y_derivada))


if __name__=='__main__':
    run()