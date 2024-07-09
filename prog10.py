def prog10():
    print('------------------------')
    print('  PAGO DE UN PRODUCTO')
    print('------------------------\n')

    print('ingrese el precio del producto:')
    P = float(input())

    print('ingrese descuento:')
    D = int(input())

    print('ingrese impuesto:')
    I = int(input())

    P_D = P * (D/100)
    PD = P - P_D
    P_I = P * (I/100)
    PT = PD + P_I

    print(f'su descuento es:{PD}')

    print(f'precio total es:{PT}')
        
