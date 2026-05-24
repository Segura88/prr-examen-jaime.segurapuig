def procesar_mensaje(mensaje):
    if not isinstance(mensaje, str):
        return "ERROR"
    partes = mensaje.split(":", 1)
    if len(partes) != 2:
        return "ERROR"
    comando = partes[0]
    if comando == "INVERTIR":
        return partes[1].strip()[::-1]
    else:
        return "ERROR"