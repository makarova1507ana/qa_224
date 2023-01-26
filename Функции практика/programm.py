# ПОльзователь выбирает фигуру
# (квадрат(прямоугольник), круг, треугольник)
# выбирает параметр вычисления (площадь или перемитр)
from shapes_functions import* # подключаем все функции
shape = input("Выберете фигуру: "
              "\n1. квадрат(прямоугольник), "
              "\n2. круг, "
              "\n3. треугольник")
parametr = input("Выберете параметр: "
                 "\n1. Площадь, "
                 "\n2. Периметр, ")
if shape == "1":
    a = int(input("сторона a: "))
    b = int(input("сторона b: "))
    if parametr == "1":
        print("S прямогульниа = ", quadrilateral_S(a, b))
    elif parametr == "2":
        print("P прямогульника = ", quadrilateral_P(a, b))
    else:
        print("нет такой команды")
elif shape == "2":
    r = int(input("радиус r: "))
    if parametr == "1":
        print("S круга = ", circle_S(r))
    elif parametr == "2":
        print("P круга = ", circle_P(r))
    else:
        print("нет такой команды")
elif shape == "3":
    a = int(input("сторона a: "))
    b = int(input("сторона b: "))
    c = int(input("сторона c: "))
    if parametr == "1":
        print("S треугольник = ", triangle_S(a, b, c))
    elif parametr == "2":
        print("P треугольник = ", a+b+c)
    else:
        print("нет такой команды")
else:
    print("нет такой фигуры")