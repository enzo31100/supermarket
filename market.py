#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module: Trot Race Simulation

Description:
    This module simulates a trot race with multiple horses. It allows users to select the type of race (1 for Tiercé,
    2 for Quarté, 3 for Quinté), specify the number of horses, and run the race by simulating the horses' movements
    based on dice rolls. The program displays the current standings and the results once the race is complete.

Author(s):
    [Your Name]
    [Your Email]

Date:
    [Date]

License:
    This software is licensed under the [License Name] License. See the LICENSE file for details.

Usage:
    Run this script to start the trot race simulation. Follow the prompts to choose the type of race, enter the number
    of horses, and advance through the race. Press 'Enter' to simulate each round of the race.

Dependencies:
    - random
    - unicodedata
"""

from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class FruitVegetable:
    """
    Represents a fruit or vegetable item in the grocery store.

    Attributes:
        name (str): The name of the item.
        stock (float): The current stock of the item in kg or pieces.
        price (float): The price of the item per kg or per piece.
        unit (str): The unit of the item, either "kg" or "piece".
    """
    name: str
    stock: float
    price: float
    unit: str  # "kg" or "piece"
