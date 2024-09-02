def promedio (*numeros):
    return sum(numeros)/len(numeros)

x = promedio (4,5,6)
print(x)

def area(**dato):
    '''
    Calcula el area de una figura geometrica
    y la imprime en pantalla
    '''
    #Si el diccionario tiene una clave llamada 'figura' evalua el valor de la clave
    if dato['figura'] == 'Rectangulo':
        return (dato['base']*dato['altura'])
    elif dato['figura'] == 'Triangulo':
        return (dato['base']*dato['altura']/2)
    elif dato['figura'] == 'Circulo':
        return (3.1415193*dato['radio']**2)
    else:
        print('Figura desconocida')

#Ejemplo llamada a funcion con return
triangulo = area(figura='Triangulo', base=10, altura = 8)
print(f'El area del triangulo es: {triangulo}')
circulo = area(figura='Circulo', radio = 10, color = 'Rojo')
print(f'El area del circulo es: {circulo}')
dodecagono = area(figura = 'Dodecagono', lado = 10)
print(f'El area del dodecagono es: {dodecagono}')

# Recursividad de funciones en python

 