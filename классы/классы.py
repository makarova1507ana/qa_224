# ООП


# Студент - создать

# класс - это пользовательский тип данных
class Student:
    def __init__(self, name, group, age):# инициализатор - создает объект
        self.name_student = name #name_student параметр или поле класса
        self.group = group
        self.age = age
        #print(self.name_student)

# создание объекта
# num = 1
# string = "cat"
student_Ivanov = Student(18, "П-45", 18) # 1-ый объект
print(student_Ivanov.name_student)

Petrov = Student(group="Э-40", age=25, name="Петров") # 2 -ой объекты
print(Petrov.name_student)
# 3 объект


Sidorov = Student("Сидоров", "Р-22", 19)
print(Sidorov.name_student, Sidorov.age, Sidorov.group)







# Класс Кот
# цвет , длина шерсти , порода, кличка, возраст - характеристики
class Cat:
    def __init__(self, name, age): #color, breed, age, length_wool):
        #self.name # -характеристика кота
        self.name = name
        self.age = age

vasya = Cat("Вася", 3)# Объект -  типа Cat
print(vasya.name, vasya.age)
