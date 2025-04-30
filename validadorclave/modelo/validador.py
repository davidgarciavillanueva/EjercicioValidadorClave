from abc import ABC, abstractmethod



class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada:int ):
        self.longitud_esperada=longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        return len(clave) > self._longitud_esperada

    def _contiene_mayuscula(self, clave: str) -> bool:
        return any(c.isupper() for c in clave)

    def _contiene_minuscula(self, clave: str) -> bool:
        return any(c.islower() for c in clave)



class Validador:
    pass

class ReglaValidacionGanimedes:
    pass

class ReglaValidacionCalisto:
    pass