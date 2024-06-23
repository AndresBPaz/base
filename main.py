
import ujson

def call_loader():
    with open('loader.py', 'r') as f:
        exec(f.read())

def carga_configuracion():
    # Carga de configuración desde config.json
    with open('datos/config.json', 'r') as f:
        global config
        config = ujson.load(f)

#llama un script personalizado dev.py
def call_dev():
    with open('dev.py', 'r') as f:
        exec(f.read())

# Bucle principal
while True:
    #carga de variables globales.
    carga_configuracion()

    #carga de modulos personalizados.
    call_loader()
