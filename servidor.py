# servidor.py
import socket
import sys
from logica import procesar_mensaje 

HOST = "0.0.0.0"
PORT = 11033  

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Servidor escuchando en {HOST}:{PORT}", flush=True)

    try:
        while True:
            conn, addr = server.accept()
            with conn:
                # Lee la petición byte a byte hasta encontrar '\n' o cierre
                linea = b""
                while True:
                    chunk = conn.recv(1)
                    if not chunk:
                        break
                    linea += chunk
                    if chunk == b"\n":
                        break

                if not linea:
                    continue

                texto = linea.decode("utf-8", errors="replace").rstrip("\n")

                # Imprimir en stderr: dirección IP del cliente y mensaje recibido
                print(f"[{addr[0]}] Mensaje: {texto}", file=sys.stderr)

                # Procesamos con nuestra lógica aislada
                respuesta_texto = procesar_mensaje(texto)

                # Construye la respuesta terminada en salto de línea y envíala
                if not respuesta_texto.endswith("\n"):
                    respuesta_texto += "\n"
                    
                conn.sendall(respuesta_texto.encode("utf-8"))
    except KeyboardInterrupt:
        print("\nApagando servidor...")
    finally:
        server.close()

if __name__ == "__main__":
    main()