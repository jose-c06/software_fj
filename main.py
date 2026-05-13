import logging

from cliente import Cliente
from servicio import ReservaSala
from servicio import AlquilerEquipo
from servicio import AsesoriaEspecializada
from reserva import Reserva

from excepciones import ClienteError
from excepciones import ServicioError
from excepciones import ReservaError


logging.basicConfig(
    filename="logs.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("===================================")
print(" SOFTWARE FJ - SISTEMA DE RESERVAS ")
print("===================================\n")

clientes = []
servicios = []
reservas = []

try:

    cliente1 = Cliente(
        "Jose Castro",
        "josecastrol0710@gmail.com",
        "3103650653"
    )

    clientes.append(cliente1)

    print("Cliente registrado correctamente")

except ClienteError as e:

    logging.error(e)
    print("Error:", e)

try:

    cliente2 = Cliente(
        "",
        "correo_malo",
        "123"
    )

    clientes.append(cliente2)

except ClienteError as e:

    logging.error(e)
    print("Error de cliente:", e)


try:

    sala = ReservaSala(
        "Sala Premium",
        100
    )

    servicios.append(sala)

    print("Servicio creado correctamente")

except ServicioError as e:

    logging.error(e)
    print("Error:", e)


try:

    equipo = AlquilerEquipo(
        "Portatil Gamer",
        -50
    )

    servicios.append(equipo)

except ServicioError as e:

    logging.error(e)
    print("Error:", e)


try:

    reserva1 = Reserva(
        cliente1,
        sala,
    )

        5
    reserva1.confirmar()

    reservas.append(reserva1)

    print("Reserva confirmada")
    print(reserva1.mostrar_reserva())

except ReservaError as e:

    logging.error(e)
    print("Error:", e)


try:

    reserva2 = Reserva(
        cliente1,
        sala,
        -4
    )

    reservas.append(reserva2)

except ReservaError as e:

    logging.error(e)
    print("Error de reserva:", e)


try:

    total = reserva1.procesar()

except ReservaError as e:

    logging.error(e)

else:

    print(f"Costo total: ${total}")

finally:

    print("Proceso finalizado")


try:

    reserva1.cancelar()

    print("Reserva cancelada")

except Exception as e:

    logging.error(e)


try:

    total = reserva1.procesar()

except ReservaError as e:

    logging.error(e)

    print("Error controlado:", e)


print("\n===================================")
print(" SISTEMA EJECUTADO CORRECTAMENTE ")
print("===================================")
