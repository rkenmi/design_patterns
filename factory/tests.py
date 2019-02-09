import unittest

from factory.Pizza import Pizza
from factory.PizzaStore import DominosPizzaStore, PizzaStore, PapaJohnsPizzaStore, FactoryNotWorkingException


class MyTestCase(unittest.TestCase):
    def test_factory_method(self):
        my_pizza_store = PizzaStore()
        with self.assertRaises(NotImplementedError):
            my_pizza_store.create_pizza('cheese')

        my_pizza_store = PapaJohnsPizzaStore()
        self.assertIsInstance(my_pizza_store.create_pizza('cheese'), Pizza)

    def test_abstract_factory_method(self):
        my_pizza_store = PizzaStore()

        with self.assertRaises(FactoryNotWorkingException):
            my_pizza_store.order_pizza('pepperoni')

        my_pizza_store = DominosPizzaStore()
        self.assertIsInstance(my_pizza_store.order_pizza('pepperoni'), Pizza)

if __name__ == '__main__':
    unittest.main()
