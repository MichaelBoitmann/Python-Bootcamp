class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cocoa, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
            "cocoa": cocoa,
        }


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cocoa=0, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cocoa=0, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cocoa=0, cost=3),
            MenuItem(name="mocha", water=200, milk=50, coffee=24, cocoa=24, cost=3),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
