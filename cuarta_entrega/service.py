

class CartService:
    def __init__(self, db_repository):
        self.db_repository = db_repository
        
    def getProducts(self):
        return self.db_repository.getProducts()
    
    def addProduct(self, product):
        if( product["price"] > 0 ):
            self.db_repository.addProduct( product )
            
        
    def deleteProduct(self, id):
        self.db_repository.deleteProduct( id )
    
    def getTotalPrice(self):
        cart_list = self.getProducts()
        totalPrice = 0
        add_10_percent_discount = False
        
        for product in cart_list:
            product_price = product["price"]
            if( product_price >= 100):
                add_10_percent_discount = True
            totalPrice += product_price
        
        if( add_10_percent_discount ):
            totalPrice = totalPrice * 0.9
        
        return totalPrice