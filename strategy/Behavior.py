"""
The Strategy Pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it.
"""

# Basic Behaviors


class Attack:
    def __init__(self, attack_type, damage):
        self.attack_type = attack_type
        self.damage = damage

    def execute(self):
        return self.damage


class Magic:
    def __init__(self, magic_type, damage, mp_cost):
        self.magic_type = magic_type
        self.damage = damage
        self.mp_cost = mp_cost

    def execute(self):
        return self.damage

# Inherited Behaviors


class Slash(Attack):
    ATTACK_TYPE = 'Melee'
    DEFAULT_DAMAGE = 15

    def __init__(self):
        super().__init__(Slash.ATTACK_TYPE, Slash.DEFAULT_DAMAGE)


class Shoot(Attack):
    ATTACK_TYPE = 'Ranged'
    DEFAULT_DAMAGE = 8

    def __init__(self):
        super().__init__(Shoot.ATTACK_TYPE, Shoot.DEFAULT_DAMAGE)


class Fireball(Magic):
    MAGIC_TYPE = 'Fire'
    DEFAULT_DAMAGE = 20

    def __init__(self):
        super().__init__(Fireball.MAGIC_TYPE, Fireball.DEFAULT_DAMAGE, 3)


class Frostbolt(Magic):
    MAGIC_TYPE = 'Frost'
    DEFAULT_DAMAGE = 18

    def __init__(self):
        super().__init__(Frostbolt.MAGIC_TYPE, Frostbolt.DEFAULT_DAMAGE, 3)

