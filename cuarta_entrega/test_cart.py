# Usar Pytest
from controller import CartController
from db import DB
from repository import CartRepository
from service import CartService

#Ejecutar en terminal con pytest test_cart.py estando dentro de la carpeta: cuarta_entrega

# CORRER LA PRUEBA
def test_add_product_with_negative_price():

    fake_response = [
        {
            "id": 1,
            "name": "Balon",
            "price": 13
        },
        {
            "id": 2,
            "name": "PC",
            "price": 83
        },
        {
            "id": 3,
            "name": "queso",
            "price": 6000.0
        }
    ]

    # SE AÑADE EL PRODUCTO
    product_with_negative_price = {
        "id" : 4,
        "name" : "PC",
        "price": -200,
    }
    
    # bd_init = db_initialization()
    db = DB(fake_response)
    cart_repository = CartRepository(db)
    cart_service = CartService(cart_repository)
    cart_controller = CartController(cart_service)
    
    cart_controller.addProduct( product_with_negative_price )
    #cart_controller.getProducts()
    
    expected_result = [
        {
            "id": 1,
            "name": "Balon",
            "price": 13
        },
        {
            "id": 2,
            "name": "PC",
            "price": 83
        },
        {
            "id": 3,
            "name": "queso",
            "price": 6000.0
        }
    ]
    
    # SE VALIDA LA COMPARACION
    assert  fake_response == expected_result


#La prueba debe pasar porque el valor del producto que se intenta agregar es negativo; por lo tanto, el fake_response y el expected_result deben ser iguales.