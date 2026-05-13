from entidad import Entidad
from excepciones import ClienteError

class Cliente(Entidad):

    def __init__(self, nombre, correo, telefono):

        if not nombre.strip():
            raise ClienteError("El nombre no puede estar vacío")

        if "@" not in correo:
            raise ClienteError("Correo inválido")

        if len(telefono) < 7:
            raise ClienteError("Teléfono inválido")

        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def get_telefono(self):
        return self.__telefono

    def mostrar_info(self):
        return f"Cliente: {self.__nombre} | Correo: {self.__correo}"
