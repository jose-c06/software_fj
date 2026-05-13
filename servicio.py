from abc import ABC, abstractmethod
from entidad import Entidad
from excepciones import ServicioError

class Servicio(Entidad, ABC):

    def __init__(self, nombre, tarifa):

        if tarifa <= 0:
            raise ServicioError("La tarifa debe ser mayor a cero")

        self.nombre = nombre
        self.tarifa = tarifa

    @abstractmethod
    def calcular_costo(self, horas):
        pass

    @abstractmethod
    def descripcion(self):
        pass


class ReservaSala(Servicio):

    def calcular_costo(self, horas, descuento=0):
        total = self.tarifa * horas
        return total - descuento

    def descripcion(self):
        return "Servicio de reserva de salas"


class AlquilerEquipo(Servicio):

    def calcular_costo(self, horas, impuesto=0):
        total = self.tarifa * horas
        return total + impuesto

    def descripcion(self):
        return "Servicio de alquiler de equipos"


class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, horas, impuesto=0, descuento=0):
        total = self.tarifa * horas
        total = total + impuesto - descuento
        return total

    def descripcion(self):
        return "Servicio de asesoría especializada"

    def mostrar_info(self):
        return f"{self.nombre} - Tarifa: ${self.tarifa}"
