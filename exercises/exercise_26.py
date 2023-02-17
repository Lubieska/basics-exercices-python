# programa que pide confirmación
def pedir_confirmacion(prompt, reintentos =4,recordatorio = "Por favor intente nuevamente"):
    while True:
        # inicializar una variable captura un dato almacenado en prompt
        ok = input(prompt)
        if ok in ('S', 's', 'si', 'SI', 'Si'):
            return True # con return sale del bucle
        if ok in ('n', 'NO', 'no', 'No'):
            return False

        reintentos = reintentos - 1
        if reintentos < 0:
            raise ValueError('respuesta de usuario inválida')
        print(recordatorio)
pedir_confirmacion("¿Realmente Deseas Salir del Sistema?")

