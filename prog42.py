def prog42():
    print('______________________________________________')
    print('    identifica si es positivo o negativo')
    print('        se detiene solo si es positivo')
    print('______________________________________________\n')

    stop = 0
    can = int(input('ingrese un numero: '))

    print()

    while stop == 0 :
        if can < 0 :
            print('el numero es negativo ')
            top = int(input('intentelo de nuevo: '))
            
            if top > 0 :
                print(f'el numero {top} es positivo')
                break
                
