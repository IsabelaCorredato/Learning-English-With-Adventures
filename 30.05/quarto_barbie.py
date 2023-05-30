import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
from urllib import request
from io import BytesIO
import win32api
from tkinter import font
import subprocess
# import login2
import math
from tkinter import ttk
import variaveis
from tkinter import PhotoImage
# import tela_barbie
import pyttsx3


def janelab_quarto():
    janelab = tk.Tk()  # abre a janelab
    janelab.title("joguinho barbie")

    imagem = Image.open("Quarto da Barbie.jpg")

    imagem_de_fundo = ImageTk.PhotoImage(imagem)

    janelab.resizable(False, False)

    monitor_largura_x = win32api.GetSystemMetrics(0)
    monitor_altura_y = win32api.GetSystemMetrics(1)
    largura_janelab = 1280
    altura_janelab = 900
    x_centro = monitor_largura_x // 2
    y_centro = monitor_altura_y // 2
    x_janelab = x_centro - (largura_janelab // 2)
    y_janelab = y_centro - (altura_janelab // 2)

    label_fundo = tk.Label(janelab, image=imagem_de_fundo)
    label_fundo.place(x=0, y=0, relwidth=1, relheight=1)
    janelab.geometry(
        f"{largura_janelab}x{altura_janelab}+{x_janelab}+{y_janelab}")

    engine = pyttsx3.init()
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0"
    engine.setProperty("voice", voice_id)

##################################################################################################################################################################################################

    def falar(texto):
        engine.say(texto)
        engine.runAndWait()

    def avancar1():
        avancar("bed", "Cooker", "Refrigaretor", "Board")

    def avancar(esc1, esc2, esc3, esc4):
        global escolha1, escolha2, escolha3, escolha4, lugares, repetiir, acertos
        historia.grid_forget()
        avancar_b.grid_forget()
        escolha1 = tk.Button(text=esc1, highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=certo1)
        escolha2 = tk.Button(text=esc2, highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado)
        escolha3 = tk.Button(text=esc3, highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado)
        escolha4 = tk.Button(text=esc4, highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado)
        lugares = tk.Text(foreground="black",
                          wrap=tk.WORD, font=("ADVERTURE", 12), width=50, height=2)
        lugares.insert('1.0', f"Então, qual móvel é típico da Bedroom?")
        repetiir = tk.Button(text="Repetir", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=repetir)

        lugares.grid(row=0, column=0, columnspan=4,
                     padx=(200, 0), pady=(470, 0))
        escolha1.grid(row=1, column=1, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha2.grid(row=1, column=2, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha3.grid(row=1, column=3, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha4.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)

        acertos = tk.Text(foreground="black",
                          wrap=tk.WORD, font=("ADVERTURE", 12), width=40, height=4)

    def certo1():
        acertos.grid(row=0, column=0, padx=(100, 0),
                     pady=(20, 0), columnspan=17)
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        lugares.grid_forget()

        parte3()

    def parte3():
        global escolha1, escolha2, escolha3, escolha4, lugares, repetiir, acertos
        escolha1 = tk.Button(text="Sleeping", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=certo2)
        escolha2 = tk.Button(text="Cleaning", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado)
        escolha3 = tk.Button(text="working", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado)
        escolha4 = tk.Button(text="playing", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado)
        lugares = tk.Text(foreground="black",
                          wrap=tk.WORD, font=("ADVERTURE", 12), width=50, height=2)

        lugares.insert(
            '1.0', f"E como nós acessamos a Terra dos Sonhos em cima da Bed dentro do Bedroom?")
        repetiir = tk.Button(text="Repetir", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=repetir)

        lugares.grid(row=0, column=0, columnspan=4,
                     padx=(200, 0), pady=(470, 0))
        escolha1.grid(row=1, column=1, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha2.grid(row=1, column=2, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha3.grid(row=1, column=3, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha4.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)

        acertos.delete("1.0", "end")
        acertos.insert(
            '1.0', f"Isso mesmo {aluno}, a existência da Bed no quarto é o que faz desse ambiente um lugar tão maravilhoso para a Terra dos Sonhos")

    def certo2():
        acertos.grid(row=0, column=0, padx=(100, 0),
                     pady=(20, 0), columnspan=17)
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        lugares.grid_forget()
        parte4()

    def parte4():
        global escolha1, escolha2, escolha3, escolha4, lugares, repetiir
        escolha1 = tk.Button(text="Spoon", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado3)
        escolha2 = tk.Button(text="Pillow", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=certo3)
        escolha3 = tk.Button(text="Book", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado3)
        escolha4 = tk.Button(text="T-Shirt", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado3)
        lugares = tk.Text(foreground="black",
                          wrap=tk.WORD, font=("ADVERTURE", 12), width=50, height=2)
        lugares.insert(
            '1.0', "E qual é o objetivo que nos auxilia a Sleeping bem na Bed?")
        repetiir = tk.Button(text="Repetir", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=repetir1)

        lugares.grid(row=0, column=0, columnspan=4,
                     padx=(200, 0), pady=(470, 0))
        escolha1.grid(row=1, column=1, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha2.grid(row=1, column=2, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha3.grid(row=1, column=3, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha4.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)
        acertos.delete("1.0", "end")
        acertos.insert(
            '1.0', f"Isso mesmo, você conseguiu entender qual a função desse objeto e porquê ele é tão importante na nossa vida!")

    def certo3():
        acertos.grid(row=0, column=0, padx=(100, 0),
                     pady=(20, 0), columnspan=17)
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        lugares.grid_forget()
        parte5()

    def parte5():
        global escolha1, escolha2, escolha3, escolha4, lugares, repetiir, acertos
        escolha1 = tk.Button(text="Blue", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado)
        escolha2 = tk.Button(text="pink", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=certo4)
        escolha3 = tk.Button(text="Yellow", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado)
        escolha4 = tk.Button(text="Black", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado)

        lugares = tk.Text(foreground="black",
                          wrap=tk.WORD, font=("ADVERTURE", 12), width=50, height=3)
        lugares.insert(
            '1.0', f"A minha Bed e o meu Bedroom são pintados da minha cor preferida. Você saberia me dizer que cor é essa?")
        repetiir = tk.Button(text="Repetir", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=repetir2)

        lugares.grid(row=0, column=0, columnspan=4,
                     padx=(200, 0), pady=(470, 0))
        escolha1.grid(row=1, column=1, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha2.grid(row=1, column=2, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha3.grid(row=1, column=3, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha4.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)
        acertos.configure(width=40, height=5)
        acertos.delete("1.0", "end")
        acertos.insert(
            '1.0', f"Acertou! O travesseiro ajuda bastante a ter uma boa noite de sono! Você está compreendendo muito bem a situação")

    def certo4():
        lugares.grid_forget()
        acertos.delete("1.0", "end")
        acertos.insert(
            '1.0', f"Você analisou o meu Bedroom inteirinho muito bem! Parabéns! Você é muito detalhista! Agora que acabamos aqui, podemos continuar nossa tour pela minha casa.")
        print("acabou essa merda buceta")
        acertos.grid(row=0, column=0, padx=(100, 0),
                     pady=(20, 0), columnspan=17)
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()


##################################################################################################################################################################################################

    aluno = variaveis.nome

    historia = tk.Text(foreground="black", wrap=tk.WORD,
                       font=("ADVERTURE", 12), width=70, height=4)
    historia.insert(
        '1.0', f"Bom dia {aluno}! \nMuito obrigada por vim me acompanhar na minha rotina! \nTenho diversas coisas para fazermos juntos no meu *Bedroom*. Vamos la?")
    historia.grid(row=0, column=1, pady=(415, 0), padx=(60, 0))

    imagem = PhotoImage(file="seta.png")
    avancar_b = tk.Button(text="-->", highlightthickness=0,
                          foreground="black", font=("ADVERTURE", 15), command=avancar1, image=imagem)
    avancar_b.grid(row=1, column=2, padx=(255, 0), pady=(200, 0))

##################################################################################################################################################################################################

    def errado():
        acertos.grid_forget()
        avancar_b.grid_forget()
        lugares.delete("1.0", "end")
        lugares.insert("1.0", "VC ERROU, PORRA")
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        repetiir.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)

    def errado2():
        acertos.grid_forget()
        avancar_b.grid_forget()
        lugares.delete("1.0", "end")
        lugares.insert("1.0", "VC ERROU, PORRA")
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        repetiir.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)

    def errado3():
        acertos.grid_forget()
        avancar_b.grid_forget()
        lugares.delete("1.0", "end")
        lugares.insert("1.0", "VC ERROU, PORRA")
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        repetiir.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)

    def errado4():
        acertos.grid_forget()
        avancar_b.grid_forget()
        lugares.delete("1.0", "end")
        lugares.insert("1.0", "VC ERROU, PORRA")
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        repetiir.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)

    def repetir():
        lugares.grid_forget()
        repetiir.grid_forget()
        avancar1()

    def repetir1():
        lugares.grid_forget()
        repetiir.grid_forget()
        parte3()

    def repetir2():
        lugares.grid_forget()
        repetiir.grid_forget()
        parte4()

    janelab.mainloop()



