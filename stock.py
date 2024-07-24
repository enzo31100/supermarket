#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Stock:
    def __init__(self, name, price_per_kg=None, quantity_kg=None, price_per_piece=None, quantity_piece=None):
        self.name = name
        self.price_per_kg = price_per_kg
        self.quantity_kg = quantity_kg
        self.price_per_piece = price_per_piece
        self.quantity_piece = quantity_piece

    def update_stock(self, kg=0, piece=0):
        """

        :param kg:
        :param piece:
        :return:
        """
        if self.quantity_kg is not None:
            self.quantity_kg -= kg
        if self.quantity_piece is not None:
            self.quantity_piece -= piece

    def is_available(self, kg=0, piece=0):
        return (self.quantity_kg >= kg if self.quantity_kg is not None else True) and \
               (self.quantity_piece >= piece if self.quantity_piece is not None else True)
