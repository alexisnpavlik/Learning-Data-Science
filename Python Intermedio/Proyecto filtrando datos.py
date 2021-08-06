DATA=[
    {
        "name":"facundo",
        "age":72,
        "organization":"Platzi",
        "position":"Technical Coach",
        "languaje":"Python",
    },
    {
        "name":"Luisana",
        "age":33,
        "organization":"Globant",
        "position":"UX Desingner",
        "languaje":"Javascript",
    },
    {
        "name":"Hector",
        "age":17,
        "organization":"Platzi",
        "position":"Associate",
        "languaje":"Ruby",
    }

]
 
def run():
    #Guarda en all_python_devs, todos los nombre de trabajadores en el diccionario "DATA"
    #Solo si los trabajadadores diminan "Ruby"
    all_python_devs=[worker["name"] for worker in DATA if worker["languaje"]=="Ruby"]
    all_platzi_workers=[worker["name"] for worker in DATA if worker["organization"]=="Platzi"]

    for worker in all_platzi_workers:
        print(worker)


    #Filtramos a las personas mayores de edad
    adults=list(filter(lambda worker: worker["age"] >17,DATA))

    adults=list(map(lambda worker:worker["name"],adults))

    for worker in adults:
        print(worker)

    #Creamos una lista con todas las personas mayores
    old_people=list(map(lambda worker: worker | {"old":worker["age"]>17},DATA))
    for worker in old_people:
        print(worker)

if __name__=='__main__':
    run()