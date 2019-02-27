#Calculadora

while True:
    print("Bienvenido a la Calcuphydora");
    print("1. Suma");
    print("2. Resta");
    print("3. Multiplicación");
    print("4. División");
    print("5. Exponenciación");
    print("6. Salir");
    elección= int(input("Introduzca su elección: "));
    if (elección>=1 and elección<=5):
        print("Introduzca dos números: ");
        num1 = int(input());
        num2 = int(input());
        if elección == 1:
            res = num1 + num2;
            print("Resultado = ", res);
        elif elección == 2:
            res = num1 - num2;
            print("Resultado = ", res);
        elif elección == 3:
            res = num1 * num2;
            print("Resultado = ", res);
        elif elección == 4:
            res = num1 / num2;
            print("Resultado = ", res);
        elif elección == 5:
            res = num1 ** num2;
            print("Resultado = ", res);
    elif elección == 6:
        break
    else:
        print("Entrada incorrecta...");
