class Dog:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        return f'{self.name} says {sound}'


class RussellTerrier(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}'


class Bulldog(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}'


class Pets():
    dogs = []

    def exercise_2(self):
        Pets.dogs = [dog1, dog2, dog3, dog4]
        print(f"I have {len(Pets.dogs)} dogs.")
        for dog in Pets.dogs:
            print(dog, end = '. ')


dog1 = Dog("Tom", 6).description()
dog2 = Dog("Jerry", 9).description()
dog3 = Dog("Butt", 3).description()
dog4 = Dog("Wine", 1).description()


dog = Pets().exercise_2()
print(' ')
print(f"And they're all {Dog.species}s, of course.")


