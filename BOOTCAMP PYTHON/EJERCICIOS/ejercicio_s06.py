#Ejercicio 1

print("Impares menores a 10")
x = 1
while x <= 10:
    print(x)
    x += 2

#Ejercicio 2

factorial = 5
contador = factorial - 1
while contador > 0 :
    factorial *= contador
    contador -= 1
    print("El factorial de 5 es", factorial)

#ejercicio 3 FOR

for i in 1, 2, 3 :
    print(i)

for i in range(3) :
    print(i)

for i in ["Ale","Ivan", "Montse", "Luis", "Rafa", "Luca"] :
    print(i)

for i in "Hola Mundo" :
    if i == "M" :
        pass
    else :
        print(i, end=" ")




