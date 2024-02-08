mascotas = []

def ingresar_mascota():
    nombre = input("Ingrese el nombre de la mascota: ")
    tipo = input("Ingrese el tipo de mascota (perro, gato, etc.): ")
    motivo_consulta = input("Ingrese la descripción de la consulta: ")
    mascotas.append((nombre, tipo, motivo_consulta))
    print("Mascota ingresada correctamente.")

def ver_listado():
    print("Listado completo de mascotas:")
    if mascotas:
        for i, mascota in enumerate(mascotas, start=1):
            print(f"{i}. Nombre: {mascota[0]}, Tipo: {mascota[1]}, Descripción: {mascota[2]}")
    else:
        print("No hay mascotas ingresadas.")

def visualizar_siguiente():
    if mascotas:
        siguiente_mascota = mascotas.pop(0)
        print(f"Siguiente mascota:")
        print(f"Nombre: {siguiente_mascota[0]}, Tipo: {siguiente_mascota[1]}, Descripción: {siguiente_mascota[2]}")
    else:
        print("No hay mascotas en espera.")

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Ingresar mascota")
        print("2. Ver listado completo de mascotas")
        print("3. Visualizar la próxima mascota")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ingresar_mascota()
        elif opcion == "2":
            ver_listado()
        elif opcion == "3":
            visualizar_siguiente()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu()
