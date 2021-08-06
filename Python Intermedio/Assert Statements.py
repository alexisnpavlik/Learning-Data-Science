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

num=3
#Si no se cumple imprime en mensaje
assert len(" ") >0, "Esta vacia"

#ismeric() comprueba si el dato es un numero
assert num.ismeric(), "Debes ingresar un numero"