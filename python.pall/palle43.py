class Hotel:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu

class Customer:
    def __init__(self, name, phno):
        self.name = name
        self.phno = phno
        self.order = {}

    def order_food(self, *items):
        for item in items:
            item_name, item_quantity = item.split('-')
            if item_name in hotel.menu:
                self.order[item_name] = int(item_quantity)  # Fixed variable name here
            else:
                print(f"{item_name} is not available in the menu.")

    def generate_bill(self):
        total_amount = 0
        for item, quantity in self.order.items():
            total_amount += hotel.menu[item] * quantity
        return total_amount

# Creating a Hotel instance
menu_items = {'coffee': 20, 'tea': 15, 'sandwich': 40, 'pizza': 100}
hotel = Hotel("Sample Hotel", menu_items)

# Creating a Customer instance
customer = Customer("Varun Sharma", "9168576781")

# Customer places an order
customer.order_food("coffee-2", "sandwich-1", "burger-3","pizza-3")

# Generating and printing the bill
total_bill = customer.generate_bill()
print(f"Total bill for {customer.name}: rupees {total_bill}")
