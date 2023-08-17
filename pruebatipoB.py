import os
menu2=True
pt=12000
pp=14000
pa=17000
menu1=True
cont1=0
cont2=0
cont3=0
dcto=0
cance=0
while menu1:
    print("****bienvenido a Pizzeria Douc****")
    print("Elija una de las opciones disponibles: ")
    print("1-Pizza Tradicional")
    print("2-Pizza Peperoni")
    print("3-Pizza All Carnes")
    print("4-Salir")
    try:
        opcion=int(input("Que deseas pedir : "))
        if(opcion >0 and opcion <5) :
            if opcion ==1:
                print("Usted ingreso opcion 1")
                pedido=int(input("¿cuantas pizzas quieres?"))
                print(f"total a pagar:{pt*pedido}\n")
                print("Quieres ordenar algo mas? ")
                cont1=(pt*pedido)

                mp=int(input("1-Si              2-No :"))
                if mp ==1:
                    menu1=True
                if mp==2:
                    menu1=False
                    os.system("cls")
            if opcion ==2:
                print("Usted ingreso opcion 2")
                pedido=int(input("¿cuantas pizzas quieres?"))
                print(f"total a pagar:{pp*pedido}") 
                print("Quieres ordenar algo mas? ")
                cont2=(pp*pedido)
                mp=int(input("1-Si              2-No :"))
                if mp ==1:
                    menu1=True
                if mp==2:
                    menu1=False
                    os.system("cls")
            if opcion ==3:
                print("Usted ingreso opcion 3")
                pedido=int(input("¿cuantas pizzas quieres?"))
                print(f"total a pagar:{pa*pedido}")
                print("Quieres ordenar algo mas? ")
                cont3=(pa*pedido)
                mp=int(input("1-Si              2-No :" ))
                if mp ==1:
                    menu1=True
                if mp==2:
                    menu1=False
                    os.system("cls")
            if opcion ==4:
                print("hasta luego")
                menu1=False
            for acumulador in range (pedido):
             acumulador=cont1+cont2+cont3
        print("Deseas seguir con la compra ? ")
        cancel1=int(input("1-Si                 2-No  : "))
        if cancel1==2:
           menu1=True
           os.system("cls")
           continue
        if cancel1==1:
           os.system("cls")
    except:
        print("Ocurrio un error")
print(f"total a cancelar : {acumulador} ")
while menu2:
    print("Selecciona tu jornada : ")
    print("1-Diurno")
    print("2-Vespertino")
    print("3-Administrativo")
    try:
        dcto=int(input("tu jornada es : "))
        if(opcion >0 and opcion <4) :
            if dcto ==1:
             print("Descuento para jornada diurna 12%")
            menu2=False
            if dcto ==2:
             print("Descuento para jornada vespertina 10%")
             menu2=False
            if dcto ==3:
             print("Administrativo no corresponde descuento")
            menu2=False
    except:
        print("algo salio mal , vuelve a intentarlo")

os.system("cls")

print("*************Pizzeria Duoc**************")
if cont1 > 0:
   print(f"Pizza Tradicional:   $ {cont1}")
if cont2 > 0:
   print(f"Pizza Peperoni:      $ {cont2}")
if cont3 > 0:
   print(f"Pizza All Carnes:    $ {cont3}")
print("*****************************************")
print(f"Subtotal:               $ {acumulador} ")
if dcto==1:
   des=12
   print("Descuento:              12%")
   d=acumulador*des//100
if dcto==2:
   des=10
   print("Descuento:              10%")
   d=acumulador*des//100
if dcto==3:
   des=0
   print("Descuento:              0%")
   d=acumulador*des//100
print("******************************************")
print(f"Total a pagar:            $ {acumulador-d} ")

print("**********Gracias por su compra***********")
