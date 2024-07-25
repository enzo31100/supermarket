class Basket:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity, is_kg=True):
        if item in self.items:
            self.items[item]['quantity'] += quantity
        else:
            self.items[item] = {'quantity': quantity, 'is_kg': is_kg}

    def display(self):
        if not self.items:
            print("Le panier est vide.")
        else:
            print("Panier :")
            for item, details in self.items.items():
                unit = "kg" if details['is_kg'] else "pièce(s)"
                print(f"{item}: {details['quantity']} {unit}")

    def calculate_total(self, inventory):
        """
        Calculate the total cost of the items in the basket based on the inventory prices.

        :param inventory: Dictionary containing the stock of items.
        :return: Total cost.
        """
        total = 0.0
        for item, details in self.items.items():
            if details['is_kg']:
                total += inventory[item].price_per_kg * details['quantity']
            else:
                total += inventory[item].price_per_piece * details['quantity']
        return total
