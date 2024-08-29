from config import *
from selectors_variables import links
from methods import *

for link in range(len(links)):

    if link == 0:
        try:
            driver.get(links[link])
            email = generate_ramdom_email()
            waitingPage()
            login_with_code(email)
        except:
            print('Error al llenar el formulario')
    else: 
        # Abre una nueva pestaña con una URL específica
        """ driver.execute_script(f"window.open('{links[link]}', '_blank');")

        # Obtén los identificadores de ventana
        handles = driver.window_handles

        # Cambia a la segunda pestaña (la que acabamos de abrir)
        driver.switch_to.window(handles[1])

        # Realiza alguna acción en la segunda pestaña
        # ...

        # Cambia a la primera pestaña (la que queremos cerrar)
        driver.switch_to.window(handles[0])

        # Cierra la primera pestaña
        driver.close()

        # Obtén los identificadores de ventana nuevamente
        handles = driver.window_handles

        # Cambia al contexto de la segunda pestaña (la que queda abierta)
        driver.switch_to.window(handles[0])
        waitingPage()
        time.sleep(10) """

        


    
    


