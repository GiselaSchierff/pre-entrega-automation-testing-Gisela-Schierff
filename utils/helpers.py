# crear sistema de login con selenium


# IMPROTACIONES
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

# importar json según Brayann 

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(''),'..')))

#IMPORTAR JSON SEGÚN CHATGPT 

import json
import os

# Ruta al archivo actual
current_dir = os.path.dirname(__file__)

# Cargar datos.json
with open(os.path.join(current_dir, 'datos.json'), 'r', encoding='utf-8') as f:
    datos = json.load(f)

# Cargar selectores.json
with open(os.path.join(current_dir, 'selectores.json'), 'r', encoding='utf-8') as f:
    selectores = json.load(f)


URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"



def get_driver(): # se divide responsabilidad
    # se maximiza la pantalla
    
    Options().add_argument('--start-maximized')

    # obtiene la instalación automática del driver y se le pasan los servicios 
    # permite abrir el navegador iniciando la sesión con selenium

    # instalación del driver 

    servicio = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service = servicio) # permite manejar el navegador desde el driver

    time.sleep(5)

    return driver # devuelve sesión de selenium

def login_saucedemo(driver): # recibe el driver  
