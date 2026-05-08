def crearOrden ():
    return [0, "", "", "", "", "", ""]

def cargarOrden(orden, id_maquina, nombre_equipo, sector_planta, tecnico, fecha, hora):
    orden[0] = id_maquina
    orden[1] = nombre_equipo
    orden[2] = sector_planta
    orden[3] = tecnico
    orden[4] = fecha
    orden[5] = hora 

def verIDMaquina(orden):
    return orden[0]

def verNombreEquipo(orden):
    return orden[1]

def verSectorPlanta(orden):
    return orden[2]

def verTecnicoAsignado(orden):
    return orden[3]

def verFechaProgramada(orden):
    return orden[4]

def verHoraInicio(orden):
    return orden[5]

def modIDMaquina(orden, nuevo):
    orden[0] = nuevo

def modNombreEquipo(orden, nuevo):
    orden[1] = nuevo

def modSectorPlanta(orden, nuevo):
    orden[2] = nuevo

def modTecnicoAsignado(orden, nuevo):
    orden[3] = nuevo

def modFechaProgramada(orden, nuevo):
    orden[4] = nuevo

def modHoraInicio(orden, nuevo):
    orden[5] = nuevo