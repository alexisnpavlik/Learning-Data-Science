
numers_cuadrado=[]

def run():
    numers_cuadrado=[]
    for x in range(1,101):
        value=x**2
        if value%3!=0:
            numers_cuadrado.append(value)
    print(numers_cuadrado)

if __name__=='__main__':
    run()