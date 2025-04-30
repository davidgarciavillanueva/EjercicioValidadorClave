from abc import ABC, abstractmethod

class Validador:
    pass

class ReglaValidacionGanimedes:
    pass

class ReglaValidacionCalisto:
    pass

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada:int ):
        self.longitud_esperada=longitud_esperada
