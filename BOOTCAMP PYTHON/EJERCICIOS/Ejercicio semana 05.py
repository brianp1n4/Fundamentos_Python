import random
 
lista_nombres = ['Roxana','Graciela','Juan','Jonathan','Luis']
nombre_secreto = random.choice(lista_nombres)
 
numero_de_intentos = 2
 
while numero_de_intentos > 0:
    print('Intentos Restantes: ', numero_de_intentos)
    resultado = input('Dime en quién estoy pensando: ')
    if resultado == nombre_secreto:
        print('Ganaste')
        break
    else:
        print('Vuélvelo a intentar')
    numero_de_intentos = numero_de_intentos - 1
 
print('Fin del juego')