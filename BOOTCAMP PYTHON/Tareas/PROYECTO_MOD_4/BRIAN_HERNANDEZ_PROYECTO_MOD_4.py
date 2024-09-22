import requests # Libreria para uso de peticiones HTTP/API
import json # Libreria para trabajar con archivos tipo JSON
import os # Libreria general para crear, editar, etc archivos, carpetas en el OS
import tkinter as tk # Libreria para trabajar con interfaces graficas
from tkinter import messagebox  #uso de cuadros de texto para interfaces
from PIL import Image, ImageTk # Uso y tratamiento de imagenes
from io import BytesIO # metodo para el tratamiento de datos binarios, como imagenes


file_path = os.path.dirname(os.path.abspath(__file__))
pokedex_file = os.path.join(file_path, "pokedex")


# Crear la carpeta "pokedex" si no existe
if not os.path.exists(pokedex_file):
    os.makedirs(pokedex_file)

#Funcion para consultar pokemon por API
def get_pokeapi(nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    
    try:
        answ = requests.get(url)

        # Manejar diferentes códigos de respuesta
        if answ.status_code == 200:
            data = answ.json()
            return data
        elif answ.status_code == 404:
            messagebox.showerror("Error", "Pokémon no encontrado. Por favor, introduce un nombre válido.")
        elif answ.status_code == 500:
            messagebox.showerror("Error", "Error en el servidor. Inténtalo más tarde.")
        else:
            messagebox.showerror("Error", f"Ocurrió un error: {answ.status_code}. Intenta de nuevo.")
    
    # Excepciones para problemas de conexion
    except requests.exceptions.ConnectionError:
        messagebox.showerror("Error", "Error de conexión. Verifica tu conexión a internet e intenta nuevamente.")
    except requests.exceptions.Timeout:
        messagebox.showerror("Error", "La solicitud a la API ha demorado demasiado. Intenta nuevamente.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Ocurrió un error inesperado: {e}")
    
    return None

#Funcion para recorrer los movimientos del pokemon y almacenarlos
def get_moves(data):
    moves = []
    for move in data['moves']:
        moves.append(move['move']['name'])
    return moves

#Funcion para recorrer las habilidades del pokemon y almacenarlos
def get_abilities(data):
    abilities = []
    for ability in data['abilities']:
        abilities.append(ability['ability']['name'])
    return abilities

#Funcion para mostrar la informacion del pokemon
def show_info(data):
    name = data['name']
    weight = data['weight']
    height = data['height']
    types = [tipo['type']['name'] for tipo in data['types']]
    picture_url = data['sprites']['front_default']

    # Obtener movimientos y habilidades usando las funciones creadas
    moves = get_moves(data)
    abilities = get_abilities(data)

    return {
        "nombre": name,
        "peso": weight,
        "altura": height,
        "movimientos": moves,
        "habilidades": abilities,
        "tipos": types,
        "imagen": picture_url
    }
#Funcion para guardar en json la informacion del pokemon

def save_info(name, data):
    file = os.path.join(pokedex_file, f"{name.lower()}.json")
    with open(file, "w") as f:
        json.dump(data, f, indent=4)
    messagebox.showinfo("Guardado", f"La información de {name} ha sido guardada en {file}")

#Funcion general para buscar pokemon
def search_pokemon(event=None):
    pokemon_name = pokemon_entry.get()
    data = get_pokeapi(pokemon_name)

    if data:
        info = show_info(data)
        show_result(info)
        save_info(pokemon_name, info)
    else:
        messagebox.showerror("Error", "El Pokémon no existe. Por favor, introduce un nombre válido.")

#Funcion para mostrar info en interfaz
def show_result(info):
    text_result.config(state=tk.NORMAL)
    text_result.delete(1.0, tk.END)
    
    # Mostrar info en ventana
    text_result.insert(tk.END, f"Nombre: {info['nombre']}\n")
    text_result.insert(tk.END, f"Peso: {info['peso']}\n")
    text_result.insert(tk.END, f"Altura: {info['altura']}\n")
    text_result.insert(tk.END, f"Movimientos: {', '.join(info['movimientos'][:5])}...\n")
    text_result.insert(tk.END, f"Habilidades: {', '.join(info['habilidades'])}\n")
    text_result.insert(tk.END, f"Tipos: {', '.join(info['tipos'])}\n")
    
    # Mostrar la imagen del pokemon
    imagen_url = info['imagen']
    if imagen_url:
        file_answ = requests.get(imagen_url)
        pokemon_picture = Image.open(BytesIO(file_answ.content))
        pokemon_picture = pokemon_picture.resize((120, 120), Image.Resampling.LANCZOS) # buscar mas documentacion
        pokemon_picture = ImageTk.PhotoImage(pokemon_picture)
        picture_tag.config(image=pokemon_picture)
        picture_tag.image = pokemon_picture  # Evita que la imagen se elimine al depurar el proceso

    text_result.config(state=tk.DISABLED)

# Funcion para limpiar ventana
def clean_window():
    pokemon_entry.delete(0,tk.END)
    text_result.config(state=tk.NORMAL)
    text_result.delete(1.0,tk.END)
    text_result.config(state=tk.DISABLED)
    picture_tag.config(image='')
    
    

# Crear la ventana principal usando libreria tkinter nativa de python
window = tk.Tk()
window.title("Pokedex")
window.geometry("400x500")

# Solicitar al usuario el nombre del pokemon a buscar
tag_name = tk.Label(window, text="Introduce el nombre de un Pokémon:")
tag_name.pack(pady=10)
pokemon_entry = tk.Entry(window)
pokemon_entry.pack(pady=5)
pokemon_entry.bind("<Return>",search_pokemon)

# Agrupar botones

frame_buttons = tk.Frame(window)
frame_buttons.pack(pady=10)

# Boton de busqueda
search_button = tk.Button(frame_buttons, text="Buscar", command=search_pokemon)
search_button.pack(side=tk.LEFT, padx=5)

# Boton para limpiar ventana
clean_button = tk.Button(frame_buttons,text="Limpiar",command=clean_window)
clean_button.pack(side=tk.LEFT,padx=5)

# Mostrar info obtenida de la busqueda
text_result = tk.Text(window, height=10, width=40, state=tk.DISABLED)
text_result.pack(pady=10)

# Etiqueta de la imagen del pokemon obtenido
picture_tag = tk.Label(window)
picture_tag.pack(pady=10)

# Iniciar la ventana
window.mainloop()



