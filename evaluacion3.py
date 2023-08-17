import os

bus= [
    ['A0','A1','A2','A3'],
    ['B0','B1','B2','B3'],
    ['C0','C1','C2','C3'],
    ['D0','D1','D2','D3'],
    ['E0','E1','E2','E3'],
    ['F0','F1','F2','F3'],
    ['H0','H1','H2','H3'],
    ['I0','I1','I2','I3'],
    ['J0','J1','J2','J3'],
    ['K0','K1','K2','K3'],
    ['L0','L1','L2','L3'],
    ['M0','M1','M2','M3'],
    ['N0','N1','N2','N3'],
    ['O0','O1','O2','O3'],
    ['P0','P1','P2','P3']
]


asientos_comprados=[ ]
pasajeros_registrados=[ ]
asientos_disponibles =[ ]


def mostrar_bus():
     dibujar_bus="--------Bus--------"
     for fila in bus:
          for asiento in fila:
               
               asientos_disponibles.append(asiento)
               
               if asiento in asientos_comprados:
                    dibujar_bus+=f"[X]"
               else:
                 dibujar_bus+=f"[{asiento}]"
          dibujar_bus+="\n"
     print(dibujar_bus)

def menu_general():
    print("***********BIENVENIDO A TRANSPORTES REGIONALES***********")
    print("1.- Registrar nuevo viaje ")
    print("2.- Mostrar asientos")
    print("3.- Mostrar informacion de un viaje ")
    print("4.- Mostrar informacion de todos los viajes")
    print("5.- Salir del programa")
    try:
        opcion=int(input("Selecciona una opcion > "))
        if opcion >0 and opcion<6:
            return opcion
        else:
            input("Opcion no disponible , vuelve a intentarlo >  ")
    except:
        input("Error , presiona enter para continuar > ")

def menu_registrar():
     asiento=input("Ingrese el asiento que desea utilizar > ")
     if asiento in asientos_disponibles:
            if not asiento in asientos_comprados:
                asientos_comprados.append(asiento)

                print("Favor indique Los siguientes datos > ")
                origen = validar_origen()
                destino= validar_destino()
                rut= validar_rut()
                nombre= input("Nombre >  ")
                apellido=input("Apellido > ")
                direccion=input("Direccion > ")
                telef=validar_telefono()
                pasajeros_registrados.append([asiento,origen,destino,rut,nombre,apellido,direccion,telef])
                os.system("cls")
                input(f"El asiento {asiento} Fue registrado")
            else:
                input("El asiento indicado esta ocupado , presiona cualquier tecla para continuar > ")
     else :
            input("El asiento no Existe, presiona cualquier tecla para continuar > ")

def mostrar_viaje():
     asiento =input("Ingresa el asiento que deseas ver >")
     if asiento in asientos_disponibles:
          if asiento in asientos_comprados:
               for pasaje in pasajeros_registrados:
                    if pasaje[0]==asiento:
                         print(f"pasaje {asiento}")
                         print(f"origen{pasaje[1]}")
                         print(f"destino{pasaje[2]}")
                         print(f"rut{pasaje[3]}")
                         print(f"nombre{pasaje[4]}")
                         print(f"apellido{pasaje[5]}")
                         print(f"direccion{pasaje[6]}")
                         print(f"telef{pasaje[7]}")
                         input("")
          else:
               input("Asiento no disponible")
     else:
          input("disponible")
    
def mostrar_todos_viajes():
     os.system("cls")
     for pasaje in pasajeros_registrados:
          print(f"Pasaje{pasaje[0]} ")
          print(f"nombre{pasaje[4]}")
          print(f"apellido{pasaje[5]}")

     input("--------------------------------")

def validar_rut():
     validar=input("Ingresa tu rut con puntos y guion >")
     try:
          if len(validar)==12:
               return validar
     except:
          input("Rut no valido vuelve a intentarlo ")


def validar_origen():
     validar=input("Ingresa Ciudad de origen >")
     try:
          if len(validar)>3 and len(validar)<21:
               return validar
     except:
          input("Ciudad de origen no valida ,intentalo denuevo >")
          
def validar_destino():
     validar=input("Ingresa Ciudad de Destino >")
     try:
          if len(validar)>3 and len(validar)<21:
               return validar
     except:
          input("Ciudad de Destino no valida ,intentalo denuevo >")


def validar_telefono():
     validar=True
     while validar:
          try:
               telef=int(input("Telefono de emergencia"))
               if telef>999999999 and telef <1000000000:
                    validar=False
               else:
                    input("El telefono debe tener 9 digitos")
                    return telef
          except:
               input("Error en el telefono ")

menu_g=True

while menu_g:
     opcion = menu_general()
     if opcion==1:
          mostrar_bus()
          menu_registrar()
     if opcion==2:
          mostrar_bus()
     if opcion==3:
          mostrar_bus() 
          mostrar_viaje()
     if opcion==4:
          mostrar_todos_viajes()   
     if opcion==5:
          print("salio del sistema")
          menu_g=False
