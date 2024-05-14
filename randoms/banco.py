while True:
    A = int(input("Ingrese el número de cuenta: "))
    B = float(input("Ingrese el saldo al inicio del mes: "))
    C = float(input("Ingrese el total de todos los artículos cargados por el cliente en el mes: "))
    D = float(input("Ingrese el total de todos los créditos aplicados a la cuenta del cliente en el mes: "))
    E = float(input("Ingrese el límite del crédito permitido: "))

    nuevo_saldo = B + C - D

    if nuevo_saldo > E:
        print(f"El cliente con el número de cuenta {A} ha excedido el límite de crédito.")
    else:
        print("El cliente no ha excedido el límite de crédito.")