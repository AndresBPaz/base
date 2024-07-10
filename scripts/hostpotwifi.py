from lib.apwifi import apwifi
from lib.webserver import MiServidorWeb
import webrepl_setup
import webrepl

class hostpotwifi:
    def __init__(self):
        pass
    
    def open(self):
        print("Opening hotspot wifi")
        self.create_ap()
        print("Wi-Fi hotspot created:", apwifi.SSID)
        print("Opening Webserver")
        self.create_webserver()
        print("Webserver created")
        print("Opening Webrepl")
        self.create_webrepl()
        print("Webrepl created")

    def close(self):
        print("Closing hotspot wifi")

    def create_ap(self):
        wifi_ap = apwifi()
        wifi_ap.create_ap()  # Creates the Wi-Fi hotspot
        print("Wi-Fi hotspot created:", apwifi.SSID)

    def create_webserver(self):
        mi_servidor = MiServidorWeb()
        mi_servidor.ejecutar()

    def create_webrepl(self):
        webrepl.start(password='12345678')
        

