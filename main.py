import json
from lib.display import Display 
import sys

def implements_loader():
    with open('implements.py', 'r') as f:
        exec(f.read())

def carga_configuracion():
    # Carga de configuración desde config.json
    with open('datos/config.json', 'r') as f:
        global config
        config = json.load(f)

#print("Cargando configuración...")
#carga de variables globales.
carga_configuracion()

#print("Cargando modulos personalizados...")
#carga de modulos personalizados.

implements_loader()

# Crear instancia de Display
display = Display() 

# Configurar mensaje de bienvenida
display.print_welcome_message("¡Hola Mundo!", 3 , clear_screen=True)

# Bucle principal
while True:
    #carga de clase encargada de llamar los scripts personalizados. 
    # Cargar e imprimir el menú
   display.menu_principal()