def prog45():
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print('$       cajero automático        $ ')
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')

    print('solo tiene 3 intentos\n')
    nombre = str(input('ingrese su nombre: '))
    stop = 0

    while stop < 3 :
        can = int(input('ingrese pin: '))
        stop += 1
        
        if can != 1234 :
            print('incorrecto')
            print('intento',stop,'\n')
            
        
        if can == 1234 :
            print('bienvenido',nombre)
            break
        
        if stop == 3:
            print('!! cuenta bloqueada !!')
            

     

            
