# Propósito del proyecto

PONER ESTRUCTURA DEL PROYECTO Y QUÉ TIENEN ADENTRO, TAMBIÉN SI HAY COSAS AÑADIDAS DE MAS (SELECTORES EN VARIABLES, ETC)
 
Se automatizará y validará en la web saucedemo.com diferentes flujos y casos de pruebas, con el fin de que el usuario pueda logearse y comprar sin problemas, dado que la web corresponde a una tienda online. A continuación se detallan los flujos y casos de pruebas: 
- Login
- Navegación y verificación del catálogo 
- Interacción con Productos y carrito



# Tecnologías utilizadas

Python como lenguaje principal y algunas dependencias de Python (Pytest, Selenium y Pytest-HTML para el reporte de tests unitarios)

Pytest para estructura de testing

Selenium WebDriver para automatización


# Instrucciones de instalación de dependencias

instalar Python desde https://www.python.org/downloads/ y comprobar la instalación en la consola con: python --v 

instalar Pytest y el plugin para generar el reporte de errores con: pip install pytest pytest-html 

instalar selenium con el siguiente comando en la consola: pip install selenium

instalar el manager del webdriven con el siguiente comando de consola: python3 primer_script.py

COMANDOS DE INSTALACION DE PYTHON Y SELENIUM, PIP (VER SI HAY MAS EN APUNTES IMPRESOS)

# Comando para ejecutar las pruebas (por ejemplo: pytest -v --html=reporte.html)


para generar un reporte HTML autosuficiente en la consola, se debe escribir pytest --html=reports/report.html --self-contained-html 


para hacer correr los tests, ejecutar el siguiente comando en la consola: pytest -v