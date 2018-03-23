class Dog:
    """ A simple dog class """

    def __init__(self, name):
        self._name = name

    def speak(self):
        return f"{self._name} says woof!"


class Cat:
    """ A simple cat class """

    def __init__(self, name):
        self._name = name

    def speak(self):
        return f"{self._name} says meow!"


def get_pet(pet='dog'):
    """ The factory method """
    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))

    return pets[pet]


dog = get_pet('dog')
cat = get_pet("cat")

print(dog.speak())
print(cat.speak())
