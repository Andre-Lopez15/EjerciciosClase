class Cuartos:
    def __init__(self, ventanas, medidasCuartos):
        self.__ventanas=ventanas
        self.__medidas=medidasCuartos
        
        def getventanas(self):
            return self.__ventanas
        
        def setventanas(self):
            self.__ventanas
        
        def getmedidasCuartos(self):
            return self.__medidasCuartos
        
        def setmedidasCuartos(self):
            self.__medidasCuartos

class Sala:
    def __init__(self, chimenea, descripcion):
        self.__chimenea=chimenea
        self.__descripcion=descripcion
        
        def getchimenea(self):
            return self.__chimenea
        
        def setchimenea(self):
            self.__chimenea
        
        def getdescripcion(self):
            return self.__descripcion
        
        def setdescripcion(self):
            self.__descripcion


class Lavatrastos:
    def __init__(self, depositos, aguaCaliente):
        self.__depositos=depositos
        self.__aguaCaliente=aguaCaliente
        
        def getdepositos(self):
            return self.__depositos
        
        def setdepositos(self):
            self.__depositos
            
        def getaguaCaliente(self):
            return self.__aguaCaliente
        
        def setaguaCaliente(self):
            self.__aguaCaliente
            
class Cocina:
    def __init__(self, electrodomesticos, medidasCocina, materialDesayunador, lavatrastos):
        self.__electrodomesticos=electrodomesticos
        self.__medidasCocina=medidasCocina
        self.__materialDesayunador=materialDesayunador
        self.__lavatrastos=lavatrastos
        
        def getelectrodomesticos(self):
            return self.__electrodomesticos
        
        def setelectrodomesticos(self):
            self.__electrodomesticos
            
        
        def getmedidasCocina(self):
            return self.__medidasCocina
        
        def setmedidasCocina(self):
            self.__medidasCocina
            
        
        def getmaterialDesayunador(self):
            return self.__materialDesayunador   
        
        def setmaterialDesayunador(self):
            self.__materialDesayunador
            
        
        def getlavatrastos(self):
            return self.__lavatrastos
        
        def setlavatrastos(self):
            self.__lavatrastos

class Patio:
    def __init__(self, areaSocial, medidasPatio, descripcionPatio):
        self.__areaSocial=areaSocial
        self.__medidasPatio=medidasPatio
        self.__descripcionPatio=descripcionPatio
        
        def getareaSocial(self):
            return self.__areaSocial
        
        def setareaSocial(self):
            self.__areaSocial
        
        def getmedidasPatio(self):
            return self.__medidasPatio
        
        def setmedidasPatio(self):
            self.__medidasPatio
        
        def getdescripcionPatio(self):
            return self.__descripcionPatio
        
        def setdescripcionPatio(self):
            self.__descripcionPatio
            
            
class Estado:
    def __init__(self, nombre, fecha):
        self.__nombre=nombre
        self.__fecha=fecha
        
        def getnombre(self):
            return self.__nombre
        
        def setnombre(self):
            self.__nombre
        
        def getfecha(self):
            return self.__fecha
        
        def setfecha(self):
            self.__fecha
            
