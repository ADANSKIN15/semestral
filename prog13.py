def prog13():
    print('------------------------------')
    print('  >>> AREA DE UN CIRCULO <<< ')
    print('------------------------------\n')
    
    print('>> ingrese el radio')
    R = float(input('->'))
    print()
    
    print('>> ingrese la altura')
    H = float(input('->'))
    print()

    ac =  3.14 *(R**2)
    vc =  3.14 * ((R**2 )* H )

     
    print(f'El area del circulo es:{ac} y el volumen del cilindro es :{vc}') 
