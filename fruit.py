"""
Module: Fruit

Description:
    This module contains the Fruit class, which represents a fruit in the inventory.
    It manages the name, price per kilogram, and available quantity of the fruit.

Usage:
    Import this module and use the Fruit class to create fruit objects. Use the methods
    to check availability and update stock.
"""

class Fruit:
    """
    Represents a fruit in the inventory.

    Attributes:
        name (str): The name of the fruit.
        price_per_kg (float): The price per kilogram of the fruit.
        quantity_kg (float): The available quantity of the fruit in kilograms.
    """

    def __init__(self, name, price_per_kg, quantity_kg):
        """
        Initializes a Fruit object with the given name, price per kilogram, and available quantity.

        :param name: The name of the fruit.
        :param price_per_kg: The price per kilogram of the fruit.
        :param quantity_kg: The available quantity of the fruit in kilograms.
        """
        self.name = name
        self.price_per_kg = price_per_kg
        self.quantity_kg = quantity_kg

    def is_available(self, kg):
        """
        Checks if the specified quantity of the fruit is available.

        :param kg: The quantity in kilograms to check for availability.
        :return: True if the quantity is available, False otherwise.
        """
        return self.quantity_kg >= kg

    def update_stock(self, kg=0):
        """
        Updates the stock of the fruit by reducing the specified quantity.

        :param kg: The quantity in kilograms to reduce from the stock.
        """
        self.quantity_kg -= kg
