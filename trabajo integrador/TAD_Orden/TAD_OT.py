from TAD_Orden import *

def crearOT():
    ot = []
    return ot

def agregarOrden(ot, orden):
    ot.append(orden)

def eliminarOrden(ot, orden):
    ot.remove(orden)

def recuperarOrden(ot, i):
    return ot[i]

def tamanio(ot):
    return len(ot)