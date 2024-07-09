def prog22():
    print('******************************')
    print('  clasificacion de edad ')
    print('****************************** \n')


    E = int(input(' ingrese su edad:'))
    print()

    if 0 <= E <= 12 :
        print('-> infantil')
        
    elif 13 <= E <= 19 :
        print('-> adolecente')
        
    elif 20 <= E <= 59 :
        print('-> adulto')
        
    elif E > 60 :
        print(' -> adulto mayor')


