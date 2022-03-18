from shopping_cart import Shopping_cart

class Customer:
    def __init__(self, user_name):
        self.name = user_name
        self.my_cart = Shopping_cart()
    def add_new_product(self,item):
        self.my_cart.add_to_cart(item)
    def get_cart(self):
        if self.my_cart.get_cart_total() == 0:
                print('The cart is empty')
        else:
            for i in self.my_cart.cart_inventory:
                print(i)