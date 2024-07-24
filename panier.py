#!/usr/bin/env python
# -*- coding: utf-8 -*-


from stock import Stock
from fruit import Fruit
from legume import Legume


class Panier:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity, is_kg=True):
        if item not in self.items:
            self.items[item] = {'quantity': 0, 'is_kg': is_kg}
        if is_kg:
            self.items[item]['quantity'] += quantity
        else:
            self.items[item]['quantity'] += quantity

    def display(self):
        print("\nPanier:")
        total = 0
        for item, data in self.items.items():
            stock_item = inventory[item]
            if data['is_kg']:
                price = stock_item.price_per_kg
            else:
                price = stock_item.price_per_piece

            cost = data['quantity'] * price
            total += cost
            print(f"{item}: {data['quantity']} {'kg' if data['is_kg'] else 'pièce'} - {cost:.2f} €")

        print(f"Total: {total:.2f} €")
