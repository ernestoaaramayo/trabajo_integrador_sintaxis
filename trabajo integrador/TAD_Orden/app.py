from TAD_Orden import *
from TAD_OT import *
from TADCola import *
from datetime import *

#Se genera la lista de ordenes
ot = crearOT()
#Variable booleana para el bucle principal while
continuar = True

#Se genera una lista con datos de prueba
def datosprueba(ot):
    datos_prueba = [
        (10001, "Computadora", "Control", "Julian", datetime.strptime("05/06/2026", "%d/%m/%Y").date(), "09:00"),
        (10002, "Equipo 2", "Control", "Marcos", datetime.strptime("05/06/2026", "%d/%m/%Y").date(), "15:00"),
        (10003, "Impresora", "Finanzas", "Elias", datetime.strptime("06/05/2026", "%d/%m/%Y").date(), "10:00"),
        (10004, "Algo", "RRHH", "Hernan", datetime.strptime("20/05/2026", "%d/%m/%Y").date(), "11:00"),
        (10005, "Maquina", "RRHH", "Sandro", datetime.strptime("25/05/2026", "%d/%m/%Y").date(), "12:00"),
        (10006, "Algo 222", "Operaciones", "Ezequiel", datetime.strptime("26/05/2026", "%d/%m/%Y").date(), "13:00")
    ]
    for id_maquina, nombre_equipo, sector_planta, tecnico, fecha, hora in datos_prueba:
        orden = crearOrden()
        cargarOrden(orden, id_maquina, nombre_equipo, sector_planta, tecnico, fecha, hora)
        agregarOrden(ot, orden)
    return ot

#inicializar datos de prueba
datosprueba(ot)

