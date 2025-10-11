# tomar textos de selectores para usar en el login 
#REVISAR COMENTARIOS 
import pytest

@pytest.fixture
def driver():
    # configuracion para consultar a selenium webdriver
    # logeo de usuario con username y password 
    # click al boton de login 
    
def test_login(driver):
    # assert credenciales para iniciar sesión 
    # logeo de usuario con username y password 
    # click al boton de login -> USAR FIXTURE
    # redirección a pagina de inventario
    # verificar el titulo (PESTAÑA)
    # verificar el titulo (body)

def test_catalogo():
    # logeo de usuario con username y password 
    # click al boton de login -> USAR FIXTURE
    # verificar el titulo (body)
    # comprobar existencia de visibilidad de productos (leng(productos) > 0)
    # verificar elementos importantes interfaz (menú, filtros, etc)

def test_carrito():
    # logeo de usuario con username y password 
    # click al boton de login -> USAR FIXTURE
    # agregar producto al carrito
    # verificar incremento del carrito
    # navegar pagina carrito de compras 
    # comprobar que el producto agregado está en el carrito 