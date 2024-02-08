
carreras = {}
clases = []
seguir = True
continuar = True

while seguir:
    print(carreras)
    print("++++++++++++++++ Menu ++++++++++++++++++")
    print("1. Crear carrera")
    print("2. Leer carrera")
    print("3. Actualizar carrera")
    print("4. Borrar carrera")
    print("5. Salir")
    opcion = int(input("Ingrese su opcion: "))
    print("----------------------------------")

    if opcion == 1:
        print("Ingresar carrera")
        nombre = input("Nombre: ")
        carreras[nombre] = {}
    elif opcion == 2:
        print("Leer (mostrar) carreras")
        for carrera in carreras:
            print("- Nombre: " + carrera)
    elif opcion == 3:
        carreraActualizar = input("Ingrese nombre de la carrera: ")
        nuevoValor = input("Ingrese nuevo nombre de la carrera: ")
        carreras[nuevoValor] = carreras.pop(carreraActualizar)
    elif opcion == 4:
        carreraBorrar = input("Ingrese nombre de la carrera: ")
        if carreraBorrar in carreras:
            del carreras[carreraBorrar]
            print("Carrera borrada")
        else:
            print("La carrera no existe")
    elif opcion == 5:
        print("Hasta la proxima")
        seguir = False
    print("----------------------------------")

    print("Desea agregar una clase?")
    respuesta = input("Respuesta: ")
    if respuesta.lower() == "si":
        while continuar:
            print(clases)
            print("-------------Menú de clases-------------")
            print("1. Crear clase")
            print("2. Leer clase")
            print("3. Actualizar clase")
            print("4. Borrar clase")
            print("5. salir clase")
            opcion2 = int(input("Ingrese su opcion: "))
            print("----------------------------------")

            if opcion2 == 1:
                print("Ingrese el nombre de la clase: ")
                nombre2 = input("Nombre de la clase: ")
                clases.append(nombre2)
            elif opcion2 == 2:
                print("Mostrar clases: ")
                for clase in clases:
                    print("- Nombre de la clase: " + clase)
            elif opcion2 == 3:
                claseActualizar = input("Ingrese nombre de la clase: ")
                nuevoValor = input("Ingrese nuevo nombre de la clase: ")
                if claseActualizar in clases:
                    index = clases.index(claseActualizar)
                    clases[index] = nuevoValor
            elif opcion2 == 4:
                claseBorrar = input("Ingrese nombre de la clase: ")
                if claseBorrar in clases:
                    clases.remove(claseBorrar)
                    print("Clase borrada")
                else:
                    print("La clase no existe")
            elif opcion2 == 5:
                print("Hasta la proxima")
                continuar = False
            print("----------------------------------")

       
        carrera_destino = input("Ingrese el nombre de la carrera para agregar las clases: ")
        if carrera_destino in carreras:
            carreras[carrera_destino]['clases'] = clases
            print("Clases agregadas a la carrera", carrera_destino)
        else:
            print("La carrera especificada no existe en el diccionario de carreras.")