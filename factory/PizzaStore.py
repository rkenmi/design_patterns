from factory.Pizza import CheesePizza, VeggiePizza
from factory.PizzaFactory import SimplePizzaFactory, DominosPizzaFactory


class PizzaStore:
    def __init__(self, factory=None):
        if factory:
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

    # quasi-Abstract factory method, implemented by subclasses
    # note that this class has no knowledge of the actual pizzas created
    def create_pizza(self, item):
        raise NotImplementedError

class DominosPizzaStore(PizzaStore):
    def __init__(self):
        super().__init__(DominosPizzaFactory())

class PapaJohnsPizzaStore(PizzaStore):

    # Factory Method Pattern
    def create_pizza(self, item):
        if item == 'cheese':
            return CheesePizza()
        elif item == 'veggie':
            return VeggiePizza()

class FactoryNotWorkingException(Exception):
    def __init__(self):
        super().__init__()
