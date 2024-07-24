#!/usr/bin/env python
# -*- coding: utf-8 -*-


from basket import Basket


class Client:
    def __int__(self, first_name, last_name):
        self.name = f"{first_name} {last_name}"
        self.basket = Basket()

    def add_product(self, product, quantity, is_kg=True):
        self.basket.add_item(product, quantity, is_kg)

    def receipt(self):
        print(f"Ticket de caisse pour {self.name}")
        self.basket.display()
