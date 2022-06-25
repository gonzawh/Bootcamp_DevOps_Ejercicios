import os #importo lib para acceder a las funciones del OS
import re #importo para manejar expresiones regulares

'''
Ejercicio 1.

El enunciado no nos dice de limitar al usuario a ingresar cierta cantidad de caracteres.
Tampoco nos dice que tipo de caracteres se deben ingresar (alfanuméricos, solo letras, caracteres especiales).
Lo que sí nos dice es que debemos devolver el resultado en 'Letras'.
Entonces:
Daremos libertad al usuario y haremos las suguientes validaciones:
    1) Formatearemos la cadena, removiendo caracteres especiales y numeros
    2) Validaremos la cantidad de letras e imprimremos lo que pide el enunciado según lo posible
    3) Si no podemos imprimir nada como resultado, informaremos al usuario que necesita ingresar al menos una letra en su cadena
Ej: 
    Input: 'Hola como estas?'
    Resultado: 
            Primeras 2 letras: Ho
            Primeras 3 letras: Hol
            Ultimas 2 letras: as
            Ultima letra: s
    Input: 'Hi!'
    Resultado:
        Primeras 2 letras: Hi
        Ultimas 2 letras: Hi
        Ultima letra: i
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
#Metodo para devolver solo las letras usando expresiones regulares
def formateoCadena(cadena):
    cadena = re.sub(r'[^a-zA-Z]','',cadena)
    return cadena

#MAIN
limpioPantalla()
#ciclo para siempre hasta que se ingrese 0.
while True:
    #recibo input del usuario como string
    cadena = input('\nIngrese una cadena de caracteres, para salir ingrese "0": ')
    limpioPantalla()
    #si es 0, rompo el ciclo y finalizo el programa
    print('Cadena Ingresada:', cadena)
    if cadena == '0':
        print('Fin del programa. ¡Hasta luego!')
        break
    print('-'*40,'\n')
    cadena = formateoCadena(cadena)
    #si la cadena tiene 3 o mas caracteres
    if len(cadena) >= 3:
        print('Primeras 2 letras:', cadena[:2])
        print('Primeras 3 letras:', cadena[:3])
        print('Ultimas 2 letras:', cadena[-2:])
        print('Ultima letra:', cadena[-1:])
    #si son 2 caracteres
    elif len(cadena) == 2:
        print('Primeras 2 letras:', cadena[:2])
        print('Ultimas 2 letras:', cadena[-2:])
        print('Ultima letra:', cadena[-1:])
    #si es 1 solo caracter
    elif len(cadena) == 1:       
        print('Ultima letra:', cadena[-1:])
    #si no ingresó valor
    else:
        print('Cadena incorrecta, debe contener al menos una letra.')
exit()
    
