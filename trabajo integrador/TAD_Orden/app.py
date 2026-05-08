from TAD_Orden import *
from TAD_OT import *
from TADCola import *

#Se genera la lista de ordenes
ot = crearOT()
#Variable booleana para el bucle principal while
continuar = True

#Se genera una lista con datos de prueba
def datosprueba(ot):
    datos_prueba = [
        (10001, "Computadora", "Control", "Julian", "06-05-2026", "09:00"),
        (10002, "Equipo 2", "Control", "Marcos", "06-05-2026", "15:00"),
        (10003, "Impresora", "Finanzas", "Elias", "06-05-2026", "10:00"),
        (10004, "Algo", "RRHH", "Hernan", "20-05-2026", "11:00"),
        (10005, "Maquina", "RRHH", "Sandro", "25-05-2026", "12:00"),
        (10006, "Algo 222", "Operaciones", "Ezequiel", "26-05-2026", "13:00")
    ]
    for id_maquina, nombre_equipo, sector_planta, tecnico, fecha, hora in datos_prueba:
        orden = crearOrden()
        cargarOrden(orden, id_maquina, nombre_equipo, sector_planta, tecnico, fecha, hora)
        agregarOrden(ot, orden)
    return ot


datosprueba(ot)

while(continuar == True):
    print("\n\n1) Alta de Ordenes de Trabajo")
    print("2) Modificación de Cronograma")
    print("3) Cancelación de Tareas:")
    print("4) Reporte General de Mantenimiento")
    print("5) Reprogramación por Parada de Planta (Traslado Masivo)")
    print("6) Depuración y Generación de Lista de Prioridad")
    print("7) Salir")
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        seguir = "si"
        orden = crearOrden()
        
        while seguir == "si":
            id_maquina = int(input("Ingrese ID de la maquina: "))
            nombre_equipo = input("Ingrese el nombre del equipo: ")
            sector_planta = input("Ingrese el sector de la planta: ")
            tecnico = input("Ingrese el nombre del tecnnico: ")
            fecha = input("Ingrese la fecha de la orden (DD-MM-YYYY): ")
            hora = input("Ingrese la hora de la orden(HH:MM): ")

            cargarOrden(orden, id_maquina, nombre_equipo, sector_planta, tecnico, fecha, hora)
            agregarOrden(ot, orden)
            
            print("-----------------------------")
            print("Generando orden...")
            print("ID de la maquina: ", id_maquina)
            print("Nombre del equipo: ", nombre_equipo)
            print("Sector de la planta: ", sector_planta)
            print("Nombre del tecnnico: ", tecnico)
            print("Fecha: ", fecha)
            print("Hora de la orden: ", hora)
            print("-----------------------------")

            seguir = input("Desea continuar agregando ordenes? (si/no)")
        
    
    elif opcion == 2:
        id_maquina = int(input("Ingrese el id de maquina: "))
        for i in range(0, tamanio(ot)):
            o = recuperarOrden(ot, i)
            
            if verIDMaquina(o) == id_maquina: 
                nueva_fecha = input('Ingrese la nueva fecha(DD-MM-YYYY): ')
                nueva_hora = input("Ingrese la nueva hora(HH:MM): ")
                modFechaProgramada(o, nueva_fecha)
                modHoraInicio(o, nueva_hora)
                
            print('No se encontro la orden.');
    
    elif opcion == 3:
        id_maquina = int(input("Ingrese el id de maquina: "))
        i = 0
        id_valido=False
        
        while i < tamanio(ot):
            o = recuperarOrden(ot, i)
            
            if verIDMaquina(o) == id_maquina:
                id_valido = True
                print("Nombre equipo de orden a eliminar: ", verNombreEquipo(o))
                eliminarOrden(ot, o)
                print("Orden eliminada.") 
                break
            else:
                i+=1
                
        if id_valido == False:
            print("No se encontro la orden.")            
        
    
    elif opcion == 4:
        
        print() #Salto de linea
        for i in range(0, tamanio(ot)):
            o = recuperarOrden(ot, i)
            
            print("ID: {} | Nombre equipo: {} | Sector: {} | Tecnico: {} | Fecha: {} | Hora: {}".format(verIDMaquina(o), verNombreEquipo(o), verSectorPlanta(o), verTecnicoAsignado(o), verFechaProgramada(o), verHoraInicio(o)))
            
            #print("\nID Maquina orden: ", verIDMaquina(o))
            #print("Nombre del equipo: ", verNombreEquipo(o))
            #print("Sector de la planta: ", verSectorPlanta(o))
            #print("Tecnico Asignado: ", verTecnicoAsignado(o))
            #print("Fecha: \n", verFechaProgramada(o))
            #print("Hora programada: \n", verHoraInicio(o))

    elif opcion == 5:
        fecha_determinada = input("Ingrese la fecha de las ordenes que desea modificar: ")
        nueva_fecha = input('Ingrese la nueva fecha: ')
        nueva_hora = input("Ingrese la nueva hora: ")
        
        i = 0
        while i < tamanio(ot):
            o = recuperarOrden(ot, i)

            if verFechaProgramada(o) == fecha_determinada:
                modFechaProgramada(o, nueva_fecha)
                modHoraInicio(o, nueva_hora)
                print("Nueva fecha de la orden ", verIDMaquina(o),": ",verFechaProgramada(o))
            
            i+=1
    
    elif opcion == 6:
        print("\na)Baja de ordenes por sector")
        print("b)Generar nueva cola de prioridades")
        opc = input("Ingrese la opcion seleccionada: ")
        
        if opc == 'a':
            sector_borrar = input("Ingrese el sector de las ordenes que desea eliminar: ")

            i = 0
            while i < tamanio(ot):
                o = recuperarOrden(ot, i)
                if sector_borrar == verSectorPlanta(o):
                    eliminarOrden(ot, o)
                else:
                    i+=1
        else:
            if opc == 'b':
                cola = crearCola()
                dia_especifico = input("Ingrese el dia de las ordenes que desea agregar a la cola: ")
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
                    print("Nombre equipo: {} | Nombre Tecnico: {}".format(verNombreEquipo(elem_cola), verTecnicoAsignado(elem_cola)))

                print("-----------------------------")

            else:
                print('Opcion incorrecta. Intente nuevamente.')
    
    elif opcion == 7:
        print("Saliendo...")
        break