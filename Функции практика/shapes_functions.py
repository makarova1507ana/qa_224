# проверка корректности сторон
def is_valid_side(*sides):# * -плавающее кол-во параметров
    for side in sides:
        if side <= 0:
            return False
    return True


# # сумма произвольного кол-во чисел
# # 3,5,5
# # 13
# # 1,1
# # 2
# # 5
# # 5
# def sum_numbers(*numbers):# * -плавающее кол-во параметров
#     summ = 0
#     for number in numbers:
#         summ += number
#     return summ
#
# print(sum_numbers(1,1,1,1))
# print(sum_numbers(1,1))
# print(sum_numbers(1))

# проверка существование треугольник
# если a+b>c (соотвественно для остальных)


#(квадрат(прямоугольник)
# s
def quadrilateral_S(a, b):
    if is_valid_side(a, b):
        return a*b
# p
def quadrilateral_P(a, b):
    if is_valid_side(a,b):
        return (a+b)*2

# круг
#s
def circle_S(r):
    if is_valid_side(r):
        return 3.14**r
#P
def circle_P(r):
    if is_valid_side(r):
        return 2*3.14*r

#треугольник
#S
def triangle_S(a, b, c):
    if is_valid_side(a, b, c):
        p = (a + b + c) / 2
        return (p*(p-a)*(p-b)*(p-c)) ** 0.5

# P
def triangle_P(a,b,c):
    if is_valid_side(a, b, c):
        return a+b+c
