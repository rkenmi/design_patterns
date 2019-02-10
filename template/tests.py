import unittest

from template.Kitchen import BurgerKitchen, SmoothieKitchen, Kitchen


class TemplateTest(unittest.TestCase):
    def test_template(self):
        kitchen0 = Kitchen()
        kitchen1 = BurgerKitchen()
        kitchen2 = SmoothieKitchen()

        with self.assertRaises(NotImplementedError):
            kitchen0.cook()

        self.assertTrue(kitchen1.cook().startswith('(BUN)'))
        self.assertFalse(kitchen2.cook().startswith('(BUN)'))
        self.assertTrue(kitchen2.cook().startswith('(CUP)'))
        self.assertFalse(kitchen1.cook().startswith('(CUP)'))


if __name__ == '__main__':
    unittest.main()
