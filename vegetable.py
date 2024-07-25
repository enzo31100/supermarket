"""
Module: Vegetable

Description:
    This module contains the Vegetable class, which represents a vegetable in the inventory.
    It manages the name, price per piece, and available quantity of the vegetable.

Usage:
    Import this module and use the Vegetable class to create vegetable objects. Use the methods
    to check availability and update stock.
"""

class Vegetable:
    """
    Represents a vegetable in the inventory.

    Attributes:
        name (str): The name of the vegetable.
        price_per_piece (float): The price per piece of the vegetable.
        quantity_piece (int): The available quantity of the vegetable in pieces.
    """

    def __init__(self, name, price_per_piece, quantity_piece):
        """
        Initializes a Vegetable object with the given name, price per piece, and available quantity.

        :param name: The name of the vegetable.
        :param price_per_piece: The price per piece of the vegetable.
        :param quantity_piece: The available quantity of the vegetable in pieces.
        """
        self.name = name
        self.price_per_piece = price_per_piece
        self.quantity_piece = quantity_piece

    def is_available(self, piece):
        """
        Checks if the specified quantity of the vegetable is available.

        :param piece: The quantity in pieces to check for availability.
        :return: True if the quantity is available, False otherwise.
        """
        return self.quantity_piece >= piece

    def update_stock(self, piece=0):
        """
        Updates the stock of the vegetable by reducing the specified quantity.

        :param piece: The quantity in pieces to reduce from the stock.
        """
        self.quantity_piece -= piece
