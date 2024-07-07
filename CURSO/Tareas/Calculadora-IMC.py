#Tarea Modulo 1 Calculadora IMC

# Solicitar y validar nombre
while True:
    nom = input("Introduce tu nombre: ")
    if nom and nom.isalpha():
        break
    else:
        print("Por favor ingresa un nombre valido.")

# Solicitar y validar apellidos
while True:
    ape_pat = input("Introduce tu apellido paterno: ")
    if ape_pat and ape_pat.isalpha():
        break
    else:
        print("Por favor ingresa un apellido válido.")

while True:
    ape_mat = input("Introduce tu apellido materno: ")
    if ape_mat and ape_mat.isalpha():
        break
    else:
        print("Por favor ingresa un apellido válido.")

# Solicitar y validar edad
while True:
    edad = input("Introduce tu edad: ")
    if edad:
        try:
            edad = int(edad)
            break
        except ValueError:
            print("Por favor ingresa una edad válida")
    else:
        print("La edad no puede estar vacía.")

# Solicitar y validar peso
while True:
    peso = input("Introduce tu peso en kilogramos: ")
    if peso:
        try:
            peso = float(peso)
            break
        except ValueError:
            print("Por favor ingrese un peso válido.")
    else:
        print("El peso no puede estar vacío.")

# Solicitar y validar estatura
while True:
    est = input("Introduce tu estatura en metros: ")
    if est:
        try:
            est = float(est)
            break
        except ValueError:
            print("Por favor ingrese una estatura válida.")
    else:
        print("La estatura no puede estar vacía.")

# Calcular IMC
imc = peso / (est ** 2)

# Mostrar resultados
print("\nDatos ingresados:")
print(f"Nombre: {nom}")
print(f"Apellido Paterno: {ape_pat}")
print(f"Apellido Materno: {ape_mat}")
print(f"Edad: {edad}")
print(f"Peso: {peso} kg")
print(f"Estatura: {est} m")
print(f"Índice de Masa Corporal (IMC): {imc:.2f}")
