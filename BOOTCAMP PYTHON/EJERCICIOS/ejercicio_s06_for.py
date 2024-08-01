#Iterar sobre el rango de 2 a 99
for i in range(2,100) : 
    primo = True #validacion de que es primo
    
    # Comenzamos a verificar si el número i es divisible por algún número j en el rango de 2 a i-1
    for j in range(2,i) :
        if i == j :             
            # Si i es igual a j, no hacemos nada y salimos del bucle
            break
        elif i % j == 0 :
            # Si i es divisible por j, entonces no es primo
            primo = False
            break   # Salimos del bucle ya que encontramos un divisor y sabemos que no es primo
        else:
            # Si no es divisible, continuamos verificando con el siguiente j
            continue
    # Si primo sigue siendo True después de verificar todos los posibles divisores, entonces es primo   
    if primo == True :
        print(i, end=" ")
