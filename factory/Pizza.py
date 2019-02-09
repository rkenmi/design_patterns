CHEESE_TOPPING = 2
ONION_TOPPING = 3
BELL_PEPPER_TOPPING = 4
PEPPERONI_TOPPING = 5
SAUSAGE_TOPPING = 6

class Pizza:
    def __init__(self, toppings=()):
        self.toppings = toppings

class CheesePizza(Pizza):
    def __init__(self):
        super().__init__((CHEESE_TOPPING))

class VeggiePizza(Pizza):
    def __init__(self):
        super().__init__((CHEESE_TOPPING, ONION_TOPPING, BELL_PEPPER_TOPPING))

class PepperoniPizza(Pizza):
    def __init__(self):
        super().__init__((CHEESE_TOPPING, PEPPERONI_TOPPING))


class CombinationPizza(Pizza):
    def __init__(self):
        super().__init__((CHEESE_TOPPING, PEPPERONI_TOPPING, ONION_TOPPING, BELL_PEPPER_TOPPING, SAUSAGE_TOPPING))
