def prog30():
    print('--------------------------')
    print(' categoria del trabajador')
    print('--------------------------')

    print()

    print('si son meses agrege (0.) y la cantidad de mes.')
    a = float(input('ingrese cuanto años tiene trabajando: '))

    if 0.1 <= a <=2 :
        print('usted es junior')
        
    elif 2<= a <= 5:
        print('usted es semi-senior')
        
    elif a >= 5 :
        print('usted es senior')
