class Kitchen:
    def __init__(self):
        self.dishes = []

    """
    The Template Method Pattern defines the skeleton of an algorithm in a method, deferring some steps to subclasses. 
    Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm’s structure.
    """
    def cook(self):
        ingredients = self.prepare()
        dish = self.create(ingredients)
        self.dishes.append(dish)
        return self.serve()

    def prepare(self):
        raise NotImplementedError

    def create(self, ingredients):
        raise NotImplementedError

    def serve(self):
        return self.dishes[-1]


class BurgerKitchen(Kitchen):
    def prepare(self):
        print('fetching toppings')
        return {
            'lettuce': 1,
            'onion': 3,
            'patty': 1,
            'ketchup': 1,
            'mayonaise': 1,
        }

    def create(self, ingredients):
        burger = ['(BUN)']
        for topping in ingredients:
            burger.append(topping)
        burger.append('(BUN)')

        return " ".join(burger)


class SmoothieKitchen(Kitchen):
    def prepare(self):
        print('fetching fruits')
        return {
            'banana': 3,
            'apple': 2,
            'mango': 1,
            'yogurt': 2,
            'milk': 1,
        }

    def create(self, ingredients):
        smoothie = ['(CUP)']
        for fruit in ingredients:
            smoothie.append(fruit)
        smoothie.append('(CUP)')

        return " ".join(smoothie)

