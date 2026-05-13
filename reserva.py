from excepciones import ReservaError

class Reserva:

    def __init__(self, cliente, servicio, horas):

        if horas <= 0:
            raise ReservaError("La duración debe ser mayor a cero")

        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar(self):

        if self.estado == "Cancelada":
            raise ReservaError("No se puede procesar una reserva cancelada")

        costo = self.servicio.calcular_costo(self.horas)

        return costo

    def mostrar_reserva(self):
        return (
            f"Cliente: {self.cliente.get_nombre()} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Horas: {self.horas} | "
            f"Estado: {self.estado}"
        )
