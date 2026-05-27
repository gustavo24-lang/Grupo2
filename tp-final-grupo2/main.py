total_servicios_global = 0
total_productos_global = 0
cantidad_clientes = 3

nombreCliente=input("Ingrese su nombre: "). title()
while len(nombreCliente) < 2 or len(nombreCliente)>= 20:
    print("ERROR-- Nombre del cliente demasiado corto o largo. Vuelva a ingresarlo. ")
    nombreCliente=input("Ingrese su nombre: "). title()

nombreMascota=input("Ingrese el nombre de su mascota: ").title()
while len(nombreMascota) < 2 or len(nombreMascota) >= 20:#NUEVO
    print("ERROR-- Nombre de mascota demasiado largo o corto. Vuelva a ingresarlo")
    nombreMascota=input("Ingrese el nombre de su mascota: ").title()

dniCliente=int(input("Ingrese su numero de DNI: ")) #dniCliente y numTelCliente son int para evitar que el usuario meta letras. 
#verifica que dniCLiente no tenga más de 8 carácteres
while len(str(dniCliente)) != 8: #Modificado para evitar que vayan con un nro menor o mayor al lim.
    print("ERROR-- El DNI no puede tener más de 8 digitos, vuelva a ingresar. ")
    dniCliente=int(input("Ingrese su numero de DNI: ")) 
    
    
dirCliente=input("Ingrese su dirección:  ").title()
#verificamos que la dirección no tenga menos de 3 carácteres ni más de 30
while 3 > len(int(dirCliente)) < 30: #NUEVO
    print("ERROR -- La dirección tiene muy pocos o demasiados caracteres, vuelva a ingresarla.")     
    dirCliente=input("Ingrese su dirección:  ").title()


numTelCliente=int(input("Ingrese su numero de teléfono: "))
#verifica que numTel no tenga más de 15 carácteres 
while len(str(numTelCliente)) != 15 :
    print("ERROR-- El numero de telefono no puede tener más ni menos de 15 digitos, vuelva a ingresar. ")
    numTelCliente=int(input("Ingrese su numero de teléfono: "))

    dirCliente = input("Ingrese su direccion: ").title()
    numTelCliente = int(input("Ingrese su numero de telEfono: "))


print("""BIENVENIDO A ROYAL PAWS
        Tenemos los siguientes descuentos y promociones
            FULL + JUGUETE SQUEAKY: 15%
            LAVADO + CHALECO: 8%
            UNA COMPRA MAYOR A $10.000: ENVIO GRATIS

        Se aplicará un recargo bajo las siguientes condiciones:
            RAZA PELIGROSA: 8%
            MASCOTA EN MAL ESTADO: 20%

        Los precios de envIo son:
            ENVIOS A CABA: $1500
            ENVIOS A Prov. BUENOS AIRES: $8000

        Aceptamos los siguientes medios de pago:
            TARJETA DE CREDITO/DEBITO
            EFECTIVO
            TRANSFERENCIA

        Para ver los servicios disponibles ingrese 1:
        Para ver los productos disponibles ingrese 2:
    """)

    ciclo = int(input("Ingrese la opcion que desee: "))
    while ciclo < 1 or ciclo > 2:
        ciclo = int(input("ERROR - Ingrese una opcion valida entre 1 y 2: "))

#sumadores 
SumLavado = 0
SumCorte = 0
SumFull = 0 
SumServicios=SumLavado+SumCorte+SumFull
SumJuguete = 0
SumAbrigo = 0
SumShampoo = 0
SumProd = SumJuguete + SumAbrigo + SumShampoo

