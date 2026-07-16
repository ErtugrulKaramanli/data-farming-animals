"""
This module defines the base Animal class for all animals on the farm.
"""


# pylint: disable=too-few-public-methods
class Animal:
    """
    A base class representing a generic farm animal with energy tracking.
    """

    def __init__(self):
        """
        Initializes an animal with 0 energy.
        """
        self.energy = 0

    def feed(self):
        """
        Feeds the animal, increasing its energy by 1.
        """
        self.energy += 1
