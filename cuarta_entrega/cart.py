
from product import Product


class Cart:
    def __init__(self, product_list):
        self.product_list = product_list
        
    def addProduct(self, product : Product):
        self.product_list = self.product_list.append(product)
    