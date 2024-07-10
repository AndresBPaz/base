from lib.FileManager import FileManager
from lib.display import Display 

class Archivos:
    def __init__(self):
        self.file_manager = FileManager()
    
    def open(self):
        print("Archivos")
        self.iniciar_archivos()

    def iniciar_archivos(self):
        # imprime en pantalla usando Display.imprimir_menu
        # items raiz y la sd card.  
        
        FileManager_menu = {
            "title": "Archivos",
            "items": [
                {"name": "Raiz", "script": "raiz.py"},
                {"name": "SD Card", "script": "sdcard.py"},
                {"name": "Salir", "script": "salir.py"}
            ]
        } 

        display = Display()
        opcion = display.imprimir_opciones(FileManager_menu) 

        print("Opción seleccionada:", opcion)

        match(opcion):
            case "Raiz":
                print("\nFiles in current directory:")
                self.change_dir("/")
                self.list_files("/")
                files = self.list_files("/")
                for file in files:
                    print(file)

            case "SD Card":
                print("\nFiles in SD card:")
                self.change_dir("/sd")
                self.list_files("/sd")
                files = self.list_files("/sd")
                for file in files:
                    print(file)

            case "Salir":
                print("Saliendo...")
                return
                    
            case _ : 
                print("Opción inválida")

    def list_files(self, path):
        return self.file_manager.list_files(path)

    def change_dir(self, path):
        self.file_manager.change_dir(path)

    def go_back(self):
        self.file_manager.go_back()

    def execute_script(self, script_name):
        self.file_manager.execute_script(script_name)

# Ejemplo de uso
archivos = Archivos()