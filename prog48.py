def prog48():
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('  Contar vocales en una cadena ')
    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')

    tex = str(input('ingrese un texto: '))
    vocal = 'AaEeIiOoUu'
    x = 0

    print()

    for i in tex :
        if i in vocal:
            x += 1
            
    print()
    print('el texto tiene',x,'vocales')
