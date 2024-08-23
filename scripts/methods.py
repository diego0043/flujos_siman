import random
import string
from config import *
from selectors_variables import *

def waitingPage():
    # Esperar a que la página se cargue completamente (ajustar según necesidad)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body')))

def click_btn(type, locator):
    try:
        if type == 'id': 
            btn_continuar = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, locator)))
            btn_continuar.click()
        elif type == 'class':
            btn_continuar = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, locator)))
            btn_continuar.click()
    except:
        print('Error al hacer click en el boton continuar')

def generate_ramdom_email():
    try: 
        ramdom_email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + '@yopmail.com'
        return ramdom_email
    except:
        print('Error al generar email aleatorio')

def click_item(type, locator):
    try:
        if type == 'id': 
            item = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, locator)))
            item.click()
        elif type == 'class':
            item = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, locator)))
            item.click()
    except:
        print('Error al hacer click en el item')

def write_input(type, locator, text):
    try:
        if type == 'id': 
            input = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, locator)))
            input.send_keys(text)
        elif type == 'class':
            input = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, locator)))
            input.send_keys(text)
    except:
        print('Error al escribir en el input')

def select_option(type, locator, option, method='text'):
    try:     
        if type == 'id':
            select_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, locator)))
        elif type == 'class':
            select_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, locator)))
        else:
            raise ValueError("Tipo de localizador no soportado")

        select = Select(select_element)
        select = Select(select_element)

        if method == 'text':
            select.select_by_visible_text(option)
        elif method == 'value':
            select.select_by_value(option)
        elif method == 'index':
            select.select_by_index(int(option))
        else:
            raise ValueError("Método de selección no soportado")
    except Exception as e:
        print(f'Error al seleccionar la opción: {e}')

def fill_form(email):
    click_btn("id", locator_btn_go_payment)
    click_btn("class", locator_btn_register)
    click_item("id", locator_input_email)
    write_input("id", locator_input_email, email)
    click_item("id", locator_name_form)
    time.sleep(2)
    click_item("id", locator_input_email)
    click_item("id", locator_name_form)
    write_input("id", locator_name_form, "Juan")
    click_item("id", locator_lastname_form)
    write_input("id", locator_lastname_form, "Perez")
    select_option("id", locator_type_document, "DUI")
    click_item("id", locator_document)
    write_input("id", locator_document, "060247028")
    click_item("id", locator_number_phone)
    write_input("id", locator_number_phone, "22222222")
    click_item("class", locator_terms)
    click_btn("id", locator_continue_form)
    
    click_btn("id", locator_continue_form)

def get_code_yopmail(email):
    try: 
        split_email = email.split('@')
        email_name = split_email[0]

        # Abre una nueva pestaña con una URL específica
        driver.execute_script(f"window.open('https://yopmail.com/es/', '_blank');")

        # Obtén los identificadores de ventana
        handles = driver.window_handles

        # Cambia a la segunda pestaña (la que acabamos de abrir)
        driver.switch_to.window(handles[1])
        
        click_item("id", locator_ymail_login)
        write_input("id", locator_ymail_login, email_name)
        click_btn("id", locator_ymail_continue)

        time.sleep(5)
        

        

        print('Obteniendo código de autenticación...')
    except:
        print('Error al obtener código de autenticación')

def login_with_code(email):
    try: 
        print('Esperando código de autenticación...')
    except:
        print('Error al hacer login con el código')

def login_new_user():
    
    try: 
        print('Ingresando nuevo usuario...')
    except:
        print('Error al hacer login con nuevo usuario')

generate_ramdom_email()