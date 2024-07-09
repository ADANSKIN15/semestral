def prog12():
    print('---------------------------------')
    print('<<<COMVERTIDOR DE TEMPERATURA>>>')
    print('---------------------------------\n')
    
    print('>>> Celsius a  Fahrenheit:')
    C = float(input('='))
    fahrenheit = (C * 1.8) + 32
    print(f'>>> tienes,{fahrenheit} grados fahrenheit de temperatura \n')

    print('>>>celsius a kelvin:')
    c = float(input('='))
    kelvin = 273 + c
    print(f'ahora tienes,{kelvin} grados kelvin de temperatura')


