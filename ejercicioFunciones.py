def agregar_elemento(objeto, mensaje):
    elemento = input(mensaje)
    if isinstance(objeto, list):
        objeto.append(elemento)
    elif isinstance(objeto, dict):
        objeto[elemento] = []  
    else:
        print("Tipo de objeto no válido. Se esperaba una lista o un diccionario.")

def leer_elementos(lista, nombre_lista):
    print(f"Mostrar {nombre_lista}: ")
    for elemento in lista:
        print("- " + str(elemento))

def actualizar_elemento(diccionario, mensaje):
    elemento_actual = input("Ingrese el nombre del elemento a actualizar: ")
    print("Elemento actual:", elemento_actual)
    print("Diccionario antes de actualizar:", diccionario)
    if elemento_actual in diccionario:
        nuevo_valor = input(mensaje)
        indice = list(diccionario.keys()).index(elemento_actual)
        claves = list(diccionario.keys())
        claves[indice] = nuevo_valor
        nuevo_diccionario = {nueva_clave: diccionario[clave] for nueva_clave, clave in zip(claves, diccionario)}
        print("Diccionario después de actualizar:", nuevo_diccionario)
        print("Elemento actualizado")
        return nuevo_diccionario
    else:
        print("El elemento especificado no existe.")
        return diccionario



def borrar_elemento(diccionario, mensaje):
    elemento_borrar = input(mensaje)
    if elemento_borrar in diccionario:
        del diccionario[elemento_borrar]
        print("Elemento borrado")
    else:
        print("El elemento especificado no existe.")

def agregar_clases_a_carrera(carreras):
    carrera_destino = input("Ingrese el nombre de la carrera para agregar las clases: ")
    if carrera_destino in carreras:
        while True:
            clases = carreras[carrera_destino]
            opcion2 = int(input("-------------Menú de clases-------------\n"
                                "1. Agregar clase\n"
                                "2. Leer clases\n"
                                "3. Actualizar clase\n"
                                "4. Borrar clase\n"
                                "5. Salir\n"
                                "Ingrese su opción: "))

            if opcion2 == 1:
                agregar_elemento(clases, "Ingrese el nombre de la clase: ")
                print("Clase agregada:", clases[-1])
            elif opcion2 == 2:
                leer_elementos(clases, "clases")
            elif opcion2 == 3:
                actualizar_elemento(carreras[carrera_destino], "Ingrese nuevo nombre de la clase: ")
            elif opcion2 == 4:
                borrar_elemento(carreras[carrera_destino], "Ingrese nombre de la clase a borrar: ")
            elif opcion2 == 5:
                carreras[carrera_destino] = clases
                print(f"Carrera: {carrera_destino}, clases agregadas: {', '.join(clases)}")
                break
            else:
                print("Opción inválida.")
    else:
        print("La carrera especificada no existe en el diccionario de carreras.")

def main():
    carreras = {} 

    while True:
        opcion = int(input("++++++++++++++++ Menu ++++++++++++++++++\n"
                           "1. Gestionar carreras\n"
                           "2. Agregar clases a carrera\n"
                           "3. Salir\n"
                           "Ingrese su opción: "))

        if opcion == 1:
            while True:
                opcion_carrera = int(input("-------------Menú de Carreras-------------\n"
                                           "1. Agregar carrera\n"
                                           "2. Leer carreras\n"
                                           "3. Actualizar carrera\n"
                                           "4. Borrar carrera\n"
                                           "5. Salir\n"
                                           "Ingrese su opción: "))

                if opcion_carrera == 1:
                    agregar_elemento(carreras, "Ingrese el nombre de la carrera: ")
                    print("Carreras agregadas:")
                    leer_elementos(list(carreras.keys()), "carreras")
                elif opcion_carrera == 2:
                    leer_elementos(list(carreras.keys()), "carreras")
                elif opcion_carrera == 3:
                    actualizar_elemento(carreras, "Ingrese nuevo nombre de la carrera: ")

                elif opcion_carrera == 4:
                    borrar_elemento(carreras, "Ingrese nombre de la carrera a borrar: ")
                elif opcion_carrera == 5:
                    break
                else:
                    print("Opción inválida.")

        elif opcion == 2:
            agregar_clases_a_carrera(carreras)

        elif opcion == 3:
            print("Hasta la próxima.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
