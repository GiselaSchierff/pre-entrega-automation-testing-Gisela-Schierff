# Propósito del proyecto

Se automatizará y validará en la web saucedemo.com diferentes flujos y casos de pruebas, con el fin de que el usuario pueda logearse y cagregar un producto al carrito sin problemas, dado que la web corresponde a una tienda online. A continuación se detallan los flujos y casos de pruebas: 
- Login
- Navegación y verificación del catálogo 
- Agregado de un producto al carrito


# Tecnologías utilizadas

Python como lenguaje principal y algunas dependencias de Python 

Pytest para estructura de testing

Selenium WebDriver para automatización

Pytest-HTML para el reporte de tests


# Instrucciones de instalación de dependencias

instalar Python desde https://www.python.org/downloads/ y comprobar la instalación en la consola con: python --v 

instalar Pytest y el plugin para generar el reporte de errores con: pip install pytest pytest-html 

instalar selenium con el siguiente comando en la consola: pip install selenium

instalar el manager del webdriven con el siguiente comando de consola: pip install webdriver-manager


# Comando para ejecutar las pruebas

para generar un reporte HTML autosuficiente en la consola, corriendo los tests, se debe escribir pytest -v --html=reports/report.html --self-contained-html 

para hacer correr los tests sin el reporte, ejecutar el siguiente comando en la consola: pytest -v
