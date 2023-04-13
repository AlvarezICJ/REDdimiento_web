Este código realiza 100 solicitudes a una URL determinada en hilos separados, utilizando la librería requests y threading de Python.
La función make_request() es la encargada de realizar una solicitud GET a la URL y en caso de éxito, 
imprimirá un mensaje indicando que la solicitud fue exitosa y el código de estado de la respuesta.
En caso de falla, la función imprimirá un mensaje de error y establecerá la variable global server_down en True.

Después de ejecutar todas las solicitudes, se espera a que todos los hilos se completen antes de imprimir si el servidor ha fallado o no. 
Si la variable server_down es True, significa que ha habido una o más fallas en las solicitudes y se imprime un mensaje indicando que el servidor ha fallado. 
En caso contrario, se imprime un mensaje indicando que todas las solicitudes se han completado con éxito.
