"""
The Strategy Pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable.
Strategy lets the algorithm vary independently from clients that use it.
"""


class RPGCharacter:
    def __init__(self, attack=None, magic=None, special=None, item=None):
        self.attack = attack
        self.magic = magic
        self.special = special
        self.item = item

    def set_attack(self, attack):
        self.attack = attack

    def set_magic(self, magic):
        self.magic = magic

    def set_special(self, special):
        self.special = special

    def set_item(self, item):
        self.item = item

    def execute_attack(self):
        return self.attack.execute()

    def execute_magic(self):
        return self.magic.execute()
