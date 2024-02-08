productos = []

def ingresar_producto():
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    precio_venta = float(input("Ingrese el precio de venta del producto: "))
    costo = float(input("Ingrese el costo del producto: "))
    cantidad_inventario = int(input("Ingrese la cantidad en inventario del producto: "))
    productos.append({"codigo": codigo, "nombre": nombre, "precio_venta": precio_venta, "costo": costo, "cantidad_inventario": cantidad_inventario})
    print("Producto ingresado correctamente.")

def consultar_producto(nombre_producto):
    for producto in productos:
        if producto["nombre"] == nombre_producto:
            print("Datos del producto:")
            print(f"Código: {producto['codigo']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio de venta: {producto['precio_venta']}")
            print(f"Costo: {producto['costo']}")
            print(f"Cantidad en inventario: {producto['cantidad_inventario']}")
            return
    print("Producto no encontrado.")

def entrada_inventario(nombre_producto, cantidad):
    for producto in productos:
        if producto["nombre"] == nombre_producto:
            producto["cantidad_inventario"] += cantidad
            print("Entrada al inventario realizada correctamente.")
            return
    print("Producto no encontrado.")

def salida_inventario(nombre_producto, cantidad):
    for producto in productos:
        if producto["nombre"] == nombre_producto:
            if producto["cantidad_inventario"] >= cantidad:
                producto["cantidad_inventario"] -= cantidad
                print("Salida del inventario realizada correctamente.")
            else:
                print("No hay suficiente cantidad en inventario.")
            return
    print("Producto no encontrado.")

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Ingresar producto")
        print("2. Consultar producto")
        print("3. Realizar entrada al inventario")
        print("4. Realizar salida del inventario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ingresar_producto()
        elif opcion == "2":
            nombre_producto = input("Ingrese el nombre del producto a consultar: ")
            consultar_producto(nombre_producto)
        elif opcion == "3":
            nombre_producto = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad a ingresar al inventario: "))
            entrada_inventario(nombre_producto, cantidad)
        elif opcion == "4":
            nombre_producto = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad a sacar del inventario: "))
            salida_inventario(nombre_producto, cantidad)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu()
