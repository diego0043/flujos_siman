import random
import string
from config import *
from selectors_variables import *

def waitingPage():
    # Esperar a que la página se cargue completamente (ajustar según necesidad)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body')))
    
def moveIframe(id):
    # Espera hasta que el iframe esté presente y cambia al contexto del iframe
    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, id))
)

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
        print("email generado: ", ramdom_email)
        return ramdom_email
    except:
        print('Error al generar email aleatorio')

def find_element(type, locator):
    try:
        if type == 'id': 
            element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, locator)))
            return element
        elif type == 'class':
            element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, locator)))
            return element
        elif type == 'xpath':
            element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locator)))
            return element
    except:
        print('Error al encontrar el elemento')

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
            raise ValueError("Método de seleccion no soportado")
    except Exception as e:
        print(f'Error al seleccionar la opcion: {e}')

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

    time.sleep(1)
    
    click_btn("id", locator_continue_form)

    click_btn("id", locator_btn_modal_get_code)
    click_btn("id", locator_send_request_code)

    time.sleep(1)

    code = get_code_yopmail(email)

    click_item("id", locator_input_token)
    write_input("id", locator_input_token, code)

    click_btn("id", locator_confirm_code)

    time.sleep(5)

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

        #refresh page
        driver.refresh()

        try:

            moveIframe("ifmail")

            #obtenemos codigo del html de yopmail 
            codeMail =  find_element("xpath", locator_xpath_code);
            
            # Obtén el contenido de texto del elemento codeMail
            Phrase = codeMail.text

            # Extrae la subcadena desde el índice 22 hasta el final
            code = Phrase[22:]
        except:
            print('Error al obtener codigo de autenticacion')
            code = '0000'

        # Cierra la primera pestaña
        driver.close()

        # Obtén los identificadores de ventana nuevamente
        handles = driver.window_handles

        # Cambia al contexto de la segunda pestaña (la que queda abierta)
        driver.switch_to.window(handles[0])

        # Asegurarse de volver al contexto principal después de cada iteracion
        driver.switch_to.default_content()

        return code
    except:
        print('Error al obtener codigo de autenticacion')

def shipping_method(shipping_type):
    if shipping_type == 'delivery':
        try: 
            time.sleep(5)
            click_btn("id", locator_shipping_delivery)
            time.sleep(2)
            select_option("id", locator_state, "San Salvador")
            select_option("id", locator_city, "San Salvador")
            time.sleep(2)

            click_item("id", locator_ship_street)
            write_input("id", locator_ship_street, "Calle 1")
            click_item("id", locator_ship_complement)
            write_input("id", locator_ship_complement, "Casa 1")
            click_item("id", locator_ship_receiver)
            write_input("id", locator_ship_receiver, "Juan Perez")
            click_btn("class", locator_btn_save_shipping)

            time.sleep(2)

            click_btn("id", locator_btn_go_payment)

        except:
            print('Error al seleccionar metodo de envio')
    else: 
        print('Metodo de envio no soportado')

def login_with_code(email):
    try: 
        fill_form(email)
        shipping_method("delivery")
    except:
        print('Error al hacer login con el codigo')
def login_new_user():
    
    try: 
        print('Ingresando nuevo usuario...')
    except:
        print('Error al hacer login con nuevo usuario')
