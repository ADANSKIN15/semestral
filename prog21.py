def prog21():
    print('---------------------------------------')
    print('  Determina si tienes mas de 5 letras')
    print('---------------------------------------')

    print()

    palabra = input('ingrese una palabra:')
    N = len(palabra)
    print()
    
    if N > 5:
        print('-> tine mas de 5 letras')
        
    else:
        print('-> insuficiente')
        
