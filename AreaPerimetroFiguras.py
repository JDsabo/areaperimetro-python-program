# Imports


import time
import math
from datetime import date

hoy = date.today()
print("La fecha de hoy es:", hoy)
print(time.strftime("La hora es: %I:%M:%S"))


# Funciones


def AreaTriangulo(b, h):
    result = (b * h) / 2
    return result


def PerimetroTriangulo(l1, l2, l3):
    result = l1 + l2 + l3
    return result


def AreaCuadrado(c1, c2):
    result = c1 * c2
    return result


def PerimetroCuadrado(t1, t2, t3, t4):
    result = t1 + t2 + t3 + t4
    return result


def AreaRectangulo(bas, alt):
    result = bas * alt
    return result


def PerimetroRectangulo(r1, r2):
    result = 2 * (r1 + r2)
    return result


def AreaRombo(d1, d2):
    result = (d1 * d2) / 2
    return result


def PerimetroRombo(dl):
    result = 4 * (dl)
    return result


def AreaCirculo(r1):
    result = (math.pi) * ((r1) * 2)
    return result


def PerimetroCirculo(r):
    result = 2 * (math.pi) * r
    return result


def AreaRomboide(b1, h1):
    result = b1 * h1
    return result


def PerimetroRomboide(lr1, lr2):
    result = 2 * (lr1) + 2 * (lr2)
    return result


def AreaTrapecio(ar, ba, ha):
    result = ha * ((ar + ba) / 2)
    return result


def PerimetroTrapecio(ox1, ox2, ox3, ox4):
    result = ox1 + ox2 + ox3 + ox4
    return result


# Logica


trigger1 = True

while trigger1:
    print(
        """
    1. Triangulo
    2. Cuadrado
    3. Rectangulo
    4. Rombo
    5. Circulo
    6. Romboide
    7. Trapecio
    8. Exit
    """
    )
    trigger1 = input("Seleccione una opcion: ")
    if trigger1 == "1":
        print("\n1. Area")
        print("2. Perimetro\n")
        trigger2 = input("Seleccione una accion para el Triangulo: ")
        if trigger2 == "1":
            b = float(input("Digite el valor de la base: "))
            h = float(input("Digite el valor de la altura: "))
            print("El Area del triangulo es: ", AreaTriangulo(b, h))
        elif trigger2 == "2":
            l1 = float(input("Digite el valor del primer lado: "))
            l2 = float(input("Digite el valor del segundo lado: "))
            l3 = float(input("Digite el valor del tercer lado: "))
            print("El Perimetro del triangulo es: ", PerimetroTriangulo(l1, l2, l3))
        break
    elif trigger1 == "2":
        print("\n1. Area")
        print("2. Perimetro\n")
        trigger3 = input("Seleccione una accion para el Cuadrado: ")
        if trigger3 == "1":
            c1 = float(input("Digite el valor del primer lado: "))
            c2 = float(input("Digite el valor del segundo lado: "))
            print("El Area del cuadrado es: ", AreaCuadrado(c1, c2))
        elif trigger3 == "2":
            t1 = float(input("Digite el valor del primer lado: "))
            t2 = float(input("Digite el valor del segundo lado: "))
            t3 = float(input("Digite el valor del tercer lado: "))
            t4 = float(input("Digite el valor del cuarto lado: "))
            print("El Perimetro del cuadrado es: ", PerimetroCuadrado(t1, t2, t3, t4))
        break
    elif trigger1 == "3":
        print("\n1. Area")
        print("2. Perimetro\n")
        trigger4 = input("Seleccione una accion para el Rectangulo: ")
        if trigger4 == "1":
            bas = float(input("Digite el valor de la base: "))
            alt = float(input("Digite el valor de la altura: "))
            print("El Area del rectangulo es: ", AreaRectangulo(bas, alt))
        elif trigger4 == "2":
            r1 = float(input("Digite el valor del primer lado vertical: "))
            r2 = float(input("Digite el valor del segundo lado horizontal: "))
            print("El Perimetro del rectangulo es: ", PerimetroRectangulo(r1, r2))
        break
    elif trigger1 == "4":
        print("\n1. Area")
        print("2. Perimetro\n")
        trigger5 = input("Seleccione una accion para el Rombo: ")
        if trigger5 == "1":
            d1 = float(input("Digite el valor de la primer diagonal: "))
            d2 = float(input("Digite el valor de la segunda diagonal: "))
            print("El Area del rombo es: ", AreaRombo(d1, d2))
        elif trigger5 == "2":
            dl = float(input("Digite el valor del algun lado: "))
            print("El Perimetro del rombo es: ", PerimetroRombo(dl))
        break
    elif trigger1 == "5":
        print("\n1. Area")
        print("2. Perimetro\n")
        trigger6 = input("Seleccione una accion para el Circulo: ")
        if trigger6 == "1":
            r = float(input("Digite el valor del radio: "))
            print("El Area del circulo es: ", AreaCirculo(r))
        elif trigger6 == "2":
            r1 = float(input("Digite el valor del algun lado: "))
            print("El Perimetro del circulo es: ", PerimetroCirculo(r1))
        break
    elif trigger1 == "6":
        print("\n1. Area")
        print("2. Perimetro\n")
        trigger7 = input("Seleccione una accion para el Romboide: ")
        if trigger7 == "1":
            b1 = float(input("Digite el valor de la base: "))
            h1 = float(input("Digite el valor de la altura: "))
            print("El Area del romboide es: ", AreaRomboide(b1, h1))
        elif trigger7 == "2":
            lr1 = float(input("Digite el valor del lado vertical: "))
            lr2 = float(input("Digite el valor del lado horiontal: "))
            print("El Perimetro del romboide es: ", PerimetroRomboide(lr1, lr2))
        break
    elif trigger1 == "7":
        print("\n1. Area")
        print("2. Perimetro\n")
        trigger8 = input("Seleccione una accion para el Trapecio: ")
        if trigger8 == "1":
            ar = float(input("Digite el valor de la base primaria: "))
            ba = float(input("Digite el valor de la base secundaria: "))
            ha = float(input("Digite el valor de la altura: "))
            print("El Area del trapecio es: ", AreaTrapecio(ar, ba, ha))
        elif trigger8 == "2":
            ox1 = float(input("Digite el valor del primer lado: "))
            ox2 = float(input("Digite el valor del segundo lado: "))
            ox3 = float(input("Digite el valor del tercer lado: "))
            ox4 = float(input("Digite el valor del cuarto lado: "))
            print(
                "El Perimetro del trapecio es: ", PerimetroTrapecio(ox1, ox2, ox3, ox4)
            )
        break
    elif trigger1 == "8":
        print("\nGracias. Hasta luego!\n")
        trigger1 = None
    else:
        print("\nNo es una opcion valida. Intente de nuevo.")
