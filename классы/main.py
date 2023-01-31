from Cat import*
def print_cats_paramets(cat=Cat):# функция печати
    print("hungry", cat.hungry, "energy", cat.energy, "mood", cat.mood)


print(5)

vasya = Cat("Вася", 3) # Объект -  типа Cat
vasya.hungry -= 20
vasya.mood = 70
print_cats_paramets(vasya)
vasya.play(30)
print_cats_paramets(vasya)
vasya.play(30)
print_cats_paramets(vasya)
vasya.feed()
print_cats_paramets(vasya)
vasya.sleep(10)
print_cats_paramets(vasya)

#print(vasya.name, vasya.age, vasya.hungry)