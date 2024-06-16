import tkinter as tk
import random
def determinar_ganador(eleccion_jugador, eleccion_computadora):
    if eleccion_jugador == eleccion_computadora:
        return "Empate"
    elif (eleccion_jugador == "Piedra" and eleccion_computadora == "Tijeras") or \
         (eleccion_jugador == "Papel" and eleccion_computadora == "Piedra") or \
         (eleccion_jugador == "Tijeras" and eleccion_computadora == "Papel"):
        return "¡Ganaste!"
    else:
        return "Perdiste"

def play(eleccion_jugador):
    eleccion_computadora = random.choice(["Piedra", "Papel", "Tijeras"])
    resultado = determinar_ganador(eleccion_jugador, eleccion_computadora)
    result_label.config(text=f"Computadora eligió: {eleccion_computadora}\n{resultado}")
    btn_piedra.config(state=tk.DISABLED)
    btn_papel.config(state=tk.DISABLED)
    btn_tijeras.config(state=tk.DISABLED)
    btn_replay.pack(side=tk.LEFT, padx=10)
    btn_quit.pack(side=tk.LEFT, padx=10)

def replay():
    result_label.config(text="")
    btn_piedra.config(state=tk.NORMAL)
    btn_papel.config(state=tk.NORMAL)
    btn_tijeras.config(state=tk.NORMAL)
    btn_replay.pack_forget()
    btn_quit.pack_forget()

window = tk.Tk()
window.title("Piedra, Papel o Tijeras")

label = tk.Label(window, text="Elige una opción:")
label.pack(pady=10)
btn_piedra = tk.Button(window, text="Piedra", command=lambda: play("Piedra"))
btn_piedra.pack(side=tk.LEFT, padx=10)
btn_papel = tk.Button(window, text="Papel", command=lambda: play("Papel"))
btn_papel.pack(side=tk.LEFT, padx=10)
btn_tijeras = tk.Button(window, text="Tijeras", command=lambda: play("Tijeras"))
btn_tijeras.pack(side=tk.LEFT, padx=10)
result_label = tk.Label(window, text="")
result_label.pack(pady=20)

btn_replay = tk.Button(window, text="Volver a jugar", command=replay)
btn_quit = tk.Button(window, text="Finalizar juego", command=window.quit)

window.mainloop()
