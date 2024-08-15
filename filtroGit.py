import os # Importa el módulo para interactuar con el sistema operativo 
import json # Importa el módulo json para trabajar con archivos JSON
from colorama import Fore, Style # Importa las clases Fore y Style del módulo colorama para imprimir texto en colores

DATA_FILE="campus_lands.json" # Ruta del archivo JSON donde se almacenarán los datos

def limpiar(): # Función para limpiar la consola
    if os.name == 'nt': # Si el sistema operativo es Windows
        os.system('cls') # Ejecuta el comando 'cls' para limpiar la consola en Windows
    else: # Si el sistema operativo es diferente a Windows (por ejemplo, Linux o macOS)
        os.system('clear') # Ejecuta el comando 'clear' para limpiar la consola

#cargar los archivos desde el json
def cargar(): # Función para cargar los datos desde el archivo JSON
    try: # Intenta abrir el archivo JSON
        with open(DATA_FILE, 'r') as file: # Abre el archivo en modo lectura
            data=json.load(file) # Carga los datos del archivo JSON
    except FileNotFoundError: # Si el archivo no existe
        data={  # Crea un diccionario con los datos iniciales
            "campers": [],
            "trainers": [],
            "coordinador": [],
            "rutas": [],
            "areas": [
                {"nombre":"Area 1", "capacidad_maxima":33, "ruta":None, "campers":[]},  
                {"nombre":"Area 2", "capacidad_maxima":33, "ruta":None, "campers":[]},
                {"nombre":"Area 3", "capacidad_maxima":33, "ruta":None, "campers":[]}
            ],
            "matriculas": [],
        }
    return data # Devuelve los datos cargados o los datos iniciales

# Función para guardar los datos en el archivo JSON
def guardar(data):
    with open(DATA_FILE, 'w' ) as file: # Abre el archivo en modo escritura
        json.dump(data,file, indent=4) # Guarda los datos en el archivo JSON con una indentación de 4 espacios

def decimal(prompt): # Función para solicitar un número decimal al usuario
    while True:
        try:
            value = float(input(prompt))# Solicita un número decimal al usuario
            return value # Devuelve el valor ingresado si es válido
        except ValueError:
            print(Fore.RED + "Entrada inválida. Ingrese un número decimal." + Style.RESET_ALL) # Muestra un mensaje de error si la entrada no es válida

def enteros(prompt): # Función para solicitar un número entero al usuario
    while True:
        try:
            value = int(input(prompt)) # Solicita un número entero al usuario
            return value # Devuelve el valor ingresado si es válido
        except ValueError:
            print(Fore.RED + "Entrada inválida. Ingrese un número entero." + Style.RESET_ALL) # Muestra un mensaje de error si la entrada no es válida

def instrucciones(): # Función para imprimir las instrucciones de uso del programa
    print(Fore.YELLOW + "Instrucciones de uso:" + Style.RESET_ALL)
    print("1. Selecciona una opcion del menú ingresando el número correspondiente.")
    print("2. Sigue las instrucciones en pantalla para completar la acción seleccionada.")
    print("3. Para salir del programa, selecciona la opcion 0.")
    print("")


# Menú principal
while True:
    limpiar() # Limpia la consola
    instrucciones() # Imprimir las instrucciones en la consola
    print(Fore.GREEN + "==== Gestion Academica CampusLands ====" + Style.RESET_ALL)
    print(Fore.YELLOW + "1. Registrar Camper" + Style.RESET_ALL)
    print(Fore.YELLOW + "2. Registrar Trainer" + Style.RESET_ALL)
    print(Fore.YELLOW + "3. Registar Coordinador" + Style.RESET_ALL)
    print(Fore.YELLOW + "4. Crear ruta de entrenamiento" + Style.RESET_ALL)
    print(Fore.YELLOW + "5. Registar notas de campers (coordinador)" + Style.RESET_ALL)
    print(Fore.YELLOW + "6. Asignar campers y traines a rutas" + Style.RESET_ALL)
    print(Fore.YELLOW + "7. Generar reportes" + Style.RESET_ALL)
    print(Fore.YELLOW + "8. Gestionar matriculas" + Style.RESET_ALL)
    print(Fore.YELLOW + "9. Seleccionar horario de trainers" + Style.RESET_ALL)
    print(Fore.RED + "0. Salir" + Style.RESET_ALL)
    print("")

    opcion = enteros(Fore.GREEN + "Eliga una opcion: " + Style.RESET_ALL) # Solicita al usuario que ingrese una opción del menú
    print("-------------------------------")

    if opcion == 0:  # Si la opción es 0, salir del programa
        print(Fore.GREEN + "¡Hasta Luego!" + Style.RESET_ALL)
        break

    elif opcion == 1: # Si la opción es 1, registrar un nuevo camper
        print(Fore.YELLOW + "=== Registrar Camper ===" + Style.RESET_ALL)
        camper = {
            "# de Identificacion" : enteros("Ingrese el numero de CC o TI del camper: "),  
            "nombres" : input("Ingrese el nombre del camper: "),
            "apellidos" : input("Ingrese el apellido del camper: "),
            "direccion" : input("Ingrese la dirección del camper: "),
            "acudiente" : input("Ingrese nombre del acudiente del camper: "),
            "Fijo" : enteros("Ingrese el numero de fijo del camper: "),
            "Telefono" : enteros("Ingrese el numero de telefono del camper: "),
            "estado" : "ingreso",
            "riesgo" : "bajo"
        }
        data = cargar() # Carga los datos existentes
        data["campers"].append(camper) # Agrega el nuevo camper a la lista de campers