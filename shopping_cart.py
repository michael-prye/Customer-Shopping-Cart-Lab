class Shopping_cart:
    def __init__(self):
        self.cart_inventory = []
    def get_cart_total(self):
        count = len(self.cart_inventory)
        return count
    def add_to_cart(self,item):
        self.cart_inventory.append(item)
    def clear_cart(self):
        self.cart_inventory.clear()
 