import os
sw=0
ent=0
opc=0
val1=2500
val2=5000
val3=1000
dcto=0
contador2=0
cantidad_entradas1=0
cantidad_entradas2=0
cantidad_entradas3=0
totalcancel1=0
totalcancel2=0
totalcancel3=0

while sw==0:
    print("***********Bienvenido a Buena Venturas FC***********")
    try:
       print("Menu de entradas")
       print("1-Entrada menores")
       print("2-Entrada Adulto")
       print("3-Entrada Adulto mayor")

       ent=int(input("selecciona una opcion : "))
       if (ent > 0 and ent <4):
            if ent==1:
                print("Entrada menores valor $2500")
                cantidad_entradas1=int(input("¿cuantas entradas deseas comprar? : "))
                totalcancel1= (cantidad_entradas1*val1)
                print(f"valor a cancelar {totalcancel1}")
                print("Deseas comprar mas entradas")
                sal=int(input("1-SI              2-No  : "))
                if sal==2:
                    sw=1
                if sal==1:
                    sw=0      
            if ent ==2:
                print("Entrada adulto valor $5000")
                cantidad_entradas2=int(input("¿cuantas entradas deseas comprar? : "))
                totalcancel2= (cantidad_entradas2*val2)
                print(f"valor a cancelar {totalcancel2}")
                print("Deseas comprar mas entradas")
                sal=int(input("1-SI              2-No  : "))
                if sal==2:
                    sw=1              
            if ent==3:
                print("Entrada Adulto mayou valor 1000")
                cantidad_entradas3=int(input("¿cuantas entradas deseas comprar?: "))
                totalcancel3=(cantidad_entradas3*val3)
                print(f"valor a cancelar {totalcancel3}")
                print("Deseas comprar mas entradas")
                sal=int(input("1-SI              2-No  : "))
                if sal==2:
                    sw=1
                os.system("cls")
       print("Deseas seguir con la compra ? ")
       cancel1=int(input("1-Si                 2-No  : "))
       if cancel1==2:
           sw=0
           os.system("cls")
           continue
       if cancel1==1:
           os.system("cls")
    except:
        print("opcion no valida , ingrese nuevamente ")


print("¿hoy es viernes?") 
dcto=int(input("1-Si                    2-No :  "))
if dcto==1:
    for contador2 in range(ent):
        contador2=(totalcancel1+totalcancel2+totalcancel3)-((totalcancel1-(10*totalcancel1//100))+(totalcancel2-(5*totalcancel2//100))+(totalcancel3))
        os.system("cls")
    print("*************ENTRADAS*************")
    print("*********************************")
    print(f"{cantidad_entradas1} Entradas Menores")
    print(f"{cantidad_entradas2} Entradas Adulto")
    print(f"{cantidad_entradas3} Entradas Adulto Mayor")
    print("*********************************")
    print(f"Subtotal             $ {totalcancel1+totalcancel2+totalcancel3}")
    print(f"Descuento            $ {contador2}")
    print("*********************************")
    print(f"Total a pagar      $ {(totalcancel1+totalcancel2+totalcancel3)- contador2}  ")
if dcto==2:
    os.system("cls")
    print("*************ENTRADAS*************")
    print("*********************************")
    print(f"{cantidad_entradas1} Entradas Menores")
    print(f"{cantidad_entradas2} Entradas Adulto")
    print(f"{cantidad_entradas3} Entradas Adulto Mayor")
    print("*********************************")
    print(f"Subtotal             $ {totalcancel1+totalcancel2+totalcancel3}")
    print(f"Descuento            $ {contador2}")
    print("*********************************")
    print(f"Total a pagar      ${totalcancel1+totalcancel2+totalcancel3}    ")

