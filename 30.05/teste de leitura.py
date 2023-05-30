import tkinter as tk
import pyttsx3

def ler_texto():
    texto = label.cget("text")
    engine.say(texto)
    engine.runAndWait()

root = tk.Tk()

label = tk.Label(root, text="Texto para leitura em voz alta")
label.pack()

button = tk.Button(root, text="Ler texto", command=ler_texto)
button.pack()

engine = pyttsx3.init()

root.mainloop()
