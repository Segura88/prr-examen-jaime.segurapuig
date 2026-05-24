# cliente.py
import socket

HOST = "127.0.0.1"
PORT = 11033
TIMEOUT = 5


def enviar_peticion(mensaje):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.settimeout(TIMEOUT)
        client.connect((HOST, PORT))

        # Enviar el mensaje con salto de línea
        if not mensaje.endswith("\n"):
            mensaje += "\n"
        client.sendall(mensaje.encode("utf-8"))

        # Recibir la respuesta
        respuesta = b""
        while True:
            trozo = client.recv(4096)
            if not trozo:
                break
            respuesta += trozo

        print(respuesta.decode("utf-8").strip())


def main():
    # Enviar un mínimo de 3 mensajes al servidor
    mensajes_a_enviar = [
        "INVERTIR: Hola Mundo",
        "VOCALES: Examen final",
        "DESCONOCIDO: mensaje",
    ]

    for msg in mensajes_a_enviar:
        print(f"Enviando: {msg}")
        enviar_peticion(msg)
        print()


if __name__ == "__main__":
    main()