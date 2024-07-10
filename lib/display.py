# Esta clase está diseñada para entornos similares a terminales y no puede interactuar directamente con la pantalla integrada de la placa TTGO T3 V1.6.1.
from libsys.ssd1306 import SSD1306_I2C
import machine
import time
import json
import sys
import os

# Definir pines de entrada y salida
BUTTON_UP_PIN = 12
BUTTON_DOWN_PIN = 13
BUTTON_SELECT_PIN = 14

# Definir botones
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
        self.iniciar_display()
        self.oled.fill(1)
        self.oled.show()
        time.sleep(1)
        self.limpiar_display()

    
    def iniciar_display(self):
        try: 
            # Inicializar el objeto self.i2c
            self.i2c = machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21))
            self.oled = SSD1306_I2C(128,64,self.i2c)
        except OSError:
            print("Error: No se pudo conectar con el display.")
            sys.exit(1)
        
    def print_welcome_message(self, message, duration_in_seconds, clear_screen=False):
        self.welcome_message = message
        self.welcome_duration = duration_in_seconds
        if self.welcome_message and self.welcome_duration:
            if clear_screen:
                self.limpiar_display()

            lines = self.split_text_into_lines(self.welcome_message, self.oled.width)

            y_offset = (self.oled.height - (len(lines) * 10)) // 2  # Adjust 10 based on the font height
            for i, line in enumerate(lines):
                x_offset = (self.oled.width - len(line) * 8) // 2  # Adjust 8 based on the font width
                self.oled.text(line, x_offset, y_offset + i * 10, 1)

            self.oled.show()
            time.sleep(self.welcome_duration)
            self.limpiar_display()

    def split_text_into_lines(self, text, max_width):
        words = text.split()
        lines = []
        current_line = words[0]

        for word in words[1:]:
            if len(current_line + ' ' + word) * 8 <= max_width:  # Adjust 8 based on the font width
                current_line += ' ' + word
            else:
                lines.append(current_line)
                current_line = word

        lines.append(current_line)
        return lines

    def load_menu(self, items=None):
        if items is None:
            # Load menu items from 'menu.json' file
            try:
                with open('datos/menu.json') as f:
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

    def imprimir_menu(self, items=None):
        self.iniciar_display()
        # Print the menu to the OLED display
        current_item = 0
        menu_items = self.load_menu(items)
        last_item = -1  # Para rastrear el último elemento seleccionado
        start_index = 0  # Índice inicial para el desplazamiento

        while True:
            # Determinar el rango de elementos a mostrar
            end_index = start_index + 4  # Mostrar 5 elementos a la vez
            visible_items = menu_items[start_index:end_index]

            if current_item != last_item:
                self.limpiar_display()
                for i, item in enumerate(visible_items):
                    display_text = item['name']
                    if start_index + i == current_item:
                        self.oled.text(f"> {display_text}", 0, 10 + (i * 16), 1)
                    else:
                        self.oled.text(display_text, 0, 10 + (i * 16), 1)
                self.oled.show()
                last_item = current_item 

            command = yield
            if command == 'UP' and current_item > 0:
                current_item -= 1
                if current_item < start_index:
                    start_index -= 1
            elif command == 'DOWN' and current_item < len(menu_items) - 1:
                current_item += 1
                if current_item >= end_index:
                    start_index += 1
            elif command == 'SELECT':
                selected_item = menu_items[current_item]
                # script_path = selected_item['script'] 
                print("Selected item:", selected_item['name'])
                # print("Executing script:", script_path)
                # self.ejecutar_script(script_path)
                if selected_item['name'] == "WiFi":
                    from scripts import wifi
                    wifi = wifi()
                    wifi.open()

                elif selected_item['name'] == "Bluetooth":
                    from scripts import bluetooth
                    bluetooth = bluetooth()
                    bluetooth.open()

                elif selected_item['name'] == "Archivos":
                    from scripts import archivos
                    archivos = archivos()
                    archivos.open()

                elif selected_item['name'] == "RF":
                    from scripts import rf
                    rf = rf()
                    rf.open()

                elif selected_item['name'] == "Ajustes":
                    from scripts import ajustes
                    ajustes = ajustes()
                    ajustes.open()

                elif selected_item['name'] == "Hostpot Wifi":
                    from scripts import hostpotwifi
                    hostpotwifi = hostpotwifi()
                    hostpotwifi.open()

                else :
                    print("Invalid item selected")

                current_item = 0
                last_item = -1

    def imprimir_opciones(self, items=None):
        self.iniciar_display()
        # Print the menu to the OLED display
        current_item = 0
        menu_items = self.load_menu(items)
        last_item = -1  # Para rastrear el último elemento seleccionado
        start_index = 0  # Índice inicial para el desplazamiento

        while True:
            # Determinar el rango de elementos a mostrar
            end_index = start_index + 4  # Mostrar 5 elementos a la vez
            visible_items = menu_items[start_index:end_index]

            if current_item != last_item:
                self.limpiar_display()
                for i, item in enumerate(visible_items):
                    display_text = item['name']
                    if start_index + i == current_item:
                        self.oled.text(f"> {display_text}", 0, 10 + (i * 16), 1)
                    else:
                        self.oled.text(display_text, 0, 10 + (i * 16), 1)
                self.oled.show()
                last_item = current_item 

            command = yield
            if command == 'UP' and current_item > 0:
                current_item -= 1
                if current_item < start_index:
                    start_index -= 1
            elif command == 'DOWN' and current_item < len(menu_items) - 1:
                current_item += 1
                if current_item >= end_index:
                    start_index += 1
            elif command == 'SELECT':
                selected_item = menu_items[current_item] 
                print("Selected item:", selected_item['name']) 
                current_item = 0
                last_item = -1
                return selected_item

    def ejecutar_script(self, script_path): 
        try:
            with open(script_path, "r") as script_file:
                script_code = script_file.read()
                exec(script_code)
                print(f"Script '{script_path}' executed successfully.")
        except OSError:
            print(f"Error: Script '{script_path}' not found.")
            # si error entonces retorna al menu principal
            self.menu_principal()
        except Exception as e:
            print(f"Error executing script '{script_path}': {e}")
            # si error entonces retorna al menu principal
            self.menu_principal()

    def menu_principal(self):
        #imprime el menu principal
        self.iniciar_display()

        menu_gen = self.imprimir_menu()
        next(menu_gen)  # Iniciar el generador

        print("Para navegar escribe UP, DOWN o SELECT")

        while True:
            command = sys.stdin.readline().strip()
            if command:
                menu_gen.send(command)

    def limpiar_display(self):
        self.oled.fill(0)
        self.oled.show()

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

 

