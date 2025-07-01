import tkinter as tk
from tkinter import scrolledtext
import requests

#Esta url se va a cambiar por ngrok mas adelante
BOT_URL = "http://127.0.0.1:5000/webhook"

def enviar_mensage():
    mensaje = entrada.get()
    if not mensaje.strip():
        return
    
    chat.insert(tk.END, f"Tú: {mensaje}\n")
    entrada.delete(0, tk.END)

    try:
        response = requests.post(BOT_URL, json={"mensaje": mensaje})
        if response.status_code == 200:
            respuesta_bot = response.json().get("respuesta", "Sin respuesta")
        else:
            respuesta_bot = "Error al conectarse con el host"
    except Exception as e:
        respuesta_bot = f"Error: {e}"

    chat.insert(tk.END, f"Bot: {respuesta_bot}\n")
    chat.see(tk.END)

ventana = tk.Tk()
ventana.title("Velikan")

chat = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=50, height=20)
chat.pack(padx=10, pady=10)

entrada = tk.Entry(ventana, width=40)
entrada.pack(side=tk.LEFT, padx=(10, 0), pady=10)

boton_enviar = tk.Button(ventana, text="enviar", command=enviar_mensage)
boton_enviar.pack(side=tk.LEFT, padx=10, pady=10)

ventana.mainloop()
