from display import Display 

class Terminal:
    def __init__(self, display):
        self.display = display
        self.terminal_history = []

    def add_to_terminal_history(self, text):
        self.terminal_history.append(text)

    def print_terminal_history(self):
        self.display.iniciar_display()
        display_width, display_height = 128, 64
        max_lines = display_height // 10
        start_index = max(0, len(self.terminal_history) - max_lines)
        for i in range(start_index, len(self.terminal_history)):
            line = self.terminal_history[i]
            y_position = 5 + (i - start_index) * 10
            self.display.oled.text(line, 0, y_position, 1)
        self.display.oled.show()



# Crear instancia de Terminal y añadir historial
# terminal = Terminal(display)
# terminal.add_to_terminal_history("Se ha iniciado el programa.")
# terminal.add_to_terminal_history("Conectando a la red Wi-Fi...")
# terminal.add_to_terminal_history("Conexión a Wi-Fi establecida.")
# terminal.add_to_terminal_history("Leyendo datos del sensor...")

# Imprimir historial de la terminal
# terminal.print_terminal_history()