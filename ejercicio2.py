import os
from datetime import datetime
'''
Según lo que comprendo del enunciado, 
el usuario sería el que maneja la caja del restaurante,
ingresaría los datos correspondientes.
Solo los clientes (mis amigos y yo) le pasaríamos como dato
el porcentaje de propina.
Por lo tanto, se asume que el usuario (cajero) ingresará todos los datos
al programa y el mismo imprimirá por pantalla la factura/ticket
con el detalle deseado.
Para este ejercicio voy a armar una especie de menu para darle un poco
mas de complejidad
'''

#Metodo para limpiar pantalla según el sistema operativo del usuario
def limpioPantalla():
    #windows
    if os.name == 'ce' or os.name == 'nt' or os.name == 'dos':
        os.system('cls')
    #linux
    elif os.name == 'posix':
        os.system('clear')    
    return

def menuPrincipal():
    limpioPantalla()
    menu = f'''\
***************************************
*        Menu: Facturar pedido        *
***************************************
 1. Subtotal del pedido: $ {subtotal}
 2. Cantidad de personas: {cantPersonas}
 3. Porcentaje Impuesto: % {impuesto}
 4. Porcentaje Propina: % {propina}

 5. Imprimir factura
 
 9. Limpiar valores
 0. Salir
--------------------------------------- 
'''
    print(menu)
    return

def imprimirFactura():
    limpioPantalla()
    fecha = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    montoImpuesto = subtotal * impuesto / 100
    montoPropina = subtotal * propina / 100 # Calculo la propina sobre el total sin impuestos
    total = round(subtotal + montoImpuesto + montoPropina, 2)
    totalPorPersona = round(total / cantPersonas, 2)
    factura = f'''\
***************************************
*         Detalle de factura          *
***************************************
 Fecha: {fecha}
 
 Subtotal del pedido:   $ {subtotal}
 Impuesto aplicado:     $ {montoImpuesto}
 Propina:               % {montoPropina} 
 
 Total:              $ {total}
 Total por persona:  $ {totalPorPersona}

---------------------------------------
''' 
    print(factura)
    return


#MAIN

#inicializo variables
subtotal = ''
impuesto = ''
cantPersonas = ''
propina = ''

#ciclo para siempre hasta que se ingrese 0.
while True:
    menuPrincipal()
    opcion = input('Ingrese opción: ')
    if opcion == '0':
        print("Saliendo del programa...")
        break
    elif opcion == '1':
        try:
            subtotal = float(input('Ingrese el subtotal del pedido: '))
            subtotal = round(subtotal,2) #redondeo y formateo a 2 decimales
        except:
            input('Monto ingresado no inválido, presione Enter para continuar...')
        continue
    elif opcion == '2':
        try:
            cantPersonas = int(input('Ingrese la cantidad de personas: '))
        except:
            input('Cantidad ingresada inválida, presione Enter para continuar...')
        continue
    elif opcion == '3':
        try:
            impuesto = float(input('Ingrese el porcentaje del impuesto a aplicar: '))
            impuesto = round(impuesto,2) #redondeo y formateo a 2 decimales
        except:
            input('Valor ingresado inválido, presione Enter para continuar...')
        continue
    elif opcion == '4':
        try:
            propina = float(input('Ingrese el porcentaje de la propina: '))
            propina = round(propina,2)
        except:
            input('Valor ingresado inválido, presione Enter para continuar...')
        continue
    elif opcion == '5':
        if subtotal == '' or cantPersonas == '' or impuesto == '' or propina == '':
            print('Verifique los datos ingresados, falta alguno para imprimir la factura')
            input('Presione Enter para continuar...')
            continue
        else:
            imprimirFactura()
            input('Presione Enter para continuar...')
            continue
    elif opcion == '9':
        subtotal = ''
        impuesto = ''
        cantPersonas = ''
        propina = ''
        continue
    else:
        input('Ingrese una opción válida, presione Enter para continuar... ')
        continue
exit()