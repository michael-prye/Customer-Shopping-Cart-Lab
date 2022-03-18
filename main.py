from customer import Customer
from product import Product

def run():
    me = Customer('michael')
    product_1 = Product('Playstation 5', '$500', 'Video Games')
    product_2 = Product('Elden Ring', '$60', 'Video Games')
    product_3 = Product('dualshock 5 controler', '$80', 'Video Games')
    print(me.name)
    me.add_new_product(product_1.name)
    me.add_new_product(product_2.name)
    me.add_new_product(product_3.name)
    me.get_cart()
    cart_total = me.my_cart.get_cart_total()
    print(cart_total)
    me.my_cart.clear_cart()
    me.get_cart()
run()