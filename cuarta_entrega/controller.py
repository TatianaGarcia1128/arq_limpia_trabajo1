


from product import Product


class CartController:
    def __init__(self, cart_service):
        self.cart_service = cart_service
        
    def getProducts(self):
        print('GET de BD')
        return self.cart_service.getProducts()
    
    def addProduct(self, product ):
        print('INSERT de BD')
        return self.cart_service.addProduct( product )

    def deleteProduct(self, id):
        print('DELETE de BD')
        return self.cart_service.deleteProduct( id )
        
    def getTotalPrice(self):
        print('COSTO TOTAL:')
        return self.cart_service.getTotalPrice()