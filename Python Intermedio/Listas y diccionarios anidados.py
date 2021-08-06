def run():
    list=[1,"hello",True]
    dic={"firtname": "Alexis", "lastname": "Medina"}

#lista de diccionario
    super_list=[
        {"firtname": "Alexis", "lastname": "Medina"},
        {"firtname": "Miguel", "lastname": "Pepe"},
        {"firtname": "Pepe", "lastname": "Martinez"}     
    ]
#diccionario de listas
    super_dic={
        "natura_nums":[1,2,3,4,50],
        "integer":[-3,-5,-1,0]
    }

#recorrer items de un diccionario
    for key, value in super_dic.items():
        print(key,"-",value)

#recorrer items de una lista
    # for key, value in super_list:
    #     print(key,"-",value)


if __name__=='__main__':
    run()