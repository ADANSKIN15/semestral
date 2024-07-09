def prog23():
    print('====================================================')
    print('precio final con descuento del 10% despues de 100$')
    print('====================================================\n')


    P = float(input('ingrese el precio:'))

    if  P < 100 :
        print(f'su precio es :{P}')
        
    elif P >= 100 :
        d = P *(10/100)
        pd = P - d
        print(f'su precio con 10% de descuento es :{pd} dolares')
        
        
        
