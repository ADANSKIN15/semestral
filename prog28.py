def prog28():
    print('************************************* ')
    print('determinar el primer año de un siglo ')
    print('************************************* ')

    print()

    año = int(input("Ingrese un año: "))

    print()

    if año % 100 == 0 and año % 400 == 0:
        print(f"{año} es el primer año de un siglo.")
    elif año % 100 != 0 and año % 4 == 0:
        print(f"{año} es el primer año de un siglo.")
    else:
        print(f"{año} no es el primer año de un siglo.")
        
