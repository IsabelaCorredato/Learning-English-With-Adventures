import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
from urllib import request
from io import BytesIO
import win32api
from tkinter import font
import subprocess
import variaveis
import math
from tkinter import ttk
import variaveis
from tkinter import PhotoImage
import cozinha_babrie
import quarto_barbie
import closet_teste
import escritório_teste
import pyttsx3


def janelab():
    janelab = tk.Tk()  # abre a janelab
    janelab.title("joguinho barbie")

    imagem = Image.open("Casa da Barbie.jpg")

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

    #############################################################################################################################################################################################

    def falar(texto):
        engine.say(texto)
        engine.runAndWait()

    def avancar():
        historia.grid_forget()
        avancar_b.grid_forget()
        # avancar_b.grid(row=1, column=2, padx=(1156, 0), pady=(557, 0))
        cozinha.grid(row=1, column=1, padx=(540, 3), pady=(20, 0))
        closet.grid(row=1, column=1, padx=(370, 3), pady=(20, 0))
        quarto.grid(row=1, column=1, padx=(200, 3), pady=(20, 0))
        escritorio.grid(row=1, column=1, padx=(0, 3), pady=(20, 0))
        lugares.grid(row=0, column=1, padx=(260, 0), pady=(470, 0))

    def escritorio():
        janelab.destroy()
        escritório_teste.janelab_escritorio()

    def quarto():
        janelab.destroy()
        quarto_barbie.janelab_quarto()

    def cozinha():
        janelab.destroy()
        cozinha_babrie.janelab_cozinha()

    def closet():
        janelab.destroy()
        closet_teste.janelab_closet()

    #############################################################################################################################################################################################
    aluno = variaveis.nome
    # aluno="blabla"
    historia = tk.Text(foreground="black", wrap=tk.WORD,
                       font=("ADVERTURE", 12), width=84, height=5)
    historia.insert('1.0', f"Olá, {aluno}, tudo bem? \nEu espero que sim! \nJá que você está aqui realizando meu sonho, vamos tentar nos divertir muito nessa jornada de aprendizado por meio de atividades interativas durante a minha rotina diária. Vamos lá?!")
    historia.grid(row=0, column=1, pady=(415, 0), padx=(60, 0))

    janelab.after(100, falar, "Olá, " + aluno + ", tudo bem? Eu espero que sim! Já que você está aqui realizando meu sonho, vamos tentar nos divertir muito nessa jornada de aprendizado por meio de atividades interativas durante a minha rotina diária. Vamos lá?!")

    # historia = tk.Message(text=f"ola {aluno}, seja muito bem vindo!!  ",
    #                       foreground="black", font=("ADVERTURE", 12,), width=750, pady=60,anchor="nw")
    # historia.grid(row=0, column=1, pady=(415, 0), padx=(60, 0))
    imagem = PhotoImage(file="seta.png")
    avancar_b = tk.Button(text="-->", highlightthickness=0,
                          foreground="black", font=("ADVERTURE", 15), command=avancar, image=imagem)
    avancar_b.grid(row=1, column=2, padx=(250, 0), pady=(230, 0))
    cozinha = tk.Button(text="cozinha", highlightthickness=0,
                        foreground="black", font=("times", 15), command=cozinha)

    closet = tk.Button(text="closet", highlightthickness=0,
                       foreground="black", font=("times", 15), command=closet)

    quarto = tk.Button(text="quarto", highlightthickness=0,
                       foreground="black", font=("times", 15), command=quarto)

    escritorio = tk.Button(text="escritorio", highlightthickness=0,
                           foreground="black", font=("times", 15), command=escritorio)

    lugares = tk.Text(foreground="black",
                      wrap=tk.WORD, font=("ADVERTURE", 12), width=40, height=2)
    lugares.insert(
        '1.0', f"Deseja começar por qual ambiente? \nEscolha já o lugar em inglês")
    
    janelab.after(100, falar, "Deseja começar por qual ambiente? Escolha já o lugar em inglês")
    janelab.after(100, falar, "O Office? O Bedroom? O Closet? ou A Kitchen?")

    janelab.mainloop()




# testar
