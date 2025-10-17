# NO ES FACIL tomar textos de selectores para usar en el login, eliminar los archivos (MEJOR) O COPYPASTEAR DE CHATGPT

#REVISAR COMENTARIOS 
import pytest
import time

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils.helpers import login_saucedemo, get_driver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.fixture(scope="function") # el scope permite mantener el login abierto 
def driver():

    # configuracion para consultar a selenium webdriver 
    driver = get_driver()
    yield driver
    driver.quit()

def test_login(driver):
    # AGREGAR ESPERA EXPLICITA
    # assert credenciales para iniciar sesión 
    # logeo de usuario con username y password 
    login_saucedemo(driver)
    # click al boton de login -> USAR FIXTURE
    # validación de redirección a pagina de inventario
    # assert "/inventory.html" in driver.current_url
    # verificar el titulo (PESTAÑA)
    # verificar el titulo Products
    # titulo = driver.find_element(By.CLASS_NAME, "title").text
    # assert titulo == "Products"

    titulo = driver.find_element(By.CLASS_NAME, "title").text
    assert titulo == "Products"
 
    # validación de redirección a pagina de inventario

    assert "/inventory.html" in driver.current_url

def test_catalogo(driver):

    # logeo de usuario con username y password 

    login_saucedemo(driver)

    titulo = WebDriverWait(driver, 15).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, "title"))
    ).text

    assert titulo == "Products"
    # click al boton de login -> USAR FIXTURE
    # verificar el titulo (body)
    # comprobar existencia de visibilidad de productos (leng(productos) > 0)

    WebDriverWait(driver, 15).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'inventory_item'))
    )
    productos = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    
   # productos = driver.find_elements(By.CLASS_NAME, 'inventory_item')
   
    assert len(productos) > 0
    # verificar elementos importantes interfaz (menú, filtros, etc)
    driver.save_screenshot("reports/ver_catalogo.png")



def test_carrito(driver):

    # logeo de usuario con username y password 
    login_saucedemo(driver)

    titulo = driver.find_element(By.CLASS_NAME, "title").text
    assert titulo == "Products"

    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'inventory_item'))
    )
    productos = driver.find_elements(By.CLASS_NAME, 'inventory_item')

    # total_productos = len(productos)

    nombreProducto1Catalogo = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text

    # assert expected_conditions.invisibility_of_element(driver.find_element(By.CLASS_NAME, "cart_contents_container"))

    productos[0].find_element(By.TAG_NAME, "button").click()

    numero_carrito = WebDriverWait(driver, 15).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'shopping_cart_badge'))
    ).text
    # numero_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert int(numero_carrito) == 1

    driver.save_screenshot("reports/numero_carrito.png")

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


    WebDriverWait(driver, 15).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'cart_item'))
    )

    productosCarrito = driver.find_elements(By.CLASS_NAME, 'cart_item')
    # productosCarrito = driver.find_elements(By.CLASS_NAME, 'cart_item')
    assert len(productosCarrito) == 1
    

    nombreProducto1Carrito = productosCarrito[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    assert nombreProducto1Carrito == nombreProducto1Catalogo

    assert "/cart.html" in driver.current_url

    driver.save_screenshot("reports/ver_carrito.png")


    # click al boton de login -> USAR FIXTURE
    # agregar producto al carrito
    # verificar incremento del carrito
    # navegar pagina carrito de compras 
    # comprobar que el producto agregado está en el carrito 