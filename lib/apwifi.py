import network
import time
import json

class apwifi:
    """
    Class to manage Wi-Fi hotspot creation and configuration on your MicroPython device.

    Example Usage:
    wifi_ap = WifiAP("my_hotspot", "my_password")
    wifi_ap.create_ap()  # Creates the Wi-Fi hotspot
    print("Wi-Fi hotspot created:", wifi_ap.SSID)
    """

    def __init__(self):
        
        with open('/datos/config.json', 'r') as f:
            self.config = json.load(f)
        
        """
        Initializes the WifiAP object with the SSID and password for the hotspot.

        Args:
            ssid (str): The name of the Wi-Fi hotspot you want to create.
            password (str): The password for the Wi-Fi hotspot.
        """
        self.SSID = self.config["ssid"]
        self.password = self.config["password"]

    def create_ap(self):
        """
        Creates the Wi-Fi hotspot using the specified SSID and password.
        """

        # Configure Wi-Fi interface as access point (AP)
        ap = network.WLAN(network.AP_IF)
        ap.active(True)
        ap.config(essid=self.SSID, password=self.password)
        ap.config(essid="my_hotspot", password="mypassword")

        # Verify hotspot creation
        if ap.active():
            print("Wi-Fi hotspot created:", self.SSID)
        else:
            print("Failed to create Wi-Fi hotspot")



# example usage
# wifi_ap = apwifi()
# wifi_ap.create_ap()  # Creates the Wi-Fi hotspot
# print("Wi-Fi hotspot created:", apwifi.SSID)
