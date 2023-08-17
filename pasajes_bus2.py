import os

bus = [
    ['A0', 'A1', 'A2'],
    ['B0', 'B1', 'B2'],
    ['C0', 'C1', 'C2'],
    ['D0', 'D1', 'D2'],
    ['E0', 'E1', 'E2'],
    ['F0', 'F1', 'F2'],
    ['G0', 'G1', 'G2'],
    ['H0', 'H1', 'H2'],
]

def imprir_asientos():
    os.system("cls")
    i_asientos = "------ BUS ------\n"
    for fila in bus:
        for asiento in fila:
            
            asientos_del_bus.append(asiento) # Agrego a una array todos los asientos del bus

            if asiento in asientos_comprados:
                i_asientos += "[ -- ]"
            else:
                i_asientos +=f"[{asiento}]"
        
        i_asientos += "\n"

    print(i_asientos)


def menu_general():
    os.system("cls")
    print("--- BUSES ESPEEDY GONZALEZ ---")
    print("1. Mostrar Asientos")
    print("2. Comprar pasaje")
    print("3. Ver pasajero")
    print("4. Cancelar Pasaje")
    print("5. Cancelar Compra")
    print("6. Salir- Ciao")

    try:
        opcion = int(input("Seleccione una de las opciones disponibles > "))
        if opcion > 0 and opcion < 7:
            return opcion
        else:
            input("la opción ingresada no es válida, presione enter para continuar > ")
    except:
        input("Error en el menu general, aprete enter para continuar > ")


def comprar_asiento():
    opcion = input("Ingrese el asiento que desea utilizar > ")

    if opcion in asientos_del_bus:
        if not opcion in asientos_comprados:
            asientos_comprados.append(opcion)
                # el .append() permite ingresar valores dentro de un array definido
            os.system("cls")
            persona_pasaje(opcion)
            input(f"El asiento {opcion} fue registrado")
        else:
            input("El asiento indicado se encuentra ocupado, por favor presione enter para continuar > ")
    else:
        input("El asiento indicado no existe, aprete enter para continuar > ")

def persona_pasaje(asiento):
    print("Favor indique sus datos:")
    rut = input("Rut : ")
    nombre = input("Nombre : ")
    apellido = input("Apellido : ")

    pasajero_bus.append([asiento,rut,nombre,apellido])


def imprimir_pasajero():

    asiento = input("Seleccione uno de los asientos > ")

    print("---- PASAJERO -----")

    for pasajero in pasajero_bus:
        if asiento in pasajero:
            print(f"Asiento: {pasajero[0]}")
            print(f"Rut: {pasajero[1]}")
            print(f"Nombre: {pasajero[2]}")
            print(f"Apellido: {pasajero[3]}")

            input("")


asientos_comprados = []
asientos_del_bus = []
pasajero_bus = []

menu = True
while menu:
    op_menu = menu_general()
    if op_menu == 1:
        imprir_asientos()
        input("")
    elif op_menu == 2:
        imprir_asientos()
        comprar_asiento()
    elif op_menu == 3:
        imprir_asientos()
        imprimir_pasajero()

    