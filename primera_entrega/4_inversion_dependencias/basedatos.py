from abc import ABC, abstractmethod

class BaseDatos(ABC):
    @abstractmethod
    def guardar(self):
        pass
    
    @abstractmethod
    def leer(self):
        pass


class ManejadorDatos:
    def __init__(self):
        pass

    def procesar(self, objeto: BaseDatos):
        objeto.leer()
        objeto.guardar()

class MySQL(BaseDatos):
    def __init__(self):
        pass

    def guardar(self):
        print('El registro fue guardado exitosamente en la bd MySQL.')

    def leer(self):
        print('El registro fue leído exitosamente en la bd MySQL.')

class MongoDB(BaseDatos):
    def __init__(self):
        pass

    def guardar(self):
        print('El registro fue guardado exitosamente en la bd MongoDB.')

    def leer(self):
        print('El registro fue leído exitosamente en la bd MongoDB.')