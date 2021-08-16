def main():
    a=1

    def nested(): #Esto es un closure (funcuon anidada) recuerda la variable auterior aunque sea eliminada la funcion
        #
        print(a)
    
    return nested()

my_funt=main()
my_funt

