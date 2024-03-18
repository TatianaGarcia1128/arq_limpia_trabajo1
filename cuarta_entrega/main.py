from cart import Cart
from controller import CartController
from db import DB
from product import Product
from repository import CartRepository
from service import CartService
import json
from test_cart import test_add_product_with_negative_price

def db_initialization():
    # Cargar el archivo JSON existente o crear una lista vacía si el archivo no existe
    try:
        with open("cuarta_entrega/list_products.json", 'r') as f:
            datos = json.load(f)
    except FileNotFoundError:
        datos = []

    return datos
    
    
def run_get_product(bd_init):
    cart_repository = CartRepository(bd_init)
    cart_service = CartService(cart_repository)
    cart_controller = CartController(cart_service)
    
    print(cart_controller.getProducts())

    
def run_add_product(bd_init):
    id = input('ingrese el id: ')
    name = input('Ingrese el nombre: ')
    price = input('Ingrese el precio: ')

    new_product = {
        "id" : int(id),
        "name" : name,
        "price": float(price),
    }

    bd_init.append(new_product)
        # Escribir los datos actualizados de vuelta al archivo JSON
    with open("cuarta_entrega/list_products.json", 'w') as f:
        json.dump(bd_init, f, indent=4)
    
    cart_repository = CartRepository(db)
    cart_service = CartService(cart_repository)
    cart_controller = CartController(cart_service)
    print(cart_controller.getProducts())
    

def run_delete_product(bd_init):
    cart_repository = CartRepository(bd_init)
    cart_service = CartService(cart_repository)
    cart_controller = CartController(cart_service)
    
    id_eliminar = input("Dígite el id del producto que desea eliminar: ")
    cart_controller.deleteProduct(int(id_eliminar))
    
    
def run_calc_total_price(bd_init):
    cart_repository = CartRepository(bd_init)
    cart_service = CartService(cart_repository)
    cart_controller = CartController(cart_service)
    print(cart_controller.getTotalPrice())

def mostrar_menu():
    print("Menú de opciones:")
    print("1. Obtener productos")
    print("2. Agregar producto")
    print("3. Eliminar producto")
    print("4. Calcular precio total")
    print("5. Salir")
    
    
if __name__ == "__main__":
    while True:
        bd_init = db_initialization()
        db = DB(bd_init)

        mostrar_menu()
        opcion = input("Ingrese el número de la opción que desea ejecutar: ")

        if opcion == "1":
            run_get_product(db)
        elif opcion == "2":
            run_add_product(bd_init)
        elif opcion == "3":
            run_delete_product(db)
        elif opcion == "4":
            run_calc_total_price(db)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido del menú.")