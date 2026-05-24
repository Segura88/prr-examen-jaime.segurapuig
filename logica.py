VOCALES = "aeiouAEIOUáéíóúÁÉÍÓÚ"
COMANDO_INVERTIR = "INVERTIR"
COMANDO_VOCALES = "VOCALES"
ERROR = "ERROR"


def _invertir(contenido):
    return contenido.strip()[::-1]


def _contar_vocales(contenido):
    contador = sum(1 for char in contenido if char in VOCALES)
    return f"{COMANDO_VOCALES}:{contador}"


def procesar_mensaje(mensaje):
    # Validar tipo de dato
    if not isinstance(mensaje, str):
        return ERROR
    
    # Validar formato (comando:contenido)
    if ":" not in mensaje:
        return ERROR
    
    comando, contenido = mensaje.split(":", 1)
    
    # Procesar según comando
    if comando == COMANDO_INVERTIR:
        return _invertir(contenido)
    elif comando == COMANDO_VOCALES:
        return _contar_vocales(contenido)
    else:
        return ERROR
