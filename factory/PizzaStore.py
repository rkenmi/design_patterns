from factory.Pizza import CheesePizza, VeggiePizza
from factory.PizzaFactory import SimplePizzaFactory, DominosPizzaFactory, RoundTablePizzaFactory


class PizzaStore:
    def __init__(self, factory=None):
        if factory:
            """
                The Abstract Factory Pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes.
            """
            self._factory = factory

    def _bake(self, pizza):
        print('Baked')
        return pizza

    def _prep(self, pizza):
        print('Dough is prepared and toppings are added')
        return pizza

    def order_pizza(self, type):
        pizza = None
        try:
            pizza = self._factory.create_pizza(type)
            pizza = self._prep(pizza)
            pizza = self._bake(pizza)
        except:
            print('invalid factory')
            raise FactoryNotWorkingException()

        return pizza

    """
    The Factory Method Pattern defines an interface for creating an object, but lets subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses.
    """
    def create_pizza(self, item):
        raise NotImplementedError

class DominosPizzaStore(PizzaStore):
    def __init__(self):
        super().__init__(DominosPizzaFactory())


class RoundTablePizzaStore(PizzaStore):
    def __init__(self):
        super().__init__(RoundTablePizzaFactory())

class PapaJohnsPizzaStore(PizzaStore):
    def create_pizza(self, item):
        if item == 'cheese':
            return CheesePizza()
        elif item == 'veggie':
            return VeggiePizza()

class FactoryNotWorkingException(Exception):
    def __init__(self):
        super().__init__()
