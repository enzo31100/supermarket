"""
Module: Client

Description:
    This module contains the Client class that represents a client in the store.
    It manages the client's name, their basket, and calculates the total amount spent.

Usage:
    Import this module and use the Client class to create client objects. Use the methods
    to add items to the client's basket and calculate the total amount spent.
"""
import basket


class Client:
    """
    Represents a client in the store.

    Attributes:
        name (str): The name of the client.
        basket (Basket): The basket containing the client's selected items.
    """

    def __init__(self, first_name, last_name):
        """
        Initializes a Client object with the given name and an empty basket.

        :param first_name: The first name of the client.
        :param last_name: The last name of the client.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.basket = basket.Basket()

    def add_item(self, item, quantity, is_kg=True):
        """
        Adds an item to the client's basket.

        :param item: The name of the item to add.
        :param quantity: The quantity of the item to add.
        :param is_kg: Boolean indicating if the quantity is in kilograms (True) or pieces (False).
        """
        self.basket.add_item(item, quantity, is_kg)

    def print_receipt(self, inventory):
        """
        Print the receipt for the client, showing all items and the total cost.

        :param inventory: Dictionary containing the stock of items.
        """
        print(f"\nReçu pour {self.first_name} {self.last_name} :")
        self.basket.display()
        print(f"Total à payer: {self.get_total(inventory):.2f} €")

    def get_total(self, inventory):
        """
        Get the total cost of the items in the client's basket based on the inventory prices.

        :param inventory: Dictionary containing the stock of items.
        :return: Total cost.
        """
        return self.basket.calculate_total(inventory)
