# cliente.py
import socket
import sys

PORT = 11033
TIMEOUT = 5


def enviar_peticion(host, mensaje):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.settimeout(TIMEOUT)
        try:
            client.connect((host, PORT))
        except OSError as error:
            print(f"ERROR: no se puede conectar a {host}:{PORT}", file=sys.stderr)
            return

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
    # Pedir dirección del servidor al usuario
    try:
        host = input("Introduce la dirección del servidor (pulsa Enter para 127.0.0.1): ").strip()
    except KeyboardInterrupt:
        sys.exit(0)

    if not host:
        host = "127.0.0.1"

    # Enviar un mínimo de 3 mensajes al servidor
    mensajes_a_enviar = [
        "INVERTIR: Hola Mundo",
        "VOCALES: Examen final",
        "DESCONOCIDO: mensaje",
    ]

    for msg in mensajes_a_enviar:
        print(f"Enviando: {msg}")
        enviar_peticion(host, msg)
        print()


if __name__ == "__main__":
    main()