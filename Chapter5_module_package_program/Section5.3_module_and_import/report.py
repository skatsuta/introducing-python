"""This module provides the weather report."""


def get_description():
    """Returns a random weather."""
    from random import choice
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilities)
