import os
import re
import time
import requests
import datetime
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Ruta al ejecutable de EdgeDriver ( especificar la ruta correcta )

paths = ['C:/Users/juan_valencia/Downloads/edgedriver_win64/msedgedriver.exe',]
            

# Configurar las opciones de Edge
options = Options()
options.add_argument("--inprivate")
options.add_argument("--start-maximized")
# Esta opción mantiene la pestaña abierta después de que el script termine
options.detach = True

# Configurar el servicio de EdgeDriver
service = Service(executable_path=paths[0])

# Crear el driver de Edge con las opciones y el servicio configurados
driver = webdriver.Edge(service=service, options=options)