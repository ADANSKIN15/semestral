import prog1 ,prog2 ,prog3 ,prog4 ,prog5 ,prog6 ,prog7 ,prog8 ,prog9 ,prog10 ,prog11 ,prog12 ,prog13 ,prog14 ,prog15
import prog16 ,prog17 ,prog18 ,prog19 ,prog20 ,prog21 ,prog22 ,prog23 ,prog24 ,prog25 ,prog26 ,prog27 ,prog28 ,prog29
import prog30 ,prog31 ,prog32 ,prog33 ,prog34 ,prog35 ,prog36 ,prog37 ,prog38 ,prog39 ,prog40 ,prog41 ,prog42 ,prog43
import prog44 ,prog45 ,prog46 ,prog47 ,prog48 ,prog49 ,prog50 ,prog51 ,prog52 ,prog53 ,prog54 ,prog55

def LOBBY ():
    while True:
        print("\n=======😄=============😄=============😄=== LOBBY ===😄=============😄=================😄=========\n")
        print('1).sumar                   2).cant/precio/impuesto       3).area/triangulo rectangulo')
        print('------------------------------------------------------------------------------------------------------')
        print('4).perimetro/rectangulo    5).área/trapecio              6).volumen/prisma')
        print('------------------------------------------------------------------------------------------------------')
        print('7).formulas                8).pies/metros/pies           9).salario       ')
        print('------------------------------------------------------------------------------------------------------')
        print('10).pago/producto         11).IMC                       12).Celsius/Fahrenheit           ')
        print('------------------------------------------------------------------------------------------------------')
        print('13).área/circulo          14).trapecio/paralelo         15).hipotenusa/triangulo ')
        print('------------------------------------------------------------------------------------------------------')
        print('16).área/poentagono reg.  17).pos/neg/cero              18).adolecente?  ')
        print('------------------------------------------------------------------------------------------------------')
        print('19).múltiplo?             20).vocal?                    21).5 letras?    ')
        print('------------------------------------------------------------------------------------------------------')
        print("22).clasif/edad           23).10%/100$                  24).1/100      ")
        print('------------------------------------------------------------------------------------------------------')
        print('25).letra/numero          26).mayor/menor               27).salario neto    28).año/siglo')
        print('------------------------------------------------------------------------------------------------------')
        print("28).año/siglo             29).triagulo/valido           30).catego/trabajdor    ")
        print('------------------------------------------------------------------------------------------------------')
        print("31).IMC/peso              32).tipo/licencia             33).divisible(3,5)         ")
        print('------------------------------------------------------------------------------------------------------')
        print("34).nomb/corto,largo      35).tarifa/kilometraje        36).1/100(while)        ")
        print('------------------------------------------------------------------------------------------------------')
        print('37).1/dado3(while)        38).sumar/dado(while)         39).sumar/digitos(while)')
        print('------------------------------------------------------------------------------------------------------')
        print('40).adivina/número(while) 41).tabla/mult(while)         42).para/positivo(while) ')
        print('------------------------------------------------------------------------------------------------------')
        print("43).cont/digitos(while)   44).decimal/binario(while)    45).cajero/automático(while)")
        print('------------------------------------------------------------------------------------------------------')
        print("46).tabla/multip( for )   47).pares1/100( for )         48).contar/vocal/str( for )  ")
        print('------------------------------------------------------------------------------------------------------')
        print('49).10/1( for )           50).impares/dado( for )       51).sumer/numero/NNN( for )')
        print('------------------------------------------------------------------------------------------------------')
        print("52).num/primo( for )      53).Celsius/Fahrenheit( for ) 54).dibuja/triangulo( for ) ")
        print('------------------------------------------------------------------------------------------------------')
        print('55).repite/texto( for )')
        print('------------------------------------------------------------------------------------------------------/n')
        print("x. Salir \n")
        voto = input("=> Elige una opción: ")
        print()
        
    

        match voto:
            case "1":
                prog1.prog1()
                break
            case "2":
                prog2.prog2()
                break
            case "3":
                prog3.prog3()
                break
            case "4":
                prog4.prog4()
                break
            case "5":
                prog5.prog5()
                break
            case "6":
                prog6.prog6()
                break
            case "7":
                prog7.prog7()
                break
            case "8":
                prog8.prog8()
                break
            case "9":
                prog9.prog9()
                break
            case "10":
                prog10.prog10()
                break
            case "11":
                prog11.prog11()
                break
            case "12":
                prog12.prog12()
                break
            case "13":
                prog13.prog13()
                break
            case "14":
                prog14.prog14()
                break
            case "15":
                prog15.prog15()
                break
            case "16":
                prog16.prog16()
                break
            case "17":
                prog17.prog17()
                break
            case "18":
                prog18.prog18()
                break
            case "19":
                prog19.prog19()
                break
            case "20":
                prog20.prog20()
                break
            case "21":
                prog21.prog21()
                break
            case "22":
                prog22.prog22()
                break
            case "23":
                prog23.prog23()
                break
            case "24":
                prog24.prog24()
                break
            case "25":
                prog25.prog25()
                break
            case "26":
                prog26.prog26()
                break
            case "27":
                prog27.prog27()
                break
            case "28":
                prog28.prog28()
                break
            case "29":
                prog29.prog29()
                break
            case "30":
                prog30.prog30()
                break
            case "31":
                prog31.prog31()
                break
            case "32":
                prog32.prog32()
                break
            case "33":
                prog33.prog33()
                break
            case "34":
                prog34.prog34()
                break
            case "35":
                prog35.prog35()
                break
            case "36":
                prog36.prog36()
                break
            case "37":
                prog37.prog37()
                break
            case "38":
                prog38.prog38()
                break
            case "39":
                prog39.prog39()
                break
            case "40":
                prog40.prog40()
                break
            case "41":
                prog41.prog41()
                break
            case "42":
                prog42.prog42()
                break
            case "43":
                prog43.prog43()
                break
            case "44":
                prog44.prog44()
                break
            case "45":
                prog45.prog45()
                break
            case "46":
                prog46.prog46()
                break
            case "47":
                prog47.prog47()
                break
            case "48":
                prog48.prog48()
                break
            case "49":
                prog49.prog49()
                break
            case "50":
                prog50.prog50()
                break
            case "51":
                prog51.prog51()
                break
            case "52":
                prog52.prog52()
                break
            case "53":
                prog53.prog53()
                break
            case "54":
                prog54.prog54()
                break
            case "55":
                prog55.prog55()
                break


                
            case "x":
                print("Saliendo...")
                break
            case _:
                print("Opción no válida, intenta de nuevo.")
                

if __name__ == "__main__":
    LOBBY()
