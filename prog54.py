def prog54():
    print('==========================================')
    print('    Dibujar un triángulo de asteriscos    ')
    print('==========================================\n')

    n = int(input("Ingrese un numero entero: "))


    for i in range(n+ 1):
        espacio = n - 1
        print("   " * espacio +  "*" * i  )            
                              
