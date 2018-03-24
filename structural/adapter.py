class Uzbek:
    """Uzbek speaker"""
    def __init__(self):
        self.name = 'Uzbek'

    def speak_uzbek(self):
        return 'Salom'


class British:
    """English speaker"""
    def __init__(self):
        self.name = 'British'

    def speak_english(self):
        return 'Hello'


class Adapter:
    """This changes generic method name to individualized method name"""
    def __init__(self, object, **adapter_method):
        self._object = object

        # Add a dictionary item that establishes the mapping between generic method name and concrete method name
        # For example: speak() to speak_uzbek()
        self.__dict__.update(adapter_method)

    def __getattr__(self, item):
        """Simply return the attributes of object"""
        return getattr(self._object, item)


uzbek = Uzbek()
british = British()

people = [
    Adapter(uzbek, speak=uzbek.speak_uzbek),
    Adapter(british, speak=british.speak_english)
]

for person in people:
    print(f'{person.name} says {person.speak()}')
