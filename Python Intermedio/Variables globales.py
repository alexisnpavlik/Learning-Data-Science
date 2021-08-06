def cajanegra():
    global c
    c = 3
    print('La variable c dentro de la función tiene por valor', c)

c = 5
cajanegra()
print('La variable c fuera de la función tiene por valor', c)