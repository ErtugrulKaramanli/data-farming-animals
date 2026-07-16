"""
This module defines the Cow class.
"""

from farm.animal import Animal


class Cow(Animal):
    """
    Represents a cow that can talk and produce milk when fed.
    """

    def __init__(self):
        """
        Initializes a cow with default animal traits and 0 milk.
        """
        super().__init__()
        self.milk = 0

    def talk(self):
        """
        Returns the sound a cow makes.
        """
        return "Moo"

    def feed(self):
        """
        Feeds the cow, increasing energy and producing 2 liters of milk.
        """
        super().feed()
        self.milk += 2
