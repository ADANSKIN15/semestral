def prog46():
    print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    print('        TABLAS DE MULTIPLICAR       ')
    print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n')

    can = int(input('tabla de multiplicar de: '))
    print()

    for x in range(1,11) :
        mul = x * can
        print(can,'X',x,'=',mul)