TotPagar = SumServicios + SumShampoo
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
        #agregar un submenú para talles de chaleco
        print("""✔ Ha seleccionado productos
                  Estos son los productos disponibles
                    1.JUGUETE SQUEAKY: $2.500
                    2.SHAMPOO: $3.000
                         COMUN 
                        SHAMPOO 2 EN 1
                         SHAMPOO PARA PIELES ATOPICAS""")

        if ciclo == 2:
            eligioProductos = True  
            print("""✔ Ha seleccionado PRODUCTOS
                  Estos son los productos disponibles:
                    1. JUGUETE SQUEAKY:              $2.500
                    2. SHAMPOO:                      $3.000
                         - Común
                         - 2 en 1
                         - Para pieles atopicas
                    3. CHALECO DE ABRIGO (XS-XL):   $5.000
            """)
            OpcProductos = int(input("Ingrese 1 para Juguete, 2 para Shampoo, 3 para Chaleco: "))
            while OpcProductos < 1 or OpcProductos > 3:
                OpcProductos = int(input("ERROR - Ingrese una opcion válida (1, 2 o 3): "))

            while OpcProductos != -1:
                if OpcProductos == 1:
                    print("✔ Selecciono un JUGUETE SQUEAKY")
                    ContJuguete += 1
                    SumJuguete += 2500

                elif OpcProductos == 2:
                    opcshampoo = int(input("¿QuE shampoo quiere? 1-Común  2-2en1  3-Atopico: "))
                    while opcshampoo < 1 or opcshampoo > 3:
                        opcshampoo = int(input("ERROR - Ingrese un número válido del 1 al 3: "))
                    if opcshampoo == 1:
                        print("✔ Usted eligio SHAMPOO COMÚN")
                        shampooComun += 1
                    elif opcshampoo == 2:
                        print("✔ Usted eligio SHAMPOO 2 EN 1")
                        shampoo2en1 += 1
                    else:
                        print("✔ Usted eligio SHAMPOO PARA PIELES AToPICAS")
                        shampooAtopico += 1
                    ContShampoo += 1
                    SumShampoo += 3000

                else:
                    print("✔ Selecciono un CHALECO DE ABRIGO")
                    ContAbrigo += 1
                    SumAbrigo += 5000

                print("Ingrese 1 para Juguete, 2 para Shampoo, 3 para Chaleco o -1 para finalizar productos:")
                OpcProductos = int(input("Ingrese una opcion: "))

            # ---- Pregunta de envIo ----
            if eligioProductos:
                print("¿DESEA ELEGIR UN METODO DE ENVIO? (SI/NO)")
                opcEnvios = input("Ingrese su respuesta: ").upper()
                while opcEnvios != "SI" and opcEnvios != "NO":
                    opcEnvios = input("ERROR - Ingrese SI o NO: ").upper()

                if opcEnvios == "SI":
                    print("""
                    Opciones de envIo:
                        1) ENVIO A CABA:              $1.500
                        2) ENVIO A Prov. BUENOS AIRES: $8.000
                    """)
                    Envios = int(input("Ingrese una opcion (1 o 2): "))
                    while Envios < 1 or Envios > 2:
                        Envios = int(input("ERROR - Ingrese 1 o 2: "))
                    if Envios == 1:
                        tipoEnvio = 1
                        costoEnvio = 1500
                        print("✔ Seleccionaste ENVIO A CABA - $1.500")
                    else:
                        tipoEnvio = 2
                        costoEnvio = 8000
                        print("✔ Seleccionaste ENVIO A PROV. BUENOS AIRES - $8.000")
                else:
                    print("✔ Sin envIo, ¡gracias!")
                direccenvio=input("Ingrese la direccion de envio: ")

        print("SELECCIONE 1 PARA SERVICIOS, 2 PARA PRODUCTOS o -1 para finalizar:")
        ciclo = int(input("Ingrese una opcion: "))
        while ciclo != 1 and ciclo !=2 and ciclo != -1:
            print("Error")
            ciclo = int(input("Ingrese una opcion: "))

    # =============================================
    # CÁLCULO DE SUBTOTALES Y DESCUENTOS/RECARGOS
    # =============================================
    subtotalServicios = SumLavado + SumCorte + SumFull
    subtotalProductos = SumJuguete + SumShampoo + SumAbrigo
    subtotalSinEnvio  = subtotalServicios + subtotalProductos

    descuento = 0
    nombreDescuento = "Ninguno"

    # Descuento FULL + JUGUETE: 15%
    if ContFull > 0 and ContJuguete > 0:
        descuento = subtotalSinEnvio * 0.15
        nombreDescuento = "FULL + JUGUETE SQUEAKY (15%)"
    # Descuento LAVADO + CHALECO: 8%
    elif ContLavado > 0 and ContAbrigo > 0:
        descuento = subtotalSinEnvio * 0.08
        nombreDescuento = "LAVADO + CHALECO (8%)"

    # EnvIo gratis si la compra supera $10.000
    envioGratis = False
    if subtotalSinEnvio > 10000 and costoEnvio > 0:
        envioGratis = True
        costoEnvio = 0

    # Recargos
    print("¿La mascota es de RAZA PELIGROSA? (SI/NO)")
    esRazaPeligrosa = input("Ingrese su respuesta: ").upper()
    while esRazaPeligrosa != "SI" and esRazaPeligrosa != "NO":
        esRazaPeligrosa = input("ERROR - Ingrese SI o NO: ").upper()

    print("¿La mascota está en MAL ESTADO? (SI/NO)")
    esMalEstado = input("Ingrese su respuesta: ").upper()
    while esMalEstado != "SI" and esMalEstado != "NO":
        esMalEstado = input("ERROR - Ingrese SI o NO: ").upper()

    recargo = 0
    nombreRecargo = "Ninguno"
    if esRazaPeligrosa == "SI" and esMalEstado == "SI":
        recargo = subtotalSinEnvio * 0.28   # se acumulan
        nombreRecargo = "Raza peligrosa (8%) + Mal estado (20%)"
    elif esRazaPeligrosa == "SI":
        recargo = subtotalSinEnvio * 0.08
        nombreRecargo = "Raza peligrosa (8%)"
    elif esMalEstado == "SI":
        recargo = subtotalSinEnvio * 0.20
        nombreRecargo = "Mascota en mal estado (20%)"

    TotPagar = subtotalSinEnvio - descuento + recargo + costoEnvio
    total_servicios_global = total_servicios_global + subtotalServicios
    total_productos_global = total_productos_global + subtotalProductos

    print("")
    print("========================================")
    print("       FACTURA - ROYAL PAWS             ")
    print("========================================")
    print("  Av. Belgrano y Av. Pueyrredon")
    print("  CUIT: 14-25364758-6")
    print("  Tel: 11-3256-4800")
    print("  RoyalPaws@gmail.com")
    print("========================================")
    print("  Cliente:   ", nombreCliente)
    print("  Mascota:   ", nombreMascota)
    print("  DNI:       ", dniCliente)
    print("  Direccion: ", dirCliente)
    print("  Direccion de envio: ", direccenvio)
    print("  TelEfono:  ", numTelCliente)
    print("========================================")

    print("  ** SERVICIOS **")
    if ContLavado > 0:
        print("  ", ContLavado, "x Lavado          $", int(SumLavado))
    if ContCorte > 0:
        print("  ", ContCorte, "x Corte           $", int(SumCorte))
    if ContFull > 0:
        print("  ", ContFull, "x Full            $", int(SumFull))
    if subtotalServicios == 0:
        print("   (Sin servicios contratados)")
    print("   SUBTOTAL SERVICIOS:    $", int(subtotalServicios))

    print("  ** PRODUCTOS **")
    if ContJuguete > 0:
        print("  ", ContJuguete, "x Juguete Squeaky  $", int(SumJuguete))
    if ContShampoo > 0:
        print("  ", ContShampoo, "x Shampoo          $", int(SumShampoo))
        if shampooComun > 0:
            print("      - Común:        ", shampooComun)
        if shampoo2en1 > 0:
            print("      - 2 en 1:       ", shampoo2en1)
        if shampooAtopico > 0:
            print("      - Atopico:      ", shampooAtopico)
    if ContAbrigo > 0:
        print("  ", ContAbrigo, "x Chaleco          $", int(SumAbrigo))
    if subtotalProductos == 0:
        print("   (Sin productos comprados)")
    print("   SUBTOTAL PRODUCTOS:    $", int(subtotalProductos))

    print("========================================")
    print("  SUBTOTAL:              $", int(subtotalSinEnvio))
    print("  Descuento (", nombreDescuento, "): -$", int(descuento))
    print("  Recargo  (", nombreRecargo, "): +$", int(recargo))

    if tipoEnvio == 0:
        print("  EnvIo:                 Sin envIo")
    elif envioGratis:
        print("  EnvIo:                 GRATIS (compra mayor a $10.000)")
    elif tipoEnvio == 1:
        print("  EnvIo a CABA:          $", int(costoEnvio))
    else:
        print("  EnvIo a Prov. Bs.As.:  $", int(costoEnvio))

    print("========================================")
    print("  TOTAL A PAGAR:         $", int(TotPagar))
    print("========================================")
    print("  ¡Gracias por elegirnos! ")
    print("========================================")

