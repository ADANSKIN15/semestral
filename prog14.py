def prog14():
    print('---------------------------')
    print('>>> TRAPECIO PARALELO <<<')
    print('---------------------------\n')

    print('>> ingrese longitud A:')
    B = float(input('=>'))
    print()
    print('>> ingrese longitud B:')
    b = float(input('=>'))
    print()
    print('>>ingrese altura:')
    H = float(input('=>'))
    print()

    AREA_trape = ((b + B)/2)*H
    PERIMETRO_TRAPE = B+b+H+H
    print()

    print(f'El area de un trapacesio es:*{AREA_trape}* y su perimetro es:*{PERIMETRO_TRAPE}*')
