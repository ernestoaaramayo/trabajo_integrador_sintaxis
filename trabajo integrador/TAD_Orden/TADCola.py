def crearCola():
    return []

def esVacia(cola):
    return len(cola) == 0

def encolar(cola, elem):
    cola.append(elem)

def desencolar(cola):
    if esVacia(cola):
        return None

    elem = cola[0]
    del cola[0]
    return elem

def tamanio(cola):
    return len(cola)

def copiarCola(destino, origen):

    aux = crearCola()

    while not esVacia(origen):
        elem = desencolar(origen)
        encolar(aux, elem)

    while not esVacia(aux):
        elem = desencolar(aux)

        encolar(destino, elem)
        encolar(origen, elem)
