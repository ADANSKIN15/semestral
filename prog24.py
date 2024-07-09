def prog24():
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('        numeros en rango de 1 al 100            ')
    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< \n')

    n = float(input('numero a determinar: '))
    print()

    if 1 <= n <= 100 :
        print('=> esta entre el 1 y 100')
        print('-------------------------')

    if n > 100 :
        print('  => fuera de rango')
        print('--------------------')
