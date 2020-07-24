class Store:
    def __init__(self, name):
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
        self.name = name
        self.items = []

    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        self.items.append({"name": name, "price": price})

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        # The following conventional way works:
        # total_price = 0
        # for item in self.items:
        #     total_price += item["price"]
        # return total_price
        # The following is shorter:
        return sum([item["price"] for item in self.items])

safeway = Store("Safeway")
safeway.add_item("Thyme", 2.99)
safeway.add_item("Steak", 22.99)
safeway.add_item("Chicken", 12.99)

print(safeway.stock_price())