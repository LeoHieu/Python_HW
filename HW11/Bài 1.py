class Dog:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

fake = Dog('Fake',2)
mickey = Dog('Mickey', 7)
fuk = Dog('Fuk', 5)

def get_biggest_number(*args):
    return max(args)

big_dog = get_biggest_number(fake.age, mickey.age, fuk.age)
print(f'The oldest dog is {big_dog} years old')