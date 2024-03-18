
import json

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
        
        try:
            # Cargar el archivo JSON existente
            with open("cuarta_entrega/list_products.json", 'r') as f:
                datos = json.load(f)
        except FileNotFoundError:
            print("El archivo JSON no existe.")
            return

        # Buscar el índice del producto con el ID especificado
        indice = None
        for i, producto in enumerate(datos):
            if producto['id'] == id:
                indice = i
                break

        if indice is not None:
            # Eliminar el producto de la lista
            del datos[indice]
            print("Registro eliminado correctamente.")
        else:
            print("No se encontró ningún registro con el ID especificado.")

        # Escribir los datos actualizados de vuelta al archivo JSON
        with open("cuarta_entrega/list_products.json", 'w') as f:
            json.dump(datos, f, indent=4)
