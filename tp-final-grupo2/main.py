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
while len(str(dniCliente))>15:
    print("ERROR-- El numero de telefono no puede tener más de 15 digitos, vuelva a ingresar. ")
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
ciclo=int(input("La opción que desee: "))

while ciclo>0: 
    
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
