#!/usr/bin/env python
# -*- coding: utf-8 -*-


from stock import Stock


class Fruit(Stock):
    def __init__(self, name, price_per_kg, quantity_kg):
        super().__init__(name, price_per_kg=price_per_kg, quantity_kg=quantity_kg)
