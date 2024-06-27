# Juego de Piedra, Papel o Tijeras

## Autor: Andrew Chávez Hernández 

## Descripción del Juego

Este es un juego  de Piedra, Papel o Tijeras implementado en Python usando la biblioteca tkinter para la interfaz gráfica. El jugador puede elegir entre Piedra, Papel o Tijeras, y jugar contra la computadora. El objetivo es ganar más partidas que la computadora.

## Funcionalidades Principales

**Jugar contra la Computadora:** El jugador puede seleccionar entre Piedra, Papel o Tijeras, y luego ver el resultado de la partida contra la computadora.

**Contador de Victorias:** Se muestra un contador que lleva la cuenta de las victorias del jugador.

**Reiniciar Juego:** Se puede reiniciar el juego para jugar múltiples rondas.

**Interfaz Gráfica Intuitiva:** La interfaz gráfica es sencilla y fácil de usar.

## Cómo Jugar

1. **Inicio del Juego**: Al iniciar el juego desde la pantalla inicial, se muestra la pantalla de juego donde puedes seleccionar tu opción entre Piedra, Papel o Tijeras.
   
2. **Selecciona tu Opción**: Haz clic en los botones correspondientes a "Piedra", "Papel" o "Tijeras" para hacer tu elección.

3. **Resultado**: Después de hacer tu elección, la computadora elegirá aleatoriamente su opción. Se mostrará el resultado (Ganaste, Perdiste o Empate) junto con la elección de la computadora.

4. **Contador de Victorias**: El contador en la esquina superior derecha muestra cuántas partidas has ganado hasta ahora. El contador se reinicia a 0 cada vez que pierdes una partida.

5. **Replay y Finalizar Juego**: Después de cada partida, puedes optar por jugar otra vez o finalizar el juego.

6. **Volver al Inicio**: En cualquier momento, puedes volver a la pantalla inicial para iniciar un nuevo juego desde cero.

## Explicación del Código y Variables

### Importación de Módulos y Librerías

```python
import tkinter as tk
import random
from tkinter import font
```
tkinter: Librería estándar de Python para crear interfaces gráficas.

random: Para generar números aleatorios, utilizado aquí para que la computadora elija entre Piedra, Papel o Tijeras.

tkinter.font: Para manejar las fuentes de texto en la interfaz gráfica.

## Variables Globales
```python
contador_victorias = 0
```
contador_victorias: Almacena el número de victorias del jugador. Se incrementa cuando el jugador gana y se reinicia a 0 cuando el jugador pierde.

## Funciones Principales

determinar_ganador(eleccion_jugador, eleccion_computadora)
```python
def determinar_ganador(eleccion_jugador, eleccion_computadora):
    if eleccion_jugador == eleccion_computadora:
        return "Empate"
    elif (eleccion_jugador == "Piedra" and eleccion_computadora == "Tijeras") or \
         (eleccion_jugador == "Papel" and eleccion_computadora == "Piedra") or \
         (eleccion_jugador == "Tijeras" and eleccion_computadora == "Papel"):
        return "¡Ganaste!"
    else:
        return "Perdiste"
```
Propósito: 
Determina el resultado de la partida basado en las elecciones del jugador y la computadora.

Argumentos:

eleccion_jugador: Elección del jugador (Piedra, Papel o Tijeras).

eleccion_computadora: Elección aleatoria de la computadora.

Devuelve: "Ganaste", "Perdiste" o "Empate" según el resultado de la partida.

## play(eleccion_jugador)
```python
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
```
Propósito: 
Gestiona la lógica del juego cuando el jugador hace una elección.

Argumento:

eleccion_jugador: Elección del jugador (Piedra, Papel o Tijeras).

Acciones:
Genera una elección aleatoria para la computadora.

Determina el resultado usando determinar_ganador.
Actualiza el contador de victorias.

Actualiza las etiquetas en la interfaz gráfica con el resultado.

Deshabilita los botones de elección para evitar selecciones adicionales hasta que se reinicie el juego.

## replay()
```python
def replay():
    result_label.config(text="")
    btn_piedra.config(state=tk.NORMAL)
    btn_papel.config(state=tk.NORMAL)
    btn_tijeras.config(state=tk.NORMAL)
    btn_replay.pack_forget()
    btn_quit.pack_forget()
```
Propósito:

Restablece la interfaz gráfica y permite jugar una nueva partida.

Acciones:

Limpia el texto del resultado anterior.

Habilita nuevamente los botones de elección.

Oculta los botones de "Volver a jugar" y "Finalizar juego" hasta la próxima partida.

## iniciar_juego()
```python

def iniciar_juego():
    pantalla_inicial.pack_forget()
    pantalla_juego.pack()
```
Propósito: 

Cambia de la pantalla inicial a la pantalla de juego.

Acciones:

Oculta la pantalla inicial.

Muestra la pantalla de juego donde se encuentran los botones y etiquetas para jugar.

Configuración de la Interfaz Gráfica

## Ventana Principal

```python

window = tk.Tk()
window.title("Piedra, Papel o Tijeras")
window.geometry("400x300")  # Ajuste de la geometría para hacerla más grande
```
Propósito: 

Crea la ventana principal de la aplicación.
Configuración:

Título de la ventana: 

"Piedra, Papel o Tijeras".

Tamaño de la ventana: 400x300 píxeles.

## Pantallas Inicial y de Juego
```python

pantalla_inicial = tk.Frame(window)
pantalla_juego = tk.Frame(window)
```
Propósito: 

Crear contenedores (frames) para organizar los elementos de la interfaz.

Uso:

pantalla_inicial: Contiene el título y el botón de inicio.

pantalla_juego: Contiene el contador de victorias, opciones de elección (botones) y etiquetas de resultado.

## Elementos de la Interfaz

```python
result_label = tk.Label(pantalla_juego, text="")  # Etiqueta para mostrar el resultado de la partida
result_label.pack(pady=20)
```

Etiquetas: contador_label, result_label

Propósito: Mostrar el número de victorias y el resultado de la partida actual.

Botones: btn_piedra, btn_papel, btn_tijeras, btn_replay, btn_quit, iniciar_btn

Propósito: Permitir al jugador seleccionar Piedra, Papel o Tijeras, jugar de nuevo, finalizar el juego y comenzar una nueva partida.
