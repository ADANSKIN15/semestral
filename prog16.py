def prog16():
    print('--------------------------------')
    print('  AREA DE UN PENTAGONO REGULAR')
    print('-------------------------------- \n')
    
    print('ingrese su lado:')
    L = float(input('>'))
       
    print('ingrese la apotema:')
    AP = float(input('>'))


    PERIME = 5*L
    AREA = (PERIME * AP) / 2


    print(f'El AREA de un pentagono es: {AREA} Y su PERIMETRO es: {PERIME}')
