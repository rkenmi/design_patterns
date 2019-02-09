from factory.Pizza import CheesePizza, VeggiePizza, PepperoniPizza, CombinationPizza, MeatballPizza


# These are not design patterns, but programming idioms


class SimplePizzaFactory:
    def create_pizza(self, type):
        pizza = None

        if type == 'cheese':
            pizza = CheesePizza()
        elif type == 'veggie':
            pizza = VeggiePizza()

        return pizza

class DominosPizzaFactory:
    def create_pizza(self, type):
        pizza = None

        if type == 'cheese':
            pizza = CheesePizza()
        elif type == 'veggie':
            pizza = VeggiePizza()
        elif type == 'pepperoni':
            pizza = PepperoniPizza()
        elif type == 'combination':
            pizza = CombinationPizza()

        return pizza

class RoundTablePizzaFactory:
    def create_pizza(self, type):
        pizza = None

        if type == 'veggie':
            pizza = VeggiePizza()
        elif type == 'pepperoni':
            pizza = PepperoniPizza()
        elif type == 'combination':
            pizza = CombinationPizza()
        elif type == 'meatball':
            pizza = MeatballPizza()

        return pizza
