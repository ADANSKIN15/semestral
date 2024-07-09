def prog29():
    print('--------------------------------------')
    print('  determina si un triangulo es valido ')
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n')

    la = float(input('ingrese lado A: '))
    lb = float(input('ingrese lado B: '))
    lc = float(input('ingrese lado C: '))

    print()

    if la + lb > lc:
        print('es valido')

    elif lc + lb > la:
        print('es valido')
        
    elif lc + la > lb:
        print(' es valido')
           
    else:
        print('no es valido')
