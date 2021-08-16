# def repite_palabras():

#     def repite(n):
#         print("hola"*n)
    
#     return repite

# saluda=repite_palabras()

# print(saluda(5))

#Otra forma

def make_repeter(n):

    def repeter(string):
        assert type(string)==str, "Solo puedes escribir string"
        return n*string
    
    return repeter

multi_5=make_repeter(5)

print(multi_5("holas "))