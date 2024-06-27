## Librerías y módulos utilizados ##
import tkinter as tk  # Importa la librería tkinter para crear interfaces gráficas
import random         # Importa el módulo random para generar elecciones aleatorias
from tkinter import font  # Importa la sublibrería font de tkinter para manejar fuentes de texto

## Variables Globales ##
contador_victorias = 0  # Variable que almacena el número de victorias del jugador

## Función determinar_ganador ##
def determinar_ganador(eleccion_jugador, eleccion_computadora):
    if eleccion_jugador == eleccion_computadora:
        return "Empate"
    elif (eleccion_jugador == "Piedra" and eleccion_computadora == "Tijeras") or \
         (eleccion_jugador == "Papel" and eleccion_computadora == "Piedra") or \
         (eleccion_jugador == "Tijeras" and eleccion_computadora == "Papel"):
        return "¡Ganaste!"
    else:
        return "Perdiste"

## Función play ##
def play(eleccion_jugador):
    global contador_victorias
    eleccion_computadora = random.choice(["Piedra", "Papel", "Tijeras"])
    resultado = determinar_ganador(eleccion_jugador, eleccion_computadora)
    
    if resultado == "¡Ganaste!":
        contador_victorias += 1
    elif resultado == "Perdiste":
        contador_victorias = 0

    contador_label.config(text=f"Victorias: {contador_victorias}")
    result_label.config(text=f"Computadora eligió: {eleccion_computadora}\n{resultado}")
    
    btn_piedra.config(state=tk.DISABLED)
    btn_papel.config(state=tk.DISABLED)
    btn_tijeras.config(state=tk.DISABLED)
    btn_replay.pack(side=tk.LEFT, padx=10)
    btn_quit.pack(side=tk.LEFT, padx=10)

## Función replay ##
def replay():
    result_label.config(text="")
    btn_piedra.config(state=tk.NORMAL)
    btn_papel.config(state=tk.NORMAL)
    btn_tijeras.config(state=tk.NORMAL)
    btn_replay.pack_forget()
    btn_quit.pack_forget()

## Función iniciar_juego ##
def iniciar_juego():
    global contador_victorias
    contador_victorias = 0
    pantalla_inicial.pack_forget()
    pantalla_juego.pack()

## Configuración de la Interfaz Gráfica ##
window = tk.Tk()  # Crea la ventana principal de la aplicación
window.title("Piedra, Papel o Tijeras")  # Establece el título de la ventana
window.geometry("400x300")  # Ajusta el tamaño de la ventana a 400x300 píxeles

## Pantalla inicial ##
pantalla_inicial = tk.Frame(window)  # Crea un marco para la pantalla inicial
pantalla_inicial.pack() 

titulo_font = font.Font(family="Helvetica", size=24, weight="bold")  # Define una fuente para el título
titulo_label = tk.Label(pantalla_inicial, text="Piedra, Papel o Tijeras", font=titulo_font)  # Crea una etiqueta con el título
titulo_label.pack(pady=20)

iniciar_btn = tk.Button(pantalla_inicial, text="Iniciar juego", command=iniciar_juego)  # Crea un botón para iniciar el juego
iniciar_btn.pack(pady=10)  # Empaqueta el botón con un espacio vertical de 10 píxeles

## Pantalla de juego ##
pantalla_juego = tk.Frame(window)  # Crea un marco para la pantalla de juego

contador_label = tk.Label(pantalla_juego, text="Victorias: 0")  # Etiqueta para mostrar el contador de victorias
contador_label.pack(anchor='ne', padx=10, pady=10) 

label = tk.Label(pantalla_juego, text="Elige una opción:")  # Etiqueta para indicar al jugador que elija una opción
label.pack(pady=10) 

btn_piedra = tk.Button(pantalla_juego, text="Piedra", command=lambda: play("Piedra"))  # Botón para elegir "Piedra"
btn_piedra.pack(side=tk.LEFT, padx=10) 

btn_papel = tk.Button(pantalla_juego, text="Papel", command=lambda: play("Papel"))  # Botón para elegir "Papel"
btn_papel.pack(side=tk.LEFT, padx=10)  

btn_tijeras = tk.Button(pantalla_juego, text="Tijeras", command=lambda: play("Tijeras"))  # Botón para elegir "Tijeras"
btn_tijeras.pack(side=tk.LEFT, padx=10)  

result_label = tk.Label(pantalla_juego, text="")  # Etiqueta para mostrar el resultado de la partida
result_label.pack(pady=20) 

btn_replay = tk.Button(pantalla_juego, text="Volver a jugar", command=replay)  # Botón para jugar de nuevo
btn_quit = tk.Button(pantalla_juego, text="Finalizar juego", command=window.quit)  # Botón para finalizar el juego

window.mainloop()  # Ejecuta el bucle principal de la interfaz gráfica
