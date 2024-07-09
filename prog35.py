def prog35():
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('        tarifa del kilometraje       ')
    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')

    d = float(input(' ingrese kilometro: '))

    print()

    ex = 2.00
    pa = 2.50

    a = d * pa
    e = ((d - 10) * ex)
    total = 25 + e

    if 1 <= d <= 10 :
        print(f'precio a pagar: {a}')
        
            
    elif d > 10 :
        total = 25 + e
        print('los 10 primeros kilometro son: 25 $')
        print(f'su tarifa despues de 10km es:{e}')
        print(f'la tarifa es :{total}')
    
        
            
    