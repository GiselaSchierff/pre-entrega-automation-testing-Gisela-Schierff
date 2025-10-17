# crear sistema de login con selenium


# IMPROTACIONES
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions





URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"



def get_driver(): # se divide responsabilidad
    
    # se maximiza la pantalla
    
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized') 

    # obtiene la instalación automática del driver y se le pasan los servicios 
    # permite abrir el navegador iniciando la sesión con selenium

    # instalación del driver 

    servicio = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service = servicio, options=chrome_options) # permite manejar el navegador desde el driver

    driver.implicitly_wait(5)

    return driver # devuelve sesión de selenium
    
def login_saucedemo(driver): # recibe el driver 
    
    # abre link
    driver.get(URL)
    # verifica que esté en la página esperada (saucedemo.com) 
    assert URL == driver.current_url

    # ingresa credenciales
    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((By.ID, "user-name"))
    ).send_keys(USERNAME)

    # driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((By.ID, "password"))
    ).send_keys(PASSWORD)

    # driver.find_element(By.ID, "password").send_keys(PASSWORD)
    
    # sacar captura
    driver.save_screenshot("reports/escribir_credenciales.png")

    # hacer click al boton para logearse

    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((By.ID, "login-button"))
    ).click()
