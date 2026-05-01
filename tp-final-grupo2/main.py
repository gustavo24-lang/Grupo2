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
dniCliente=int(input("Ingrese su numero de DNI: ")) #dniCliente y numTelCliente son int para evitar que el usuario meta letras. 

#verifica que dniCLiente no tenga más de 8 carácteres
while len(str(dniCliente))>8:
    print("ERROR-- El DNI no puede tener más de 8 digitos, vuelva a ingresar. ")
    dniCliente=int(input("Ingrese su numero de DNI: ")) 
    
dirCliente=input("Ingrese su dirección:  ").title()
numTelCliente=int(input("Ingrese su numero de teléfono: "))

#verifica que numTel no tenga más de 15 carácteres 
while len(str(numTelCliente))>15 :
    print("ERROR-- El numero de telefono no puede tener más ni menos de 15 digitos, vuelva a ingresar. ")
    numTelCliente=int(input("Ingrese su numero de teléfono: "))

print("------MENÚ------")
print("""
    ROYAL PAWS
      
    SERVICIOS
LAVADO: $6.000
CORTE: $5.000
FULL: $10.000

    PRODUCTOS
JUGUETE SQUEAKY: $2.500
SHAMPOO: $3.000
     COMUN 
        SHAMPOO 2 EN 1
     SHAMPOO PARA PIELES ATOPICAS
      
CHALECOS DE ABRIGO PERRO( XS, S, M, L, XL ): $5.000
      
    DESCUENTOS Y PROMOCIONES
FULL + JUGUETE SQUEAKY: 15%
LAVADO + CHALECO: 8%
UNA COMPRA MAYOR A $10.000 ENVIO GRATIS
      
    RECARGOS
RAZA PELIGROSA: %8
MASCOTA EN MAL ESTADO: %20  

    
      ENVIOS
ENVIOS A CABA: $1500
ENVIOS A Prov. BUENOS AIRES: $8000

    MEDIOS DE PAGO
TARJETA DE CREDITO/DEBITO
EFECTIVO
TRANSFERIENCIA 
      
      """)
print("""SELECCION 1 PARA SERVICIOS, 2 PARA PRODUCTOS""")
ciclo=int(input("La opción que desee: "))
while ciclo <1 or ciclo>2:
    ciclo=int(input("ERROR - Ingrese una opcion valida entre 1 y 2: "))

ContLavado = 0
SumLavado = 0
ContCorte = 0
SumCorte = 0
ContFull = 0
SumFull = 0 
ContJuguete = 0
SumJuguete = 0
ContShampoo = 0
SumShampoo = 0 
ContAbrigo =0
SumAbrigo =0 
shampooComun = 0
shampoo2en1 = 0
shampooAtopico = 0
while ciclo !=-1: 
    if ciclo== 1: 
        print("✔ Ha seleccionado servicios  ")
        print("ingrese que servicio quiere 1 para lavado, 2 para corte, 3 para full")
        OpcServicios= int(input("ingrese una opcion de servicio: "))
        while OpcServicios <1 or OpcServicios>3:
            print("ERROR - ingrese una opcion valida 1 al 3:")
            OpcServicios= int(input("ingrese una opcion de servicio: "))

        while OpcServicios != -1:

            if OpcServicios ==1:
                print("✔ usted eligio lavado")
                ContLavado +=1
                SumLavado += 6000
            elif OpcServicios == 2:
                print("✔ Usted eligio corte ")
                ContCorte +=1
                SumCorte +=5000
            else:
                ContFull +=1
                SumFull += 10000 
            print("si quiere volver a elegir un servicio")
            print("ingrese que servicio quiere 1 para lavado, 2 para corte, 3 para full o -1 para finalizar")
            OpcServicios= int(input("ingrese una opcion de servicio: "))
            
    if ciclo== 2: 

        print("✔ Ha seleccionado productos ")
        print("ingrese 1 para jueguete squeaky, 2 para shampoo , 3 para chaleco de abrigo canino")

        OpcProductos = int(input("ingrese una opcion: "))

        while OpcProductos <1 or OpcProductos >2:
            OpcProductos = int(input(" ERROR - ingrese una opcion valida (1, 2 o 3): "))

        while OpcProductos != -1 :

            if OpcProductos==1 :
                print(" ✔ selecciono un juguete!!")
                ContJuguete +=1
                SumJuguete += 2500
            elif OpcProductos ==2:
                opcshampoo = int(input("que shampoo quiere 1 para shampoo comun, 2 para 2 en 1, 3 para atopico: "))
                while opcshampoo <1 or opcshampoo>3:
                 opcshampoo = int(input("ERROR - Ingrese un numero valido del 1 al 3: "))
                if opcshampoo== 1:
                    print("✔ usted eligio shampoo comun")
                    shampooComun +=1
                elif opcshampoo ==2:
                    print("✔ usted eligio shampo 2 en 1")
                    shampoo2en1 +=1
                else:
                    print("✔ usted eligio shampoo")
                    shampooAtopico +=1
                ContShampoo +=1
                SumShampoo += 3000 
            else:
                ContAbrigo +=1
                SumAbrigo += 5000
            print("Siquiere volver a comprar un producto")
            print("ingrese 1 para jueguete squeaky, 2 para shampoo , 3 para chaleco de abrigo canino o -1 para finalizar")

            OpcProductos = int(input("ingrese una opcion: "))
    print("""SELECCION 1 PARA SERVICIOS, 2 PARA PRODUCTOS""")
    ciclo=int(input("quiere volver a elegir selecione una opcion (-1 para finalizar): "))
