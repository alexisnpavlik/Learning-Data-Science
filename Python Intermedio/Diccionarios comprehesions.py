def run():

    #Escribe un diccionario con los 100 primeros naturales
    #Key N° naturales, values N° al cuadrado
    dic={}
    for i in range(1,101):
        if i%3 !=0:
         dic[i]=i**3
    print(dic)

#Lo mismo pero en comprehesions
    dic={i: i**3 for i in range(1,101) if i%3 !=0}
    print(dic)
    

if __name__=='__main__':
    run()