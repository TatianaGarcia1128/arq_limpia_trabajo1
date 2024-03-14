

class CartRepository:
    def __init__(self, db_instance):
        self.db_instance = db_instance
        
    def getProducts(self):
        return self.db_instance.get_db_data()
        
    def addProduct(self, product ):
        self.db_instance.insert_db_data(product)
        
    def deleteProduct(self, id):
        self.db_instance.delete_db_data(id)
    
