import json
from lib.display import Display 
import sys

def implements_loader():
    with open('implements.py', 'r') as f:
        exec(f.read())
        
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