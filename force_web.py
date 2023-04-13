import requests
import threading

# Variable global para indicar si ha ocurrido una falla
server_down = False

# Función para realizar una solicitud
def make_request(url):
    global server_down  # Acceder a la variable global

    try:
        response = requests.get(url)
        print(f"Request to {url} successful, status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request to {url} failed: {e}")
        server_down = True  # Se establece la variable global en True si ha habido una excepción

# URL y número de solicitudes
url = "https://www.example.com"
num_requests = 100

# Se ejecutan las solicitudes en threads separados
for i in range(num_requests):
    threading.Thread(target=make_request, args=(url,)).start()

# Esperar a que todas las solicitudes se completen antes de imprimir el resultado
for thread in threading.enumerate():
    if thread != threading.current_thread():
        thread.join()

# Imprimir si el servidor ha fallado o no
if server_down:
    print("El servidor ha fallado en una o más solicitudes")
else:
    print("Todas las solicitudes se han completado con éxito") 
