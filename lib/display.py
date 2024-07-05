# Esta clase está diseñada para entornos similares a terminales y no puede interactuar directamente con la pantalla integrada de la placa TTGO T3 V1.6.1.
from libsys.ssd1306 import SSD1306_I2C
import machine
import time
import json

BUTTON_UP_PIN = 12
BUTTON_DOWN_PIN = 13
BUTTON_SELECT_PIN = 14

BUTTON_UP = 0x01
BUTTON_DOWN = 0x02
BUTTON_SELECT = 0x04


class Display:

    #variables globales
    i2c, oled = None, None

    def __init__(self):
        self.i2c = None
        self.oled = None
        self.welcome_message = None  # Mensaje de bienvenida
        self.welcome_duration = None  # Duración del mensaje de bienvenida
        self.terminal_history = []  # Lista vacía para almacenar el historial de la terminal
        self.button_up = machine.Pin(BUTTON_UP_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
        self.button_down = machine.Pin(BUTTON_DOWN_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
        self.button_select = machine.Pin(BUTTON_SELECT_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
    
    def iniciar_display(self):
        # Inicializar el objeto self.i2c
        self.i2c = machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21))
        self.oled = SSD1306_I2C(128,64,self.i2c)

    def set_welcome_message(self, message):
        """
        Establece el mensaje de bienvenida que se mostrará al iniciar el programa.

        Args:
            message (str): El mensaje de bienvenida a mostrar.
        """
        self.welcome_message = message

    def set_welcome_duration(self, duration_in_seconds):
        """
        Establece la duración del mensaje de bienvenida en segundos.

        Args:
            duration_in_seconds (float): La duración del mensaje de bienvenida en segundos.
        """
        self.welcome_duration = duration_in_seconds

    def print_welcome_message(self, clear_screen=False):
        if self.welcome_message and self.welcome_duration:

            self.iniciar_display()

            # Clear the screen if requested
            if clear_screen:
                self.limpiar_display()

            # Display the welcome message centered
            self.oled.text(self.welcome_message, 32, 32, 1)
            self.oled.show()

            # Wait for the specified duration
            time.sleep(self.welcome_duration)

            #limpiar display
            self.limpiar_display()

    def limpiar_display(self):
        # Limpiar la pantalla
        self.oled.fill(0)
        self.oled.show()

    def load_menu(self, items=None):
        """
        Loads menu items from either a JSON file or a provided dictionary.

        Args:
            items (dict, optional): A dictionary containing menu items.
                If None (default), loads menu items from 'menu.json'.

        Returns:
            list: A list of menu items loaded from the specified source.

        Raises:
            ValueError: If both 'items' and 'menu.json' file are missing.
        """

        if items is None:
            # Load menu items from 'menu.json' file
            try:
                with open('menu.json') as f:
                    data = json.load(f)
                menu_items = data['items']
            except OSError:
                raise ValueError("Menu file 'menu.json' not found. Please provide a dictionary or create the file.")
        else:
            # Use provided dictionary as menu items
            if not isinstance(items, dict):
                raise ValueError("Invalid argument: 'items' must be a dictionary.")
            menu_items = items['items']

        return menu_items

    def imprimir_menu(self):
        # Print the menu to the OLED display
        current_item = 0
        menu_items = self.load_menu()
        while True:
            # Clear the OLED display
            self.limpiar_display()

            # Print the menu title
            # oled.text(data['title'], 0, 0, 1)

            # Print the menu items
            for i, item in enumerate(menu_items):
                if i == current_item:
                    # Print the current item in bold
                    #self.oled.text(item, 0, 10 + (i * 16), 1)
                    self.oled.text(f"> {item}", 0, 10 + (i * 16), 1)

                else:
                    # Print the other items in normal font
                    #self.oled.text(item, 0, 10 + (i * 16), 0)
                    self.oled.text(item, 0, 10 + (i * 16), 1)

            # Display the OLED
            self.oled.show()

            # Wait for a button press
            buttons = self.get_buttons()

            # Handle the button presses
            if buttons & BUTTON_UP:
                # Move the current item up one if it is not already at the top
                if current_item > 0:
                    current_item -= 1
            elif buttons & BUTTON_DOWN:
                # Move the current item down one if it is not already at the bottom
                if current_item < len(menu_items) - 1:
                    current_item += 1
            elif buttons & BUTTON_SELECT:
                # Select the current item
                print("Selected item:", menu_items[current_item])

                # Break out of the loop
                break

            # Wait for a short period of time
            time.sleep(0.1)
            
    def get_buttons(self):
        buttons = 0
        if not self.button_up.value():
            buttons |= BUTTON_UP
        if not self.button_down.value():
            buttons |= BUTTON_DOWN
        if not self.button_select.value():
            buttons |= BUTTON_SELECT
        return buttons
    
# Crear instancia de Display
#display = Display()

# Configurar mensaje de bienvenida
#display.set_welcome_message("¡Bienvenido a la placa TTGO T3 V1.6!")
#display.set_welcome_duration(5)
#display.print_welcome_message(clear_screen=True)

 

