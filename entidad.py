entidad.py
from abc import ABC, abstractmethod

class Entidad(ABC):
    """
    Clase abstracta base del sistema.
    """

    @abstractmethod
    def mostrar_info(self):
        pass
      
