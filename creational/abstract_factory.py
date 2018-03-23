class Dog:
    """ A simple dog class """

    def __init__(self, name):
        self._name = name

    def speak(self):
        return f"{self._name} says woof!"

    def __str__(self):
        return self._name


class Cat:
    """ A simple cat class """

    def __init__(self, name):
        self._name = name

    def speak(self):
        return f"{self._name} says meow!"

    def __str__(self):
        return self._name


class DogFactory:
    """ Concrete Factory """

    def get_pet(self):
        return Dog("Doe")
    
    def get_pet_food(self):
        return "Dog Food!"
    

class CatFactory:
    """ Concrete Factory """

    def get_pet(self):
        return Cat("Jony")
    
    def get_pet_food(self):
        return "Cat Food!"
    

class PetStore:
    """ PetStore houses our Abstract Factory """
    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory
    
    def show_pet(self):
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_pet_food()

        print(f"Our pet is '{pet}'")
        print(f"Our pet '{pet.speak()}'")
        print(f"Its food is '{pet_food}'")


dog_factory = DogFactory()
cat_factory = CatFactory()

shop = PetStore(pet_factory=dog_factory)
shop.show_pet()

another_shop = PetStore(pet_factory=cat_factory)
another_shop.show_pet()
