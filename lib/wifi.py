#esta libreria facilitara el uso del wifi de la placa
import network
import time

class Wifi:
    def __init__(self, SSID = "", PASSWORD = ""):
        #carga el ssid y la contraseña de la red
        ssid = SSID
        password = PASSWORD

        if ssid != "" or password != "":
            self.connectwifi(ssid, password)

        # Check if connection was successful and update attributes
        if self.is_connected():
            self.IP = self.sta.ifconfig()[0]
            self.MAC = self.sta.config('mac')
            self.SSID = self.sta.config('essid')
            self.CHANNEL = self.sta.config('channel')
            self.AUTHMODE = self.sta.config('authmode')
            self.HIDDEN = self.sta.config('hidden')
            self.RSSI = self.sta.status('rssi')
            print("Conectado a la red WiFi con IP:", self.IP)
        else:
            print("Error al conectar a la red WiFi")

    # Función para conectar a la red Wi-Fi
    def connectwifi(ssid, password):
        sta = network.WLAN(network.STA_IF)
        sta.active(True)
        sta.connect(ssid, password)
        while not sta.is_connected():
            time.sleep(0.5)
        print("Conectado a Wi-Fi:", sta.ifconfig()[0])
    
    def is_connected(self):
        """
        Checks if the Wi-Fi connection is active.

        Returns:
            bool: True if connected, False otherwise.
        """

        return self.sta.is_connected()

        