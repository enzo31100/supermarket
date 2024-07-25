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

Dependencies:
    - fruit
    - vegetable
    - basket
    - client
"""

from fruit import Fruit
from vegetable import Vegetable
import basket
import client as client_module  # Renommer l'importation pour éviter le conflit

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

clients = []


def main():
    """
    Main function to run the stock and basket management program.
    Provides a menu for clients to add fruits and vegetables to their basket,
    view their basket, and exit the program.
    """
    while True:
        print("\n1. Arrivée d'un client")
        print("2. Éditer le bilan de la journée")
        print("3. Quitter")
        choice = input("Votre choix : ")

        if choice == '1':
            first_name = input("Prénom du client : ")
            last_name = input("Nom du client : ")
            current_client = client_module.Client(first_name, last_name)  # Utiliser le nom renommer
            clients.append(current_client)

            while True:
                print("\n1. Ajouter des fruits")
                print("2. Ajouter des légumes")
                print("3. Voir le panier")
                print("4. Terminer les achats")
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
                            current_client.add_item(selected_fruit, quantity)
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
                            current_client.add_item(selected_vegetable, quantity, is_kg=False)
                            inventory[selected_vegetable].update_stock(piece=quantity)
                        else:
                            print("Quantité non disponible.")
                    else:
                        print("Choix non valide.")

                elif choice == '3':
                    current_client.basket.display()

                elif choice == '4':
                    current_client.print_receipt(inventory)
                    break

        elif choice == '2':
            print("\nBilan de la journée :")
            total_revenue = 0
            for client in clients:
                print(f"Client : {client.first_name} {client.last_name}, Total Achats : "
                      f"{client.get_total(inventory):.2f} €")
                total_revenue += client.get_total(inventory)
            print(f"\nTotal des ventes : {total_revenue:.2f} €")
            print("\nStock restant :")
            for item in inventory:
                if isinstance(inventory[item], Fruit):
                    print(f"{item}: {inventory[item].quantity_kg} kg")
                elif isinstance(inventory[item], Vegetable):
                    print(f"{item}: {inventory[item].quantity_piece} pièce(s)")

        elif choice == '3':
            print("Au revoir !")
            break


if __name__ == "__main__":
    main()
