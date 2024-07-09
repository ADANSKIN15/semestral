def prog40():
    import random

    print('************************')
    print('*   Adivina el número  *')
    print('************************\n')

    c = random.randrange(1,10)
    stop = 0

    while stop == 0 :
        can = int(input('ingrese un numero: '))
        
        if can < c :
            print('!es mas alto!')
            
        if can > c :
            print('!es mas bajo!')
               
        if can == c :
            print('!correcto!')
            break
            
                        

