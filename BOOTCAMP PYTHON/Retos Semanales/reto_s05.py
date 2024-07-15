#Reto de la semana 5 Bootcamp Fundamentos Python

print('Este programa solicita al usuario 2 años para devolver la diferencia entre ellos segun sea el caso')

#Ciclo while para solicitar la info al usuario considerando que los datos sean numericos y no sean los mismos.
while True:
    año_actual = input('Por favor ingresa el año actual (YYYY): ')
    if año_actual and año_actual.isnumeric():
        año_actual = int(año_actual)
    else:
        print('Ingresa un año válido')
        continue

    año_random = input('Por favor ingresa un año cualquiera (YYYY): ')
    if año_random and año_random.isnumeric():
        año_random = int(año_random)
    else:
        print('Ingresa un año válido')
        continue
    
    if año_actual != año_random:
        break
    else:
        print('Ingresaste 2 años iguales, por favor, ingresa valores diferentes.')

#Calcular la diferencia entre los años ingresados.

calculo_año = abs(año_actual - año_random)

#Impresion del calculo de acuerdo al valor ingresado (singular/plural)
if calculo_año == 1:
    if año_actual < año_random:
        print('Aun falta %d año' % calculo_año)
    else:
        año_actual > año_random
        print('Ha pasado %d año' % calculo_año)
else:
    if año_actual < año_random:
        print('Aun faltan %d años'%calculo_año)
    else:
        año_actual > año_random
        print('Han pasado %d años'%calculo_año)
