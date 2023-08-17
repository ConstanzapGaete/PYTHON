
import os

bus= [
    ['A0','A1','A2'],
    ['B0','B1','B2'],
    ['C0','C1','C2'],
    ['D0','D1','D2'],
    ['E0','E1','E2'],
    ['F0','F1','F2'],
    ['H0','H1','H2'],
]

def imprimir_asientos():
    os.system("cls")
    i_asientos="-------BUS-------\n"
    for fila in bus:
        for asiento in fila:
            asiento_del_bus.append(asiento)
            if asiento in asientos_comprados:
                i_asientos+="[ -- ]"
            else:
                i_asientos+=f"[{asiento}]"
        i_asientos+="\n"

    print(i_asientos) 

def menu_general():
    print("----------BUSES CARACOL----------")
    print("1.- Mostrar asientos")
    print("2.- Comprar pasajes")
    print("3.- Ver Pasajero")
    print("4.- Pagar pasajes")
    print("5.- Cancelar compra")
    print("6.- Salir")
    try:
        opcion=int(input("Selecciona una opcion > "))
        if opcion >0 and opcion<7:
            return opcion
        else:input("No disponible")
    except:
        input("no disponible")

def comprar_asiento():
    opcion=input("Ingrese el asiento que desea utilizar > ")
    if opcion in asiento_del_bus:
        if not opcion in asientos_comprados:
            asientos_comprados.append(opcion)
            os.system("cls")
            persona_pasaje(opcion)
            input(f"El asiento {opcion} Fue registrado")
        else:
            ("El asiento esta ocupado ")
    else :
        input("error presiona cualquier tecla para continuar > ")

  
def persona_pasaje(asiento):
    print("Favor indique sus datos > ")
    rut = input("Rut : ")
    nombre= input("Nombre: ")
    apellido= input("Apellido: ")

    pasajero_bus.append([asiento,rut,nombre,apellido])

def imprimir_pasajero():
    asiento= input("Seleccione uno de los asientos > ")
    print("**********PASAJERO**********")
    for pasajero in pasajero_bus:
        if asiento in pasajero :
            print(f"Asiento: {pasajero[0]}")
            print(f"Rut: {pasajero[1]}")
            print(f"Nombre: {pasajero[2]}")
            print(f"Apellido: {pasajero[3]}")

            input("")

def cancelar_pasaje():
    os.system("cls")
    print(f"Pasaje{ asientos_comprados} cancelado ")
    asientos_comprados==0
    input("ingresa  enter para volver al menu principal ")

def salir():
    os.system("cls")
    print("********Vuelva pronto********")
    input("")

def pago_pasaje():
    if asientos_comprados >0:
        print(f"Asientos {asientos_comprados}")
        print(f"Total a pagar : "({asientos_comprados}*4500))
    else:
        ("no se a seleccionado ningun asiento ")
        

asientos_comprados=[ ]
asiento_del_bus=[ ]
pasajero_bus=[]
menu=True
while menu:
    op_menu= menu_general()
    if op_menu==1:
        imprimir_asientos()
        input(" ")
    elif op_menu==2:
        imprimir_asientos()
        comprar_asiento()
    elif op_menu==3:
        imprimir_asientos()
        imprimir_pasajero()
    elif op_menu==4:
        pago_pasaje()
    elif op_menu==5:
        cancelar_pasaje()
    elif op_menu==6:
        salir()


