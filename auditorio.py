import os 

auditorio=[
    ['A1', 'A2', 'A3'],
    ['B1', 'B2', 'B3'],
    ['C1', 'C2', 'C3']
]

asientos_disponibles=[]
persona_registrada=[]
asientos_ocupados=[]
persona_asiento=[]
rut_registro=[]


def mostrar():
    dibujo="----------------\n"
    for fila in auditorio:
        for asiento in fila:
            asientos_disponibles.append(asiento)
            if asiento in asientos_ocupados:
                dibujo+= '| X |'
            else:
                dibujo+=f"| {asiento} |"
        dibujo+="\n"
    dibujo+="--------------"
    print(dibujo)


def menup():
    print("************HOLA************")
    print("1- Ver todos los asientos")
    print("2- Reservar ")
    print("3- buscar por asiento")
    print("4- buscar por rut")
    print("5- Salir")
    opcion=int(input("Ingresa una opcion : "))
    try:
        if opcion >0 and opcion <6:
            return opcion
        else:
            input("Fuera de rango")
    except:
        input("no disponible")


def reserva():
    opcion=input("Ingresa asiento que deseas reservar : ")
    if opcion in asientos_disponibles:
        if not opcion in asientos_ocupados:
            nom=input("ingresa tu nombre : ")
            ape=input("Ingresa tu apellido : ")
            rut=input("Ingresa tu rut : ")
            asientos_ocupados.append(opcion)
            persona_registrada.append([opcion,nom,ape,rut])
            persona_asiento.append([opcion,rut,nom,ape])
            rut_registro.append(rut)
            input(f"Asiento {opcion} registrado exitosamente.")
        else:
            input("Asiento ocupado")
    else:
        input("Asiento no existe ")



def buscar_por_asiento():
    asiento=input("Ingresa el asiento que quieres ver : ")
    if asiento in asientos_disponibles:
        if asiento in asientos_ocupados:
            for pasaje in persona_registrada:
                if pasaje[0]==asiento:
                    print(f"Nombre : {pasaje[1]}")
                    print(f"rut : {pasaje[3]}")
                    print(f"Asiento: {pasaje[0]}")
                    print("-----------------")
        else:
            input("Asiento disponible para comprar ")  
    else:
        input("asiento no existe ")

def buscar_por_rut():
    rut=input("Ingresa el rut de reserva : ")
    if rut in rut_registro:
            for pasaje in persona_asiento:
                if pasaje[1]==rut:
                    print(f"Nombre : {pasaje[2]}")
                    print(f"rut : {pasaje[1]}")
                    print(f"Asiento: {pasaje[0]}")
                    print("-----------------")
    else:
        input("rut no existe ")   








menu=True
while menu:
    opcion=menup()
    if opcion ==1:
        mostrar()
        input("")
    if opcion==2:
        mostrar()
        reserva()
    if opcion==3:
        mostrar()
        buscar_por_asiento()
    if opcion==4:
        buscar_por_rut()
    if opcion==5:
        print("ADIU")
        menu=False