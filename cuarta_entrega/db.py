

class DB:
    def __init__(self, db_product_list):
        self.db_data = db_product_list
        
    def get_db_data(self):
        return self.db_data

    def insert_db_data(self, product):
        print('Antigua:', self.db_data )
        self.db_data.append(product)
        
        print('Actualizada', self.db_data )
    
    def delete_db_data(self, id):
        print('Antigua:', self.db_data )
        
        new_product_list = []
        for product in self.db_data:
            if product["id"] != id:
                new_product_list.append(product)
        self.db_data = new_product_list
        print('Despues:', self.db_data )
