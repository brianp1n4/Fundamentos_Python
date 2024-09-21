numerador = 10
denominador = 0
cadena ='3'
numerico = 5

# print(numerador / denominador)
# print(cadena + numerico)

try :
    print(numerador / denominador)
except (ZeroDivisionError, TypeError):
    print('Ha ocurrido un error')    


print('Fin del programa')    

