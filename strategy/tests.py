import unittest

from strategy.Behavior import Slash, Frostbolt, Shoot
from strategy.RPGCharacter import RPGCharacter


class StrategyTest(unittest.TestCase):
    def test_strategy(self):
        fred = RPGCharacter(Slash(), Frostbolt())

        self.assertEqual(fred.execute_attack(), Slash.DEFAULT_DAMAGE)

        fred.set_attack(Shoot())
        self.assertNotEqual(fred.execute_attack(), Slash.DEFAULT_DAMAGE)
        self.assertEqual(fred.execute_attack(), Shoot.DEFAULT_DAMAGE)

        fred.set_attack(Slash())
        self.assertNotEqual(fred.execute_attack(), Shoot.DEFAULT_DAMAGE)
        self.assertEqual(fred.execute_attack(), Slash.DEFAULT_DAMAGE)


if __name__ == '__main__':
    unittest.main()
