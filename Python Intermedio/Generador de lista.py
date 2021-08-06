#Leer numeros de archivo y hacer una lista
def read():
    archivo=open("archivo.txt","r",encoding="utf-8")
    texto=archivo.read()
    archivo.close()
    return texto
   
def list_creator(texto):
    lista=[]
    lista=texto.split()
    lista_final=[]
    for x in lista:
        lista_final.append(int(x))
    print(lista_final)

def run():
    list_creator(read())

if __name__=='__main__':
    run()