def solicitar_contraseña():
    while True:
        contraseña = input("Ingrese una contraseña que inicie con un número: ")
        if contraseña and contraseña[0].isdigit():
            return contraseña
        else:
            print("La contraseña debe comenzar con un número. Inténtelo de nuevo.")

def verificar_contraseña(contraseña):
    intentos = 3
    while intentos > 0:
        verificacion = input("Ingrese nuevamente la contraseña para verificar: ")
        if verificacion == contraseña:
            print("Contraseña verificada correctamente.")
            return True
        else:
            intentos -= 1
            print(f"Contraseña incorrecta. Le quedan {intentos} intentos.")
    print("Ha cometido tres errores. El programa se cerrará.")
    return False

def main():
    contraseña = solicitar_contraseña()
    if verificar_contraseña(contraseña):
        print("Acceso concedido.")
    else:
        print("Acceso denegado. Programa cerrado.")

if __name__ == "__main__":
    main()
