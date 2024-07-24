#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Main module for managing the stock and basket of fruits and vegetables.

This module allows clients to select and purchase fruits and vegetables from a store.
Clients can add fruits and vegetables to their basket, view their basket and the remaining
quantities in stock, and exit the program. The stock is updated after each purchase.

Usage:
    Run this script to start the stock and basket management program. Follow the prompts to
    choose fruits or vegetables, enter the desired quantities, and display the basket. The
    program automatically updates the stock based on purchases made.
"""

from fruit import Fruit
from vegetable import Vegetable
import basket

# Initial stock data with French names
inventory = {
    'Clémentine': Fruit('Clémentine', 2.90, 6),
    'Datte': Fruit('Datte', 7.00, 4),
    'Grenade': Fruit('Grenade', 3.50, 3),
    'Kaki': Fruit('Kaki', 4.50, 3),
    'Kiwi': Fruit('Kiwi', 3.50, 5),
    'Mandarine': Fruit('Mandarine', 2.80, 6),
    'Orange': Fruit('Orange', 1.50, 8),
    'Poire': Fruit('Poire', 2.50, 5),
    'Pomme': Fruit('Pomme', 1.50, 8),
    'Carotte': Vegetable('Carotte', 1.30, 7),
    'Choux de Bruxelles': Vegetable('Choux de Bruxelles', 4.00, 4),
    'Chou vert': Vegetable('Chou vert', 2.50, 12),
    'Courge butternut': Vegetable('Courge butternut', 2.50, 6),
    'Endive': Vegetable('Endive', 2.50, 5),
    'Épinard': Vegetable('Épinard', 2.60, 4),
    'Poireau': Vegetable('Poireau', 1.20, 5),
    'Pamplemousse': Vegetable('Pamplemousse', 2.00, 8),
    'Potiron': Vegetable('Potiron', 2.50, 6),
    'Radis noir': Vegetable('Radis noir', 5.00, 10),
    'Salsifis': Vegetable('Salsifis', 2.50, 3),
}


def main():
    """
    Main function to run the stock and basket management program.
    Provides a menu for clients to add fruits and vegetables to their basket,
    view their basket, and exit the program.
    """
    basket_client = basket.Basket()

    while True:
        print("\n1. Ajouter des fruits")
        print("2. Ajouter des légumes")
        print("3. Voir le panier")
        print("4. Quitter")
        choice = input("Votre choix : ")

        if choice == '1':
            print("\nFruits disponibles :")
            print("Entrez '0' pour retour")
            fruits = [item for item in inventory.keys() if isinstance(inventory[item], Fruit)]
            for idx, fruit in enumerate(fruits, 1):
                print(f"{idx}. {fruit} ({inventory[fruit].quantity_kg} kg)")

            fruit_choice = input("Choisissez un fruit (numéro) : ")
            if fruit_choice == "0":
                continue
            elif fruit_choice.isdigit() and 1 <= int(fruit_choice) <= len(fruits):
                selected_fruit = fruits[int(fruit_choice) - 1]
                quantity = float(input("Quantité (kg) : "))
                if inventory[selected_fruit].is_available(kg=quantity):
                    basket_client.add_item(selected_fruit, quantity)
                    inventory[selected_fruit].update_stock(kg=quantity)
                else:
                    print("Quantité non disponible.")
            else:
                print("Choix non valide.")

        elif choice == '2':
            print("\nLégumes disponibles :")
            print("Entrez '0' pour retour")
            vegetables = [item for item in inventory.keys() if isinstance(inventory[item], Vegetable)]
            for idx, vegetable in enumerate(vegetables, 1):
                print(f"{idx}. {vegetable} ({inventory[vegetable].quantity_piece} pièce(s))")

            vegetable_choice = input("Choisissez un légume (numéro) : ")
            if vegetable_choice == "0":
                continue
            elif vegetable_choice.isdigit() and 1 <= int(vegetable_choice) <= len(vegetables):
                selected_vegetable = vegetables[int(vegetable_choice) - 1]
                quantity = int(input("Quantité (pièce) : "))
                if inventory[selected_vegetable].is_available(piece=quantity):
                    basket_client.add_item(selected_vegetable, quantity, is_kg=False)
                    inventory[selected_vegetable].update_stock(piece=quantity)
                else:
                    print("Quantité non disponible.")
            else:
                print("Choix non valide.")

        elif choice == '3':
            basket_client.display()

        elif choice == '4':
            print("Au revoir !")
            break


if __name__ == "__main__":
    main()
