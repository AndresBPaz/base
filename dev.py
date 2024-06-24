# desde el directorio scripts llama los scripts personalizados en modo multitarea para la placa
# para cada script se puede crear un nuevo hilo. 

import _thread
from scripts.led import Led
from scripts.hostpotwifi import hostpotwifi

def llamar_Scripts():
    # llama la clase led.py en un nuevo hilo 
    try:
        # llama la clase led.py en un nuevo hilo
        _thread.start_new_thread(Led(), ())

        #Lama la clase para iniciar el wifi ap
        _thread.start_new_thread(hostpotwifi(), ())


    except Exception as e:
        print(f"Error creating thread: {e}")

llamar_Scripts()
