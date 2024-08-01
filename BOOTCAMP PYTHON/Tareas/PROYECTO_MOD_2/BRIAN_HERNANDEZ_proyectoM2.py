#PRESENTACION DEL PROGRAMA
opcion = input("Seleccione el número del programa a ejecutar \n \t 1. LONGUITUD DE UNA FRASE \n \t 2. ENCUENTRA EL CUADRANTE \n")
if opcion.isdigit() == False:
    print("Debes ingresar el número del programa a ejecutar para continuar")
else:
    if opcion == "1":
    #1. LONGUITUD DE UNA FRASE
    #Solicitamos la palabra al usuario
        while True:
            palabra=input("\n################### \n\n Ingrese una palabra de 4 a 8 letras: ")

            #Se guarda la cantidad de caracteres de la palabra ingresada por usuario
            tamaño=len(palabra)

            #Se valida que la palabra contenga solo letras
            if palabra.isalpha() == False:
                print("No ingreses números, espacios o simbolos")
                continue #Regresar al inicio del while, solicitar de nuevo input

            #Se valida palabra dentro del rango de 4 a 8    
            elif tamaño >= 4 and tamaño <= 8:
                print("La palabra es correcta. Fin del programa")
                break #Se detiene while, palabra es correcta

            elif tamaño < 4:
                print(f"La palabra es muy corta. Solo tiene {tamaño} letras.")
            else:
                print(f"La palabra es muy larga. Tiene {tamaño} letras.")
    else:
        #2. ENCUENTRA EL CUADRANTE
        #Solicitamos coordenadas al usuario
        print("\t\nPOR FAVOR SOLO INGRESE VALORES ENTEROS\n")
        #Iteracion para solicitar X
        while True:
            try:
                #Se solicita valor de X al usuario
                valor_x = int(input("Ingrese la coordenada X: \n"))
            except ValueError:
                #Error en caso de input diferente de un numero
                print("Por favor, ingrese un número entero.")
                continue #Solicitar de nuevo valor_x

            #Validar que el valor de x se adiferente de cero        
            if valor_x == 0:
                print("La coordenada X no puede ser 0")
                continue #regresar al inicio de while para solicitar x nuevamente

            #Iteracion para solicitar Y
            while True:
                try:
                    #Se solicita Y al usuario
                    valor_y = int(input("Ingrese la coordenada Y: \n"))
                except ValueError:
                    #Error en caso de input diferente de numero
                    print("Por favor, ingrese un número entero.")
                    continue #Solicitar de nuevo Y
                #Validar que el valor de Y se adiferente de cero   
                if valor_y == 0:
                    print("La coordenada Y no puede ser 0")
                else:
                    break #Finalizar bucle cuando se tienen coordenadas validas

            # Determinar en qué cuadrante se encuentra el punto
            if valor_x > 0 and valor_y > 0:
                print("La coordenada está en el cuadrante I")
            elif valor_x < 0 and valor_y > 0:
                print("La coordenada está en el cuadrante II")
            elif valor_x < 0 and valor_y < 0:
                print("La coordenada está en el cuadrante III")
            elif valor_x > 0 and valor_y < 0:
                print("La coordenada está en el cuadrante IV")
            break

        

                    