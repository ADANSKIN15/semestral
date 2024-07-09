def prog44():
    print('++++++++++++++++++++++++')
    print('  Decimal a Binario')
    print('++++++++++++++++++++++++\n')


    num = int(input('Ingrese un número entero: '))

    binario = bin(num)[2:]

    print(f'En binario de {num} es : {binario}')
