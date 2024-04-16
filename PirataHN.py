from abc import ABC, abstractmethod

class Canal:
    def __init__(self, nombre, codigo, pais_origen, suscripcion_paga, monto_mensual):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__pais_origen = pais_origen
        self.__suscripcion_paga = suscripcion_paga
        self.__monto_mensual = monto_mensual
        self.__productos = []

    @property
    def nombre(self):
        return self.__nombre

    def agregar_producto(self, producto):
        self.__productos.append(producto)

    def mostrar_productos(self):
        for producto in self.__productos:
            print(producto)

    def utilidad_por_canal(self):
        return len(self.__productos) * self.__monto_mensual

    @staticmethod
    def saludo():
        return "¡Bienvenido al canal!"

class Producto(ABC):
    def __init__(self, nombre, anio_publicacion, ranking, costos, visualizaciones):
        self.__nombre = nombre
        self.__anio_publicacion = anio_publicacion
        self.__ranking = ranking
        self.__costos = costos
        self.__visualizaciones = visualizaciones

    @abstractmethod
    def recaudacion(self):
        pass

    def __str__(self):
        return f'{self.__nombre}, {self.__anio_publicacion}, {self.__ranking}, {self.recaudacion()}'

class Capitulo:
    def __init__(self, nombre, duracion, ranking):
        self.__nombre = nombre
        self.__duracion = duracion
        self.__ranking = ranking

class Temporada:
    def __init__(self, capitulos):
        self.__capitulos = capitulos

class Serie(Producto):
    def __init__(self, nombre, anio_publicacion, ranking, costos, visualizaciones, temporadas):
        super().__init__(nombre, anio_publicacion, ranking, costos, visualizaciones)
        self.__temporadas = [Temporada(temporada) for temporada in temporadas]

    def recaudacion(self):
        if len(self.__temporadas) == 1:
            return 0.2 * self.__costos / self.__visualizaciones
        else:
            return 0.5 * self.__costos / self.__visualizaciones * len(self.__temporadas)

class Pelicula(Producto):
    def __init__(self, nombre, anio_publicacion, ranking, generos, actores_principales, costos, visualizaciones):
        super().__init__(nombre, anio_publicacion, ranking, costos, visualizaciones)
        self.__generos = generos
        self.__actores_principales = actores_principales

    def recaudacion(self):
        return 0.8 * self.__costos / self.__visualizaciones

def menu():
    print("1. Agregar canal")
    print("2. Agregar serie a canal")
    print("3. Agregar película a canal")
    print("4. Mostrar productos de canal")
    print("5. Calcular utilidad de canal")
    print("6. Salir")

def main():
    canales = []
    while True:
        menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            nombre = input("Nombre del canal: ")
            codigo = input("Código del canal: ")
            pais_origen = input("País de origen del canal: ")
            suscripcion_paga = input("¿Se paga por suscripción? (s/n): ") == "s"
            monto_mensual = float(input("Monto mensual de la suscripción: "))
            canal = Canal(nombre, codigo, pais_origen, suscripcion_paga, monto_mensual)
            canales.append(canal)
        elif opcion == "2":
            nombre_canal = input("Nombre del canal: ")
            for canal in canales:
                if canal.nombre == nombre_canal:
                    nombre = input("Nombre de la serie: ")
                    anio_publicacion = int(input("Año de publicación: "))
                    ranking = float(input("Ranking: "))
                    costos = float(input("Costos: "))
                    visualizaciones = int(input("Visualizaciones: "))
                    temporadas = int(input("Número de temporadas: "))
                    producto = Serie(nombre, anio_publicacion, ranking, costos, visualizaciones, temporadas)
                    canal.agregar_producto(producto)
                    break
            else:
                print("Canal no encontrado.")
        elif opcion == "3":
            nombre_canal = input("Nombre del canal: ")
            for canal in canales:
                if canal.nombre == nombre_canal:
                    nombre = input("Nombre de la película: ")
                    anio_publicacion = int(input("Año de publicación: "))
                    ranking = float(input("Ranking: "))
                    generos = input("Géneros (separados por comas): ").split(',')
                    actores_principales = input("Actores principales (separados por comas): ").split(',')
                    costos = float(input("Costos: "))
                    visualizaciones = int(input("Visualizaciones: "))
                    producto = Pelicula(nombre, anio_publicacion, ranking, generos, actores_principales, costos, visualizaciones)
                    canal.agregar_producto(producto)
                    break
            else:
                print("Canal no encontrado.")
        elif opcion == "4":
            nombre_canal = input("Nombre del canal: ")
            for canal in canales:
                if canal.nombre == nombre_canal:
                    canal.mostrar_productos()
                    break
            else:
                print("Canal no encontrado.")
        elif opcion == "5":
            nombre_canal = input("Nombre del canal: ")
            for canal in canales:
                if canal.nombre == nombre_canal:
                    print("Utilidad del canal:", canal.utilidad_por_canal())
                    break
            else:
                print("Canal no encontrado.")
        elif opcion == "6":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main() 