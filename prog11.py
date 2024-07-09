def prog11():
    print('---------------------------')
    print('  ***CALCULADORA DE IMC*** ')
    print('---------------------------\n')
    
    print('>>>ingrese su altura en mts:')
    A = float(input('->'))
    print()

    print('>>>ingrese su peso en kg:')
    P = float(input('->'))
    print()

    IMC  = P/(A*A)

    print('->',IMC)
