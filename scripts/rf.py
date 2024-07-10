import json

class rf:
    def __init__(self):
        print("RF")
        
        with open('/datos/config.json', 'r') as f:
            self.config = json.load(f)

        self.TTGO_MOSI = self.config["TTGO_MOSI"]
        self.TTGO_SCLK = self.config["TTGO_SCLK"]
        self.TTGO_CS = self.config["TTGO_CS"]
        self.TTGO_DIO = self.config["TTGO_DIO"]
        self.TTGO_RST = self.config["TTGO_RST"]

    def open(self):
        print("Opening RF")
        