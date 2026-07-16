"""
Unit tests for the Cow class.
"""

from farm.cow import Cow


def test_initialize_sets_milk_to_zero():
    """A new cow should start with 0 liters of milk."""
    cow = Cow()
    assert cow.milk == 0


def test_initialize_sets_energy_to_zero():
    """A new cow should start with 0 energy inherited from Animal."""
    cow = Cow()
    assert cow.energy == 0


def test_talk_returns_moo():
    """A cow should say 'Moo' when talk is called."""
    cow = Cow()
    assert cow.talk() == "Moo"


def test_feed_adds_energy():
    """Feeding a cow should increase its energy by 1."""
    cow = Cow()
    cow.feed()
    assert cow.energy == 1


def test_feed_adds_milk():
    """Feeding a cow should increase its milk production by 2 liters."""
    cow = Cow()
    cow.feed()
    assert cow.milk == 2


def test_feed_extends_method():
    """Feeding a cow multiple times should correctly accumulate both energy and milk."""
    cow = Cow()
    cow.feed()
    cow.feed()
    assert cow.energy == 2
    assert cow.milk == 4
