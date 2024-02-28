import datetime
import random

aparato = {}
orden = {}
tecnicos_disponibles = ["Juan", "María", "Carlos"]
seguir = True

def generar_numero_registro():
    return random.randint(10000, 99999)

def ingresar_detalles_aparato(aparato_nombre):
    descripcion = input("Descripción del aparato: ")
    falla = input("Falla del aparato: ")
    aparato[aparato_nombre] = {"Descripción": descripcion, "Falla": falla}

def mostrar_detalles_orden(tipo, detalles):
    print(f"Tipo de orden: {tipo}")
    for key, value in detalles.items():
        if key == "Cliente":
            print(f"{key}: {value}") 
        elif key == "Fecha de ingreso":
            print(f"{key}: {value.strftime('%d-%m-%Y')}")
            # Calcular el tiempo transcurrido desde la fecha de ingreso
            tiempo_transcurrido = datetime.datetime.now() - value
            print(f"Tiempo transcurrido desde ingreso: {tiempo_transcurrido.days} días")
        elif key == "Fecha de salida":
            print(f"{key}: {value.strftime('%d-%m-%Y')}")
        elif key == "Precio":
            print(f"{key}: L. {value}")
        elif key == "Técnico":
            print(f"{key}: {value}")
        elif key == "Aparato":
            print("Detalles del aparato:")
            for aparato_nombre, detalles_aparato in value.items():
                print(f"  Nombre: {aparato_nombre}")
                print(f"  Descripción: {detalles_aparato['Descripción']}")
                print(f"  Falla: {detalles_aparato['Falla']}")
        elif key == "Reparado":
            if value is None:
                print("Estado del aparato: Pendiente de reparación")
            elif value:
                print("Estado del aparato: Reparado")
            else:
                print("Estado del aparato: No reparado")
        elif key == "PorqueNoSeReparo":
            if value:
                print(f"Razón por la que no se reparó: {value}")
    print()

while seguir:
    print("-------Taller de reparaciones--------")
    print("----------Menú de opciones-----------")
    print("1. Ingresar detalles del aparato a reparar")
    print("2. Crear orden normal")
    print("3. Crear orden con garantía")
    print("4. Mostrar detalles de órdenes")
    print("5. Buscar orden por número de registro")
    print("6. Salir")
    opcion = int(input("Ingrese su opción: "))

    if opcion == 1:
        print("Seleccione un técnico disponible:")
        for idx, tecnico in enumerate(tecnicos_disponibles, start=1):
            print(f"{idx}. {tecnico}")
        tecnico_seleccionado = int(input("Ingrese el número correspondiente al técnico seleccionado: "))
        tecnico_elegido = tecnicos_disponibles[tecnico_seleccionado - 1]
        print("Ingrese el nombre del aparato que desea reparar")
        nombre = input("Nombre: ")
        ingresar_detalles_aparato(nombre)
        # Solicitar fecha de ingreso del aparato
        fecha_ingreso = datetime.datetime.strptime(input("Ingrese la fecha de ingreso del aparato (formato: dd-mm-yyyy): "), "%d-%m-%Y")
        
    elif opcion == 2:
        print("Usted ha elegido crear una orden normal")
        cliente = input("Nombre del cliente: ")
        # Solicitar fecha de salida y precio
        fecha_salida = datetime.datetime.strptime(input("Ingrese la fecha de salida del aparato (formato: dd-mm-yyyy): "), "%d-%m-%Y")
        precio = float(input("Ingrese el precio de la reparación: "))
        orden["Normal"] = {"Fecha de ingreso": fecha_ingreso, "Fecha de salida": fecha_salida, "Precio": precio, "Cliente": cliente, "Técnico": tecnico_elegido, "Aparato": aparato, "Reparado": True, "PorqueNoSeReparo": None}
        
    elif opcion == 3:
        print("Usted ha elegido crear una orden con garantía")
        referencia = input("Ingrese la referencia de garantía: ")
        cliente = input("Nombre del cliente: ")
        numero_registro = generar_numero_registro()
        orden["Garantia"] = {"Número de registro": numero_registro, "Fecha de ingreso": fecha_ingreso, "Referencia": referencia, "Cliente": cliente, "Técnico": tecnico_elegido, "Aparato": aparato, "Reparado": False, "PorqueNoSeReparo": "No tenía compostura"}
        print(f"Se ha generado el número de registro: {numero_registro}")
        
    elif opcion == 4:
        print("Detalles de las órdenes:")
        for tipo, detalles in orden.items():
            mostrar_detalles_orden(tipo, detalles)
        
    elif opcion == 5:
        print("Buscar orden por número de registro")
        numero_registro_buscar = int(input("Ingrese el número de registro de la orden: "))
        encontrado = False
        for tipo, detalles in orden.items():
            if detalles.get("Número de registro") == numero_registro_buscar:
                mostrar_detalles_orden(tipo, detalles)
                encontrado = True
                break
        if not encontrado:
            print("No se encontró ninguna orden con ese número de registro.")
        
    elif opcion == 6:
        seguir = False
        print("¡Hasta luego!")
        
    else:
        print("Opción inválida. Por favor, elija una opción válida.")
