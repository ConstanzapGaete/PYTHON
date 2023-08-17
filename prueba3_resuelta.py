import os

bus = [
    ['A0', 'A1', 'A2', 'A3'],
    ['B0', 'B1', 'B2', 'B3'],
    ['C0', 'C1', 'C2', 'C3'],
    ['D0', 'D1', 'D2', 'D3'],
    ['E0', 'E1', 'E2', 'E3']
]

asientos_disponibles = []
asientos_ocupados = []
pasaje_comprado = []

def mostrar_bus():
    dibujar_bus = "----- BUS ------\n"
    for fila in bus:
        for asiento in fila:
            asientos_disponibles.append(asiento)
            if asiento in asientos_ocupados:
                dibujar_bus += f"**{asiento}**"
            else:
                dibujar_bus += f" /{asiento}/ "
        dibujar_bus += "\n"
    dibujar_bus += "---------------\n"
    print(dibujar_bus)


def registrar_viaje():
    asiento = input("Seleccione uno de los asientos Disponible > ")

    if asiento in asientos_disponibles:
        if not asiento in asientos_ocupados:
            input(" asiento existe y esta disponible ")
            asientos_ocupados.append(asiento)

            origen = validar_origen()
            destino = input("Destino : ")
            rut = input("Rut : ")
            nombre = input("Nombre : ")
            apellido = input("Apellido : ")
            direccion = input("Dirección : ")
            telefono_emergencia = validar_telefono()

            pasaje_comprado.append(
                [asiento, origen, destino, rut, nombre, apellido, direccion, telefono_emergencia]
                #   0        1      2       3       4       5           6       7
            )

            input(f" Pasaje con asiento número {asiento} fue registrado exitosamente > ")

        else:
            input(" asiento esta ocupado ")
    else:
        input(" asiento no existe ")

def mostrar_viaje():
    asiento = input("Ingresa el asiento que deseas ver > ")
    if asiento in asientos_disponibles:
        if asiento in asientos_ocupados:
            for pasaje in pasaje_comprado:
                if pasaje[0] == asiento:
                    print(f"--- PASAJE {asiento} -----")
                    print(f"Origen: {pasaje[1]} ")
                    print(f"Destino: {pasaje[2]} ")
                    print(f"RUT: {pasaje[3]} ")
                    print(f"NOMBRE: {pasaje[4]} ")
                    print(f"APELLIDO: {pasaje[5]} ")
                    print(f"DIRECCION: {pasaje[6]} ")
                    print(f"TELEFONO EMERGENCIA: {pasaje[7]} ")
                    input("------------------")
        else:
            input("Asiento disponible para comprar > ")
    else:
        input(" asiento no existe ")

def mostrar_todos_viajes():
    os.system("cls")
    for pasaje in pasaje_comprado:
        print(f"--- PASAJE {pasaje[0]} -----")
        print(f"NOMBRE: {pasaje[4]} ")
        print(f"APELLIDO: {pasaje[5]} ")
    input("------------------")

def validar_telefono():
    validar = True
    while validar:
        try:
            telefono_emergencia = int(input("telefono emergencia : "))
            if telefono_emergencia > 99999999 and telefono_emergencia < 1000000000:
                validar = False
            else: 
                input("El telefono debe tener 9 dígitos, presione enter  ")
        except:
            input("Error en el teléfono, presione enter  ")
    return telefono_emergencia

def validar_origen():
    validar = True
    while validar:
        try:
            origen = input("Origen : ")
            if len(origen) > 2 and len(origen) < 21:
                validar = False
            else: 
                input("El origen debe tener entre 3 y 20 dígitos, presione enter  ")
        except:
            input("Error en el origen, presione enter  ")
    return origen

def menu_general():
    os.system("cls")
    print("---- MENU ----")
    print("1. Registrar Viaje")
    print("2. Mostrar Asiento")
    print("3. Mostrar información de un viaje")
    print("4. Mostrar información de TODOS LOS viaje")
    print("5. Salir")
    try:
        opcion = int(input("Ingrese una opción > "))
        if opcion > 0 and opcion < 6:
            return opcion
        else:
            input("opción fuera de rango, presione enter > ")
    except:
        input("opción no válida, presione enter > ")

menu = True
while menu:
    opcion = menu_general()
    if opcion == 1:
        mostrar_bus()
        registrar_viaje()
    if opcion == 2:
        mostrar_bus()
        input("opcion 2")
    if opcion == 3:
        mostrar_bus()
        mostrar_viaje()
    if opcion == 4:
        mostrar_todos_viajes()
    if opcion == 5:
        print("Salió del sistema, ADIOS")
        menu = False