import tkinter as tk
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

window.mainloop()