
#IMPORTACIONES
import pytest

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

from utils.helpers import verificar_login_saucedemo, get_driver, verificar_productos_visibles_catalogo
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.fixture(scope="function") # el scope permite mantener el login abierto 
def driver():

    # configuracion para abrir selenium webdriver 
    driver = get_driver()
    yield driver
    driver.quit()

def test_login(driver):
    # logeo de usuario con username y password, y confirmación de título de Products  
    verificar_login_saucedemo(driver)

    # log de verificación del test
    print("El test del login pasó correctamente")

def test_catalogo(driver):

    # logeo de usuario con username y password, y confirmación de título de Products  
    verificar_login_saucedemo(driver)

    # comprobar existencia de visibilidad de productos
    verificar_productos_visibles_catalogo(driver)
    
    # verificar elementos importantes interfaz
    # verificar hamburguesa
    WebDriverWait(driver, 15).until(
        expected_conditions.visibility_of_element_located((By.ID, "react-burger-menu-btn"))
    )

    # verificar filtros
    WebDriverWait(driver, 15).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, "product_sort_container"))
    )

    # verificar título Products
    titulo_products = WebDriverWait(driver, 15).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, "title"))
    ).text
    assert titulo_products == "Products"

    # verificar texto footer
    titulo_swag_labs = WebDriverWait(driver, 15).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, "footer_copy"))
    ).text
    assert titulo_swag_labs == "© 2025 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy"

    # captura de pantalla del catálogo
    driver.save_screenshot("reports/ver_catalogo.png")

    # log de verificación del test
    print("El test del catálogo pasó correctamente")

def test_carrito(driver):

    # logeo de usuario con username y password, y confirmación de título de Products  
    verificar_login_saucedemo(driver)

    # comprobar existencia de visibilidad de productos
    productos = verificar_productos_visibles_catalogo(driver)
    
    # guardar nombre del primer producto, que se va a agregar al carrito 
    nombre_producto1_catalogo = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text

    # guardar precio del primer producto, que se va a agregar al carrito 
    precio_producto1_catalogo = productos[0].find_element(By.CLASS_NAME, "inventory_item_price").text

    print(f"El producto que se quiere agregar al carrito es {nombre_producto1_catalogo} y tiene un precio de {precio_producto1_catalogo}")


    # Esperar a que el primer botón tenga el texto Add to cart
    WebDriverWait(driver, 10).until(
        expected_conditions.text_to_be_present_in_element(
            (By.XPATH, "//div[@class='inventory_item'][1]//button"),
            "Add to cart"
        )
    )
    # hacer click en el botón del primer prducto, para agregarlo al carrito 
    productos[0].find_element(By.TAG_NAME, "button").click()

    # sacar captura del carrito con el primer producto agregado
    driver.save_screenshot("reports/numero_carrito.png")

    # hacer click en el carrito para ir a la página del carrito
    carrito = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
    )   
    carrito.click()

    # Esperar hasta que cambie la URL
    WebDriverWait(driver, 10).until(
        expected_conditions.url_contains("/cart.html")
    )

    # Verificar que el título sea Your cart
    titulo_your_cart = WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, "title"))
    )
    assert titulo_your_cart.text == "Your Cart"

    # verificar que haya un producto dentro del carrito 
    WebDriverWait(driver, 15).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, "cart_item"))
    )
    productos_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
    
    assert len(productos_carrito) == 1
    
    # verificar que el nombre del producto dentro del carrito sea el mismo que el que se agregó 
    nombre_producto1_carrito = productos_carrito[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    assert nombre_producto1_carrito == nombre_producto1_catalogo

    # verificar que el precio del producto dentro del carrito sea el mismo que el que se agregó 
    precioProducto1Carrito = productos_carrito[0].find_element(By.CLASS_NAME, "inventory_item_price").text
    assert precioProducto1Carrito == precio_producto1_catalogo

    # sacar captura de la página del carrito con el primer producto agregado
    driver.save_screenshot("reports/ver_carrito.png")

    # log de verificación del test
    print("El test del carrito pasó correctamente")

