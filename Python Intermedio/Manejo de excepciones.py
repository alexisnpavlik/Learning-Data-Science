
#Comprueba si una cadena es un palidromo
#No permite el ingreso de cadenas vacias o numeros
def palindrome(string):
    try:
        if len(string)==0:
            raise ValueError("No ingresaste ningun valor") 
        return string==string[::-1]
    except ValueError as ve:
        print(ve)
        return False

string=input("Ingresa ")
try:
    print(palindrome(string))
except TypeError:
    print("Solo se puede ingresar Str")


try:
    f= open("archibo.txt")
finally:
    f.close()

