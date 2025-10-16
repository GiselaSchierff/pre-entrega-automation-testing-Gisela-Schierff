# NO ES FACIL tomar textos de selectores para usar en el login, eliminar los archivos (MEJOR) O COPYPASTEAR DE CHATGPT

#REVISAR COMENTARIOS 
import pytest

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils.helpers import login_saucedemo, get_driver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="session") # el scope permite mantener el login abierto 
def driver():
    # configuracion para consultar a selenium webdriver 
    driver = get_driver()
    yield driver
    driver.quit()

def test_login(driver):
    
    # assert credenciales para iniciar sesión 
    # logeo de usuario con username y password 
    login_saucedemo(driver)
    # click al boton de login -> USAR FIXTURE
    # validación de redirección a pagina de inventario
    assert "/inventory.html" in driver.current_url
    # verificar el titulo (PESTAÑA)
    # verificar el titulo Products
    titulo = driver.find_element(By.CLASS_NAME, "title").text
    assert titulo == "Products"

 

def test_catalogo(driver):
    # logeo de usuario con username y password 
    login_saucedemo(driver)
    # click al boton de login -> USAR FIXTURE
    # verificar el titulo (body)
    # comprobar existencia de visibilidad de productos (leng(productos) > 0)
    productos = driver.find_elements(By.CSS_SELECTOR, ".inventory_item")
    assert len(productos) > 0
    # verificar elementos importantes interfaz (menú, filtros, etc)

def test_carrito(driver):

    # logeo de usuario con username y password 
    login_saucedemo (driver)
    productos = driver.find_elements(By.CSS_SELECTOR, ".inventory_item")

    total_productos = len(productos)

    

 

    productos[0].find_elements(By.TAG_NAME, "add-to-cart-sauce-labs-backpack").click

   
    uno_numero_carrito = productos[0].find_elements(By.CLASS_NAME, "shopping_cart_badge").text
    assert uno_numero_carrito == 1



    # click al boton de login -> USAR FIXTURE
    # agregar producto al carrito
    # verificar incremento del carrito
    # navegar pagina carrito de compras 
    # comprobar que el producto agregado está en el carrito 