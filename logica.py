def procesar_mensaje(mensaje):
    partes = mensaje.split(":", 1)
    comando = partes[0]
    if comando == "INVERTIR":
        return partes[1].strip()[::-1]