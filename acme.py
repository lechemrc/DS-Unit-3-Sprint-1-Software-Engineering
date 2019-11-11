import random

class Product:
    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        ratio = self.price / self.weight
        if ratio < 0.5:
            return 'Not so stealable...'
        elif ratio >= 0.5 and ratio < 1.0:
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):
        explosive = self.flammability * self.weight
        if explosive < 10:
            return '...fizzle.'
        elif explosive >= 10 and explosive < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'


class BoxingGlove(Product):
    def __init__(self, name, weight=10):
        super().__init__(self)
        self.name = name
        self.weight = weight

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return 'That tickles.'
        elif self.weight >= 5 and self.weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'

