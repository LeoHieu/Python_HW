class Dog:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        return f'{self.name} says {sound}'

    def eat(self):
        self.is_hungry = False
        return self.is_hungry

class RussellTerrier(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}'


class Bulldog(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}'


class Pets():
    dogs = []

    def bai_2(self):
        Pets.dogs = [dog1, dog2, dog3, dog4]
        print(f"I have {len(Pets.dogs)} dogs.")
        for dog in Pets.dogs:
            a =  Dog.description(dog)
            print(a, end = '. ')

    def check_is_hungry(self):
        Pets.dogs = [dog1, dog2, dog3, dog4]
        count = 0
        for dog in Pets.dogs:
            b = Dog.eat(dog)
            if b == False:
                count += 1
        if count == len(Pets.dogs):
            print('My dogs are not hungry')
        else:
            print('My dogs are hungry')


dog1 = Dog("Tom", 6)
dog2 = Dog("Jerry", 9)
dog3 = Dog("Butt", 3)
dog4 = Dog("Wine", 1)


dog = Pets().bai_2()
print(' ')
print(f"And they're all {Dog.species}s, of course.")

abc = Pets().check_is_hungry()