#Bucle principal de la aplicacion
while(continuar == True):
    print("\n\n1) Alta de Ordenes de Trabajo")
    print("2) Modificación de Cronograma")
    print("3) Cancelación de Tareas")
    print("4) Reporte General de Mantenimiento")
    print("5) Reprogramación por Parada de Planta (Traslado Masivo)")
    print("6) Depuración y Generación de Lista de Prioridad")
    print("7) Salir")
    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        orden = crearOrden()

        #While para verificar si el ID ingresado encontro coincidencias, si las encuentra, vuelve a repetir el 
        #bucle hasta que se ingrese una ID unica
        while True:
            id_maquina = int(input("Ingrese ID maquina: "))
            existe = False
            for i in range(tamanio(ot)):
                o = recuperarOrden(ot, i)
                if id_maquina == verIDMaquina(o):
                    existe = True
                    print("El ID ingresado ya existe.")
                    break
            if not existe:
                break

        nombre_equipo = input("Ingrese el nombre del equipo: ")
        sector_planta = input("Ingrese el sector de la planta: ")
        tecnico = input("Ingrese el nombre del técnico: ")

        # Bucle para la Fecha
        while True:
            try:
                #Aunque se ingrese en formato DD/MM/AAAA se guarda en formato AAAA/MM/DD
                f = input("Ingrese fecha (DD/MM/AAAA): ")
                fecha_valida = datetime.strptime(f, "%d/%m/%Y").date()
                if fecha_valida < date.today():
                    print("Error. La fecha es anterior a hoy.")
                    continue
                break
            except ValueError:
                print("Formato de fecha inválido.")

        #Bucle para la Hora
        while True:
            try:
                h = input("Ingrese hora (HH:MM): ")
                hora_valida = datetime.strptime(h, "%H:%M").time()
                break
            except ValueError:
                print("Formato de hora inválido.")
                
        cargarOrden(orden, id_maquina, nombre_equipo, sector_planta, tecnico, fecha_valida, hora_valida)
        agregarOrden(ot, orden)

        print("-----------------------------")
        print("Generando orden...")
        print("ID de la máquina: ", id_maquina)
        print("Nombre del equipo: ", nombre_equipo)
        print("Sector de la planta: ", sector_planta)
        print("Nombre del técnico: ", tecnico)
        print("Fecha de la orden: ", fecha_valida)
        print("Hora de la orden: ", hora_valida)
        print("-----------------------------")

    elif opcion == 2:
        encontrada = False
        id_maquina = int(input("Ingrese ID de la máquina: "))
        for i in range(0, tamanio(ot)):
            o = recuperarOrden(ot, i)

            if verIDMaquina(o) == id_maquina: 
                encontrada = True

                #Nueva fecha
                while True:
                    try:
                        f = input("Ingrese fecha (DD/MM/AAAA): ")
                        nueva_fecha_valida = datetime.strptime(f, "%d/%m/%Y").date()
                        if nueva_fecha_valida < date.today():
                            print("Error. La fecha es anterior a hoy.")
                            continue
                        break
                    except ValueError:
                        print("Formato de fecha inválido.")

                #Nueva hora
                while True:
                    try:
                        h = input("Ingrese hora (HH:MM): ")
                        nueva_hora_valida = datetime.strptime(h, "%H:%M").time()
                        break
                    except ValueError:
                        print("Formato de hora inválido.")
                modFechaProgramada(o, nueva_fecha_valida)
                modHoraInicio(o, nueva_hora_valida)
                break

        if not encontrada:
            print('No se encontró la orden.');

    elif opcion == 3:
        id_maquina = int(input("Ingrese el ID de máquina de la orden a eliminar: "))
        i = 0
        encontrada = False

        while i < tamanio(ot):
            o = recuperarOrden(ot, i)

            if verIDMaquina(o) == id_maquina:
                encontrada = True
                
                print("Nombre del equipo de la orden a eliminar: ", verNombreEquipo(o))
                eliminarOrden(ot, o)
                print("Orden eliminada.") 
                break
            else:
                i+=1
                
        if not encontrada:
            print("No se encontró la orden.")            

    elif opcion == 4:

        print() #Salto de linea
        for i in range(0, tamanio(ot)):
            o = recuperarOrden(ot, i)

            print("ID: {} | Nombre equipo: {} | Sector: {} | Técnico: {} | Fecha: {} | Hora: {}".format(verIDMaquina(o), verNombreEquipo(o), verSectorPlanta(o), verTecnicoAsignado(o), verFechaProgramada(o), verHoraInicio(o)))

    elif opcion == 5:
        fecha_determinada = datetime.strptime(input("Ingrese la fecha de las órdenes que desea modificar (DD/MM/AAAA): "), "%d/%m/%Y").date()

        #Nueva fecha
        while True:
            try:
                f = input("Ingrese la nueva fecha (DD/MM/AAAA): ")
                nueva_fecha_valida = datetime.strptime(f, "%d/%m/%Y").date()
                if nueva_fecha_valida < date.today():
                    print("Error. La fecha es anterior a hoy.")
                    continue
                break
            except ValueError:
                print("Formato de fecha inválido.")

        #Nueva hora
        while True:
            try:
                h = input("Ingrese la nueva hora (HH:MM): ")
                nueva_hora_valida = datetime.strptime(h, "%H:%M").time()
                break
            except ValueError:
                print("Formato de hora inválido.")

        i = 0
        while i < tamanio(ot):
            o = recuperarOrden(ot, i)

            if verFechaProgramada(o) == fecha_determinada:
                modFechaProgramada(o, nueva_fecha_valida)
                modHoraInicio(o, nueva_hora_valida)
                print("Nueva fecha de la orden", verIDMaquina(o),": ",verFechaProgramada(o))

            i+=1

    elif opcion == 6:

        print("\na)Baja de órdenes por sector")
        print("b)Generar nueva cola de prioridades")
        
        while True:
            opc = input("Ingrese la opción seleccionada: ")
            
            if opc == 'a':
                sector_borrar = input("Ingrese el sector de las órdenes que desea eliminar: ")
                i = 0
                while i < tamanio(ot):
                    o = recuperarOrden(ot, i)
                    if sector_borrar == verSectorPlanta(o):
                        eliminarOrden(ot, o)
                        print("Orden eliminada: ", verIDMaquina(o))
                    else:
                        i+=1
                break        
            elif opc == 'b':
                cola = crearCola()
                dia_especifico = datetime.strptime(input("Ingrese el día de las órdenes que desea agregar a la cola(DD/MM/AAAA): "), "%d/%m/%Y").date()
                #Se encolan las ordenes del dia determinado
                for i in range(0, tamanio(ot)):
                    o = recuperarOrden(ot, i)
                    if verFechaProgramada(o) == dia_especifico:
                        encolar(cola, o)
                #Se desencolan y se muestran por pantalla las ordenes agregadas a la cola
                #Agregar while que revise si es vacia
                print("\n-----------------------------")
                while esVacia(cola) != True:
                    elem_cola = desencolar(cola)
                    print("Nombre equipo: {} | Nombre Técnico: {}".format(verNombreEquipo(elem_cola), verTecnicoAsignado(elem_cola)))
                print("-----------------------------")
                break       
            else:
                print('Opción incorrecta. Intente nuevamente.')

    elif opcion == 7:
        print("Saliendo...")
        break