if total_lavados >= total_cortes and total_lavados >= total_full:
    servicio_top = "Lavado"
elif total_cortes >= total_lavados and total_cortes >= total_full:
    servicio_top = "Corte"
else:
    servicio_top = "Full"

# Determinar Producto más vendido
if total_juguetes >= total_shampoos and total_juguetes >= total_abrigos:
    producto_top = "Juguete Squeaky"
elif total_shampoos >= total_juguetes and total_shampoos >= total_abrigos:
    producto_top = "Shampoo"
else:
    producto_top = "Chaleco de Abrigo"

# Cálculos de porcentajes y promedios
total_general = total_servicios_global + total_productos_global
if total_general > 0:
    porcentaje_servicios = (total_servicios_global * 100) / total_general
    porcentaje_productos = (total_productos_global * 100) / total_general
else:
    porcentaje_servicios = 0
    porcentaje_productos = 0

promedio_por_cliente = total_general / cantidad_clientes

# =============================================
# APARTADO DE ESTADISTICAS FINAL
# =============================================
print("")
print("========================================")
print("       ESTADISTICAS GENERALES           ")
print("========================================")
print("  Promedio de gasto por cliente: $", int(promedio_por_cliente))
print("  Total Servicios:  $", int(total_servicios_global), "(", int(porcentaje_servicios), "%)")
print("  Total Productos:  $", int(total_productos_global), "(", int(porcentaje_productos), "%)")
print("  --------------------------------------")
print("  SERVICIO MÁS VENDIDO: ", servicio_top)
print("  PRODUCTO MÁS VENDIDO: ", producto_top)
print("========================================")
