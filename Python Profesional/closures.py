#Esto es un closure (funcion anidada) 
def main():
    a=1

    def nested(): 
#Recuerda la variable auterior
        print(a)
    
    return nested()

my_funt=main()
my_funt

