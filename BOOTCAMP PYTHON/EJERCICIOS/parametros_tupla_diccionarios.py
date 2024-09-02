# Parametros de tipo tula, *args

def promedio (*numeros):
    '''Recibe un solo parametro de tipo tupla,
    e imprime su promedio
    '''
    promedio = sum(numeros)/len(numeros)
    print('El promedio es:', promedio)

promedio(4)
promedio(4, 5, 6)
promedio(1, 2, 3, 4, 5, 6, 7, 8, 9)

def es_numero(titulo, *serie):
    '''
    Imprime un titulo
    Verifica si el caracter en el parametro de 
    tipo tupla es un numero o no
    '''
    print(titulo)
    for i in serie:
        if type(i) == int or i.isdigit():
            print(f'{i} es numero')
        else:
            print(f'{i} no es numero')

es_numero('Numeros', '1', '2', '3')        
es_numero('Letras', 'a', 'b', 'c')

nombre = 'Mezcla'
lista_varios = ['a', '2', 3, 'f', 5]
es_numero(nombre, *lista_varios)


#Parametros de tipo **kwargs

def area(**dato):
    '''
    Calcula el area de una figura geometrica
    y la imprime en pantalla
    '''
    #Si el diccionario tiene una clave llamada 'figura' evalua el valor de la clave
    if dato['figura'] == 'Rectangulo':
        print(dato['base']*dato['altura'])
    elif dato['figura'] == 'Triangulo':
        print(dato['base']*dato['altura']/2)
    elif dato['figura'] == 'Circulo':
        print(3.1415193*dato['radio']**2)
    else:
        print('Figura desconocida')

area(figura = 'Triangulo', base = 10, altura = 5)
area(figura = 'Circulo', radio = 10, color = 'Rojo')
area(figura = 'Dodecagono', lado = 10)







