# Класс Кот
# цвет , длина шерсти , порода, кличка, возраст - характеристики

# def is_max(parametr): # функция для проверки параметра на максимальное значение
#     return parametr >= 100

class Cat:
    def __init__(self, name, age): #color, breed, age, length_wool):
        #self.name # - характеристика кота
        self.name = name
        self.age = age #f - field - поле класса - характеристика
        self.hungry = 100 #100 - полностью сытый
        self.energy = 100 #100 - бодрый
        self.mood = 100 #100 -довольный

    def feed(self): #метод
        self.hungry = 100 #полностью восполнил сытость
        self.mood = 100
        self.energy = 50

    def play(self, time: int): #метод time -минуты
        # 1 - минута - 1 единица настроения
        if not(self.is_max(self.mood)):
            self.mood += int(time*2)
        else:
            self.mood = 100
        self.hungry -= time*0.5
        self.energy -= time

    @staticmethod #декоратор
    # метод работает вне зависимости от объекта (от желания объекта)(в фоне)
    def is_max(parametr):  # функция для проверки параметра на максимальное значение
        return parametr >= 100



    def sleep(self, time: int):  # метод
        energy = self.energy
        hungry = self.hungry
        hungry -= time
        if not(self.is_max(energy)):
            energy += time * 2





