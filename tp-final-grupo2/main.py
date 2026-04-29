#pedir datos al usuario.
"""Datos a solicitar al cliente:  

    Nombre 

    nombre de mascota 

    DNI 
    
    Dirección 

    Número de teléfono 
"""
nombreCliente=input("Ingrese su nombre: "). title()
nombreMascota=input("Ingrese el nombre de su mascota: ").title()
dniCliente=int(input("Ingrese su numero de DNI: "))
"""

todavía no vimos las palabras reservadas que usé para el condicional

while len(str(dniCliente))>8:
    print("ERROR-- El DNI no puede tener más de 8 digitos, vuelva a ingresar. ")
    dniCliente=int(input("Ingrese su numero de DNI: ")) 
"""

dirCliente=input("Ingrese su dirección:  ").title()
numTelCliente=int(input("Ingrese su numero de teléfono: "))
"""

    while len(str(dniCliente))>15:
    print("ERROR-- El numero de telefono no puede tener más de 15 digitos, vuelva a ingresar. ")
    numTelCliente=int(input("Ingrese su numero de teléfono: "))
"""
ciclo=int(input("Ingrese un numero>0 para iniciar el sistema: "))

while ciclo>0: 
    
    print("------MENÚ------")
    #parte de gustavo
    
    print("Seleccione 1 para --x cosa--")
    if ciclo== 1: 
        print("Ha seleccionado --opción-- ")
    print("Seleccione 2 para --x cosa--")
    if ciclo== 2: 
        print("Ha seleccionado --opción-- ")
    print("Seleccione 3 para --x cosa--")
    if ciclo== 3: 
        print("Ha seleccionado --opción-- ")
    print("Seleccione 4 para --x cosa--")
    if ciclo== 4: 
        print("Ha seleccionado --opción-- ")
    print("Seleccione 5 para --x cosa--")   
    if  ciclo== 5: 
        print("Ha seleccionado --opción-- ")
    ciclo=int(input("Ingrese un numero>0 para iniciar el sistema: "))
