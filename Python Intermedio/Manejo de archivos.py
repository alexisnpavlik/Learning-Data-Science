

#Sobre escribir un archivo con texto
archivo= open("archivo.txt","w")
frase="Estupendo dia para estudiar \n Los miercoles"
archivo.write(frase)
archivo.close()

#Abir y leer el contenido
archivo= open("archivo.txt","r")
leer=archivo.read()
archivo.close()
print(leer)


#Abrir y añadir texto
archivo= open("archivo.txt","a")
frase="\n y tambien los jueves"
archivo.write(frase)
archivo.close()



