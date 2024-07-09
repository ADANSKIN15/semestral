def prog39():
    print('==============================')
    print('  Sumar dígitos de un número  ')
    print('============================== \n')


    F = int(input('ingrese un numero: '))

    suma = 0

    print()

    while F > 0 :
        suma += (F % 10)
        F //= 10
        
    print(f'la suma de sus digitos es:{suma}')
