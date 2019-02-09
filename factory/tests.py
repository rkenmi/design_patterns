import unittest

from factory.PizzaStore import DominosPizzaStore, PizzaStore, PapaJohnsPizzaStore


class MyTestCase(unittest.TestCase):
    def test_factory_method(self):
        my_pizza_store = PizzaStore()

        method_implemented = True
        try:
            my_pizza_store.create_pizza('pepperoni')
        except:
            method_implemented = False

        self.assertEqual(method_implemented, False)

        my_pizza_store = PapaJohnsPizzaStore()

        method_implemented = True
        try:
            my_pizza_store.order_pizza('pepperoni')
        except:
            method_implemented = False

        self.assertEqual(method_implemented, True)


if __name__ == '__main__':
    unittest.main()
