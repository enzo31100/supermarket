#!/usr/bin/env python
# -*- coding: utf-8 -*-


from stock import Stock


class Vegetable(Stock):
    def __init__(self, name, price_per_piece, quantity_piece):
        super().__init__(name, price_per_piece=price_per_piece, quantity_piece=quantity_piece)


"""
class Vegetable:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def update_quantity(self):
        name = {'carotte': 0, 'choux de bruxelles': 1, 'chou vert': 2, 'courge butternut': 3, 'Endive': 4}

        if self.name in name:
            self.quantity = name[self.name] * 100
"""
