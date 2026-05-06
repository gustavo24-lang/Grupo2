
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
while len(str(numTelCliente))>15  or len(str(numTelCliente))<15 :
    print("ERROR-- El numero de telefono no puede tener más ni menos de 15 digitos, vuelva a ingresar. ")
    numTelCliente=int(input("Ingrese su numero de teléfono: "))


print("------MENÚ------")
print("""
    ROYAL PAWS
      
    SERVICIOS
LAVADO: $6.000
CORTE: $5.000
FULL: $10.000

print("""BIENVENIDO A ROYAL PAWS
        Tenemos los siguientes descuentos y promociones
            FULL + JUGUETE SQUEAKY: 15%
            LAVADO + CHALECO: 8%
            UNA COMPRA MAYOR A $10.000 ENVIO GRATIS

        Se aplicará un recargo bajo las siguientes condiciones:
            RAZA PELIGROSA: %8
            MASCOTA EN MAL ESTADO: %20  


        Los precios de envío son:
            ENVIOS A CABA: $1500
            ENVIOS A Prov. BUENOS AIRES: $8000

        Aceptamos los siguientes medios de pago:
            TARJETA DE CREDITO/DEBITO
            EFECTIVO
            TRANSFERIENCIA 
            
      Para ver los servicios disponibles ingrese 1:
      Para ver los productos disponibles ingrese 2:
      """)
ciclo=int(input("Igrese la opción que desee: "))
while ciclo <1 or ciclo>2:
    ciclo=int(input("ERROR - Ingrese una opcion valida entre 1 y 2: "))


#contadores
ContLavado = 0
ContCorte = 0
ContFull = 0
ContJuguete = 0
ContShampoo = 0
ContAbrigo =0
shampooComun = 0
shampoo2en1 = 0
shampooAtopico = 0

#sumadores 
SumLavado = 0
SumCorte = 0
SumFull = 0 
while ciclo>0: 
    #opción 1 = servicios
    if ciclo== 1: 
        
        print("""✔ Ha seleccionado servicios  
              Estos son los servicios disponibles y sus precios: 
                    1.LAVADO: $6.000
                    2.CORTE: $5.000
                    3.FULL: $10.000
            """)
        
        print("ingrese el numero del servicio que desea.")
        OpcServicios= int(input("ingrese una opcion de servicio: "))
        #valida OpcServicios
        while OpcServicios <1 or OpcServicios>3:
            print("ERROR - ingrese una opcion valida 1 al 3:")
            OpcServicios= int(input("ingrese una opcion de servicio: "))
        #--LAVADO--
        if OpcServicios ==1:
            print("usted eligio lavado")
            ContLavado +=1
            SumLavado += 6000
        #--CORTE--
        elif OpcServicios == 2:
            print("Usted eligio corte ")
            ContCorte +=1
            SumCorte +=5000
        #--FULL--
        else:
            ContFull +=1
            SumFull += 10000 
            
    print("Seleccione 2 para --x cosa--")
    if ciclo== 2: 
        #agregar un submenú para talles de chaleco
        print("""✔ Ha seleccionado productos
                  Estos son los productos disponibles
                    1.JUGUETE SQUEAKY: $2.500
                    2.SHAMPOO: $3.000
                         COMUN 
                        SHAMPOO 2 EN 1
                         SHAMPOO PARA PIELES ATOPICAS

                    3.CHALECOS DE ABRIGO PERRO( XS, S, M, L, XL ): $5.000 
                """)
        print("ingrese 1 para jueguete squeaky, 2 para shampoo , 3 para chaleco de abrigo canino")

        OpcProductos = int(input("ingrese una opcion: "))

#Había un >2 en lugar de un >3 en el veri
        while OpcProductos <1 or OpcProductos >3:
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
    
    ciclo=int(input("Quiere volver a elegir selecione una opcion (-1 para finalizar): "))
   
    print("--Factura de servicio Royal Paws--")
    print("------------------------------------------")

    print("""ROYAL PAWS
            Av. Belgrano y Av. Pueyrredón,
            CUIT:14253647586,
            Tel: 11325648
            RoyalPaws@gmail.com 
                """)

    print("------------------------------------------")

    print("Cliente: ,", nombreCliente,
          "Mascota: ", nombreMascota, 
          "DNI Cliente: ", dniCliente,
          "Dirección: ", dirCliente, 
          "Numero Teléfono: ", numTelCliente)

    print("------------------------------------------")
    print("Servicios contratados")
    print(ContLavado, " Servicios de lavado", ContCorte, "Servicios de corte ", ContFull, " Servicios 'full'  ")
    print("El precio total a pagar por los SERVICIOS es de ", SumCorte+SumFull+SumLavado)
    
    print(" ")
    
    print("Productos comprados")
    print("Compró ", ContJuguete, " Juguetes ", ContShampoo, " Shampoos (De cualquiera de las 3 variedades) ", ContAbrigo, " Abrigos (de cualquiera de los talles)")
    print("El total a pagar por los productos es de ", SumAbrigo+SumJuguete+SumShampoo)
    
    print("El total a pagar es de: ", TotPagar)
    
    print("------------------------------------------")
    print("El precio final es de: ")
