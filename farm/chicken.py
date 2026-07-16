"""
This module defines the Chicken class.
"""

from farm.animal import Animal


class Chicken(Animal):
    """
    Represents a chicken that behaves differently based on its gender.
    """

    def __init__(self, gender):
        """
        Initializes a chicken with a gender and 0 eggs.
        """
        super().__init__()
        self.gender = gender
        self.eggs = 0

    def talk(self):
        """
        Returns a sound based on the chicken's gender.
        """
        if self.gender == "female":
            return "Cluck"
        return "Cock-a-doodle-do"

    def feed(self):
        """
        Feeds the chicken. Only female chickens produce eggs.
        """
        super().feed()
        if self.gender == "female":
            # Dişi tavuk her beslendiğinde 1 yumurta üretir
            self.eggs += 1
