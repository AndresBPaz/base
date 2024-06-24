# Esta clase está diseñada para entornos similares a terminales y no puede interactuar directamente con la pantalla integrada de la placa TTGO T3 V1.6.1.
from libsys.ssd1306 import SSD1306_I2C
import machine
import time

class Display:

    #variables globales
    i2c, oled = None, None

    def __init__(self):
        self.welcome_message = None  # Mensaje de bienvenida
        self.welcome_duration = None  # Duración del mensaje de bienvenida
        self.terminal_history = []  # Lista vacía para almacenar el historial de la terminal
    
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


    def print_terminal_history(self):

        self.iniciar_display()

        # Get the display size
        display_width, display_height = self.oled.get_size()

        # Limit the number of lines to display based on screen size
        max_lines = display_height - 5  # Subtract space for title bar and border

        # Start from the last line of history
        start_index = max(0, len(self.terminal_history) - max_lines)

        # Scroll through the history and display the lines
        for i in range(start_index, len(self.terminal_history)):
            line = self.terminal_history[i]

            # Calculate position for the current line
            y_position = 5 + (i - start_index) * 10  # Assuming font size is 10 pixels

            # Draw the line on the screen
            self.oled.text(line, 0, y_position, 1)
            self.oled.show()



    # Agregar texto al historial de la terminal
    def add_to_terminal_history(self, text):
        """
        Agrega una línea de texto al historial de la terminal.

        Args:
            text (str): La línea de texto que se agregará al historial de la terminal.
        """
        self.terminal_history.append(text)

    def limpiar_display(self):
        # Limpiar la pantalla
        self.oled.fill(0)
        self.oled.show()

# Establecer el mensaje de bienvenida
# display.set_welcome_message("¡Bienvenido a la placa TTGO T3 V1.6!")

# Establecer la duración del mensaje de bienvenida en 5 segundos
# display.set_welcome_duration(5)

# Mostrar el mensaje de bienvenida
# display.print_welcome_message(clear_screen=True)

# Agregar texto al historial de la terminal
# display.add_to_terminal_history("Se ha iniciado el programa.")
# display.add_to_terminal_history("Conectando a la red Wi-Fi...")
# display.add_to_terminal_history("Conexión a Wi-Fi establecida.")
# display.add_to_terminal_history("Leyendo datos del sensor...")

# Mostrar el historial de la terminal
# display.print_terminal_history()

