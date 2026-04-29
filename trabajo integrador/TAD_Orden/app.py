from TAD_Orden import *
from TAD_OT import *

ot = crearOT()
continuar = True

while(continuar == True):
    print("\n\n1)Alta de Ordenes de Trabajo")
    print("2)Modificación de Cronograma")
    print("3)Cancelación de Tareas:")
    print("4)Reporte General de Mantenimiento")
    print("5)Reprogramación por Parada de Planta (Traslado Masivo)")
    print("6)Depuración y Generación de Lista de Prioridad")
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
            fecha = input("Ingrese la fecha de la orden: ")
            hora = input("Ingrese la hora de la orden: ")

            cargarOrden(orden, id_maquina, nombre_equipo, sector_planta, tecnico, fecha, hora)
            agregarOrden(ot, orden)

            seguir = input("Desea continuar agregando ordenes? (si/no)")
        
    
    elif opcion == 2:
        id_maquina = int(input("Ingrese el id de maquina"))
        for i in range(1, tamanio(ot)):
            o = recuperarOrden(ot, i)
            
            if verIDMaquina(o) == id_maquina: 
                nueva_fecha = input('Ingrese la nueva fecha: ')
                nueva_hora = input("Ingrese la nueva hora: ")
                modFechaProgramada(o, nueva_fecha)
                modHoraInicio(o, nueva_hora)
                
            print('No se encontro la orden.');
    
    elif opcion == 3:
        id_maquina = int(input("Ingrese el id de maquina"))
        i = 1
        
        while i < tamanio(ot):
            o = recuperarOrden(ot, i)
            
            if verIDMaquina(o) == id_maquina:
                print("Nombre equipo de orden a eliminar: ", verNombreEquipo(o))
                eliminarOrden(orden, id_maquina) 
            else:
                i+=1
            
        print ("No se encontro la orden.")
    
    elif opcion == 4:
        for i in range(1, tamanio(ot)):
            o = recuperarOrden(ot, i)
            print("\nID Maquina orden: ", verIDMaquina(i))
            print("Nombre del equipo: ", verNombreEquipo(i))
            print("Sector de la planta: ", verSectorPlanta(i))
            print("Tecnico Asignado: ", verTecnicoAsignado(i))
            print("Fecha: %s, hora programada:%s \n", verFechaProgramada(i), verHoraInicio(i))
    
    elif opcion == 5:
        reprogramarOrdenes();
    
    # elif opcion == 6:
                    
    # elif opcion == 7:
    #     continuar = False
print("Saliendo...")






















#Funcion para mostrar en pantalla el numero de orden, el id de la maquina y el nombre del equipo para referencia
        #    while  i < tam(orden): 
        #    o = recuperarOrden(orden, i)
        #print("ID de orden: ", i + 1, "|", "ID del equipo: ", verIDMaquina(o), "|", "Nombre del equipo: ", verNombreEquipo(o))
        #    i += 1