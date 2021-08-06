#construya un algoritmo capaz de encontrar todas las cifras de tres digitos
#que cumplan con la condicion de que la suma d elos cubos de sus digitos
#sea igual al numero que la cifra representa.
#ejemplo: 153       1**3+5**3+3**3=1+125+27=153

def probador_cubos():
    lista=[]
    for i in range(100,1000):
        n=str(i)
        primer_num=int(n[0])
        segundo_num=int(n[1])
        tercer_num=int(n[1])

        if ((primer_num**3)+(segundo_num**3)+(tercer_num**3))==i:
            lista=lista.append(i)
    print(lista)



def run():
    probador_cubos()

if __name__=='__main__':
    run()