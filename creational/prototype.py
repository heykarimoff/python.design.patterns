import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, attr):
        """ Clone a registered object and update its attributes """
        obj = copy.deepcopy(self._objects[name])
        obj.__dict__.update(attr)
        return obj


class Car:
    def __init__(self):
        self.name = 'Skylark'
        self.color = 'Black'
        self.options = 'Turbo speed'

    def __str__(self):
        return f'{self.name} | {self.color} | {self.options}'


sky_lark_car = Car()
prototype = Prototype()
prototype.register_object('sky_lark', sky_lark_car)

ferrari = prototype.clone('sky_lark', {'name': 'Ferrari'})

print(sky_lark_car)
print(ferrari)


