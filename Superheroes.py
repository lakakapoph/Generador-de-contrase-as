superheroes = ["Spiderman", "Superman", "Wolverine"]

while True:

    eleccion = int(input("Eliminar superheroe(1), Agregar superheroe(2), Imprimir lista(3), Cerrar programa(4)"))

    if eleccion == 1:
        elim = input("¿que numero de superheroe desea eliminar? ")

        superheroes.remove(elim)

        print("Se ha eliminado ",elim)

    elif eleccion == 2:
        agregar = input("¿que superheroe desea agregar?")

        superheroes.append(agregar)

        print(superheroes)

    elif eleccion == 3:

        print(superheroes)

    elif eleccion == 4:
        print("Programa finalizado con exito")
        
        break
