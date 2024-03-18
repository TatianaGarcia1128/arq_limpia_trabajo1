from cart import Cart
from controller import CartController
from db import DB
from product import Product
from repository import CartRepository
from service import CartService


def db_initialization():
    lista_productos = [
        {
            "id" : 1,
            "name" : "Balon",
            "price": 13,
        },
        {
            "id" : 2,
            "name" : "PC",
            "price": 83,
        },
    ]

    db = DB(lista_productos)
    return db
    
    
def run_get_product():
    bd_init = db_initialization()
    cart_repository = CartRepository(bd_init)
    cart_service = CartService(cart_repository)
    cart_controller = CartController(cart_service)
    
    print(cart_controller.getProducts())
    
def run_add_product():
    
    new_product = {
        "id" : 3,
        "name" : "Morral",
        "price": 53,
    }
    
    bd_init = db_initialization()
    cart_repository = CartRepository(bd_init)
    cart_service = CartService(cart_repository)
    cart_controller = CartController(cart_service)
    
    cart_controller.addProduct( new_product )
    print(cart_controller.getProducts())
    

def run_delete_product():
    
    bd_init = db_initialization()
    cart_repository = CartRepository(bd_init)
    cart_service = CartService(cart_repository)
    cart_controller = CartController(cart_service)
    
    cart_controller.deleteProduct(1)
    print(cart_controller.getProducts())
    
    
def run_calc_total_price():
    bd_init = db_initialization()
    cart_repository = CartRepository(bd_init)
    cart_service = CartService(cart_repository)
    cart_controller = CartController(cart_service)
    print(cart_controller.getTotalPrice())
    
    
if __name__ == "__main__":
    # run_get_product()
    # run_add_product()
    # run_delete_product()
    run_calc_total_price()
    
    # test()