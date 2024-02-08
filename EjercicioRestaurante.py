comidas = []

while True:
    print("\n--- Menú ---")
    print("1. Ingresar comida")
    print("2. Agregar ingredientes a una comida")
    print("3. Agregar receta a una comida")
    print("4. Ver listado de comidas")
    print("5. Ver detalles de una comida")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre_plato = input("Ingrese el nombre del plato: ")
        tipo_plato = input("Ingrese el tipo de plato (ensalada, carnes, hamburguesas, etc.): ")
        comidas.append({"nombre_plato": nombre_plato, "tipo_plato": tipo_plato, "ingredientes": [], "receta": []})
        print("Comida ingresada correctamente.")
    elif opcion == "2":
        if not comidas:
            print("No hay comidas ingresadas.")
        else:
            print("Listado de comidas:")
            for i, comida in enumerate(comidas, start=1):
                print(f"{i}. {comida['nombre_plato']}")
            num_comida = int(input("Seleccione el número de la comida a la que desea agregar ingredientes: ")) - 1
            nombre_ingrediente = input("Ingrese el nombre del ingrediente: ")
            cantidad = float(input("Ingrese la cantidad del ingrediente: "))
            unidad_medida = input("Ingrese la unidad de medida del ingrediente: ")
            costo_por_unidad = float(input("Ingrese el costo por unidad del ingrediente: "))
            comidas[num_comida]["ingredientes"].append({"nombre": nombre_ingrediente, "cantidad": cantidad, "unidad_medida": unidad_medida, "costo_por_unidad": costo_por_unidad})
            print("Ingredientes agregados correctamente.")
    elif opcion == "3":
        if not comidas:
            print("No hay comidas ingresadas.")
        else:
            print("Listado de comidas:")
            for i, comida in enumerate(comidas, start=1):
                print(f"{i}. {comida['nombre_plato']}")
            num_comida = int(input("Seleccione el número de la comida a la que desea agregar receta: ")) - 1
            print("Ingrese los pasos de la receta (ingrese 'fin' para terminar):")
            pasos_receta = []
            paso = ""
            while paso.lower() != "fin":
                paso = input("Paso: ")
                if paso.lower() != "fin":
                    pasos_receta.append(paso)
            comidas[num_comida]["receta"] = pasos_receta
            print("Receta agregada correctamente.")
    elif opcion == "4":
        if not comidas:
            print("No hay comidas ingresadas.")
        else:
            print("Listado de comidas:")
            for i, comida in enumerate(comidas, start=1):
                print(f"{i}. Nombre: {comida['nombre_plato']}, Tipo: {comida['tipo_plato']}")
    elif opcion == "5":
        if not comidas:
            print("No hay comidas ingresadas.")
        else:
            print("Listado de comidas:")
            for i, comida in enumerate(comidas, start=1):
                print(f"{i}. {comida['nombre_plato']}")
            num_comida = int(input("Seleccione el número de la comida que desea ver: ")) - 1
            print("Detalles de la comida:")
            print(f"Nombre del plato: {comidas[num_comida]['nombre_plato']}")
            print(f"Tipo de plato: {comidas[num_comida]['tipo_plato']}")
            print("Ingredientes:")
            for ingrediente in comidas[num_comida]["ingredientes"]:
                print(f"- {ingrediente['nombre']}: {ingrediente['cantidad']} {ingrediente['unidad_medida']}, Costo por unidad: {ingrediente['costo_por_unidad']}")
            print("Receta:")
            for i, paso in enumerate(comidas[num_comida]["receta"], start=1):
                print(f"{i}. {paso}")
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
