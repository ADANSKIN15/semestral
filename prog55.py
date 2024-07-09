def prog55():
    print('=====================================')
    print('           imprime texto             ')
    print('=====================================\n')
    texto = str(input('escriba un texto: '))
    num = int(input('ingrese la cantidad de repeticiones: '))
    import time
    for i in range(1,num +1,1):
        print(texto)
        time.sleep(1)
