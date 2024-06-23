import sys
import importlib.util
import os

# funcion para carga de módulos dinámicamente desde el directorio "lib" sin considerar nombres
def load_module():
    for f in os.listdir("lib"):
        if f.endswith(".py"):
            module_name = f[:-3]
            spec = importlib.util.spec_from_file_location(module_name, os.path.join("lib", f))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            sys.modules[module_name] = module
            print(f"Módulo importado: {module_name}")
                
    # Inicialización de objetos (utilizando módulos cargados dinámicamente)
    try:
        sensor = getattr(sys.modules[module_name], "Sensor")()  # Ejemplo de acceso a clases/funciones desde módulos cargados
        display = getattr(sys.modules[module_name], "Display")()
    except AttributeError:
        print("Error al inicializar objetos. Modulos cargados no contienen las clases/funciones necesarias.")

load_module()