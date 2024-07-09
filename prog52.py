def prog52():
    print('----------------------------------')
    print('Determinar si un número es primo')
    print('----------------------------------\n')


    can =int(input("ingrese nuemro:"))
    print()
    top = 0
    for i in range(1, can + 1):
        if can % i == 0:
            top += 1

    if top == 2:  
        print(f"El número {can} es primo")
    else:
        print(f"El número {can} no es primo")

    
