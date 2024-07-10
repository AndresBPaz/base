import sys

class Wifi:

    menu_wifi = {
        "items": [
            {"name": "Buscar"},
            {"name": "Spam"},
            {"name": "Salir"}
        ]
    }

    def __init__(self):
        pass 
    def open(self):
        print("Opening WiFi")

    def close(self):
        print("Closing WiFi")
        sys.exit(0)