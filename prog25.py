def prog25():
    print('=======================================')
    print('reconoce si es una letra o numero')
    print('======================================= \n')

    L = input('igrese letra o numero:')

    print()

    if L.isalpha():
        print('=> Es una letra')

    elif L.isdigit():
        print('=> Es un numero')

    else:
        print('=> No es ni letra ni numero')
      
