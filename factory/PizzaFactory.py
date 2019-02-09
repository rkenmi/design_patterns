from factory.Pizza import CheesePizza, VeggiePizza, PepperoniPizza, CombinationPizza


# These are not design patterns, but programming idioms


class SimplePizzaFactory:
    def create_pizza(self, type):
        pizza = None

        if type == 'Cheese':
            pizza = CheesePizza()
        elif type == 'Veggie':
            pizza = VeggiePizza()

        return pizza

class DominosPizzaFactory:
    def create_pizza(self, type):
        pizza = None

        if type == 'Cheese':
            pizza = CheesePizza()
        elif type == 'Veggie':
            pizza = VeggiePizza()
        elif type == 'Pepperoni':
            pizza = PepperoniPizza()
        elif type == 'Combination':
            pizza = CombinationPizza()

        return pizza
