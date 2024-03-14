# Usar Pytest
from controller import CartController
from db import DB
from repository import CartRepository
from service import CartService


# ALISTAR LOS DATOS PARA EL TEST:
def db_initialization():
    lista_productos = [
        {
            "id" : 1,
            "name" : "Balon",
            "price": 10,
        },
    ]

    db = DB(lista_productos)
    return db
    



# CORRER LA PRUEBA
def test_add_product_with_negative_price():
    
    # SE AÑADE EL PRODUCTO
    product_with_negative_price = {
        "id" : 2,
        "name" : "PC",
        "price": -200,
    },
    
    bd_init = db_initialization()
    cart_repository = CartRepository(bd_init)
    cart_service = CartService(cart_repository)
    cart_controller = CartController(cart_service)
    
    cart_controller.addProduct( product_with_negative_price )
    cart_controller.getProducts()
    
    expected_result = [
        {
            "id" : 1,
            "name" : "Balon",
            "price": 10,
        },
    ]
    
    actual_value = cart_controller.getProducts()
    
    # SE VALIDA LA COMPARACION
    assert  actual_value == expected_result
    