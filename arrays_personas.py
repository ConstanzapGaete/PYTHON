import os
persona = ['1-7','Alan','Patricio','Brito','Delgado']

grupo = [
    ['1-7','Alan','Patricio','Brito','Delgado'],
    ['2-8','Maria','Antonia','Delgado','Perez'],
    ['3-9','Jose','Francisco','Brito','Martinez']
]

# con len() obtenemos el largo de un array
# print(len(grupo))

# obtener el nombre del array persona
# for i in range(len(persona)):
#     if i == 1:
#         print(persona[i])

def buscar_por_rut(rut_persona):
    for i in range(len(grupo)):
        for j in range(len(grupo[i])):
            if grupo[i][j] == rut_persona:
                return grupo[i]

def imprimir_persona(array_persona):
    print(f"Rut: \t\t\t {array_persona[0]}")
    print(f"Primer Nombre: \t\t {array_persona[1]}")
    print(f"Segundo Nombre: \t {array_persona[2]}")
    print(f"Apellido Paterno: \t {array_persona[3]}")
    print(f"Apellido Materno: \t {array_persona[4]}")
    input("")

# imprimir_persona(buscar_por_rut('1-7'))

def agregar_persona():
    os.system("cls")
    print("----- AGREGAR PERSONA ------")
    rut = input("Indique su rut > ")
    primer_nombre = input("Indique su nombre > ")
    segundo_nombre = input("Indique su Segundo nombre > ")
    apellido_paterno = input("Indique su apellido paterno > ")
    apellido_materno = input("Indique su apellido materno > ")

    grupo.append([rut, primer_nombre, segundo_nombre, apellido_paterno, apellido_materno])
    

# ejecutar codigo
agregar_persona()

os.system("cls")
print(grupo)