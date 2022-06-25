#Main
#Pedimos al usuario los parametros y verificando que sean válidos
while True:
    nombre = input('Ingrese su Nombre: ').title() #le damos mayúsculas a la primer letra del nombre/s
    edad = input('Ingrese su edad: ')
    try:
        edad = int(edad)
        if edad == 0:
            print("Ingresa una edad válida.")
            continue
    except:
        print('La edad debe ser un número entero mayor a 0.')
        continue
    break

edad_anterior = edad - 1
edad_posterior = edad + 1

#Agregamos un poco de complejidad para que el mensaje sea mas acertado.
if edad == 2:
    print(f'{nombre}: El año pasado tenías {edad_anterior} año y el próximo año cumplirás {edad_posterior} años.')
elif edad > 2:
    print(f'{nombre}: El año pasado tenías {edad_anterior} años y el próximo año cumplirás {edad_posterior} años.')
else:
    print(f'{nombre}: El año pasado aún no habías nacido y el próximo año cumplirás {edad_posterior} años.')
exit()