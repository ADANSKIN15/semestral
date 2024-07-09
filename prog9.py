def prog9():
    print('---------------------------')
    print('  > CALCULO DEL SALARIO <')
    print('---------------------------\n')

    print('>> horas mensual:')
    HM = float(input())

    print('>>>precio de la hora:')
    PH = float(input())

    print('>>>horas extras:')
    HE = float(input())

    print('>>>precio de horas extra:')
    PE = float(input())

    print()

    monto_hex = HE * PE
    monto_total = HM * PH + monto_hex

    print()

    print(f'>>> monto de hora extra es :{monto_hex}$')


    print()

    print(f'>>> monto total del mes es : {monto_total}$')



    