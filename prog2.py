def prog2():
    print('😨 PRECIO, 🤔 CANTIDAD, 😢 IMPUESTO \n \n \n ')
    print('CANTIDAD:')
    c = int(input())
    print()
    print('PRECIO:')
    P = float(input())
    print()
    print('IMPUESTO:')
    I = float(input())
    print()
    p1 = c * P
    p2 = p1 * (I / 100)
    p3 = p1 + p2
    print()
    print(p3)
