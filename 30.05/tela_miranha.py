import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
from urllib import request
from io import BytesIO
import win32api
from tkinter import font
import subprocess

import math
from tkinter import ttk
import variaveis
import miranha_beco
import miranha_park
import miranha_estacao
import miranha_hospital
from tkinter import PhotoImage
import pyttsx3

# import cozinha_babrie


def janelah():
    janelab = tk.Tk()  # abre a janelab
    janelab.title("joguinho do homem aranha")

    imagem1 = Image.open("tela_do_miranha.png")
    imagem = imagem1.resize((1280, 900))
    imagem_de_fundo = ImageTk.PhotoImage(imagem)


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
        historia.delete("1.0", "end")
        historia.insert(
            "1.0", f'Espero ansiosamente pela sua ajuda, {aluno}!!')
        historia.configure(height=2, width=40)
        historia.grid(row=0, column=1, pady=(340, 0), padx=(260, 0))
        janelab.after(100, falar, "Espero ansiosamente pela sua ajuda, " + aluno + "!!")
        janelab.after(100, falar, "Escolha em qual ambiente deseja começar com o incrível homem-aranha. A estação de trem, O Hospital, O Parque ou o beco")
        avancar_b.grid_forget()
        avancar_b1.grid_forget()
        repetiir.grid_forget()
        # avancar_b.grid(row=1, column=2, padx=(1156, 0), pady=(557, 0))
        cozinha.grid(row=1, column=1, padx=(590, 3), pady=(15, 0))
        closet.grid(row=1, column=1, padx=(430, 3), pady=(15, 0))
        quarto.grid(row=1, column=1, padx=(250, 3), pady=(15, 0))
        escritorio.grid(row=1, column=1, padx=(0, 3), pady=(15, 0))
        lugares.grid(row=0, column=1, padx=(260, 0), pady=(470, 0))

    def avancar1():
        historia.delete("1.0", "end")
        historia.insert("1.0", f"Olá, {aluno}, tudo bem? Eu espero que sim! \nJá que você está aqui me ajudando a fazer tantas coisas. Vamos tentar nos divertir muito nessa jornada de aprendizado por meio de atividades interativas durante a minha vigia diária na cidade. Vamos começar?!")
        avancar_b.grid_forget()
        historia.configure(height=4)
        repetiir.grid_forget()
        avancar_b1.grid(row=1, column=2, padx=(240, 0), pady=(200, 0))
        janelab.after(100, falar, "Olá, " + aluno + ", tudo bem? Eu espero que sim! \nJá que você está aqui me ajudando a fazer tantas coisas. Vamos tentar nos divertir muito nessa jornada de aprendizado por meio de atividades interativas durante a minha vigia diária na cidade. Vamos começar?!")

    def beco():
        janelab.destroy()
        miranha_beco.janelah_beco()

    def hospital():
        janelab.destroy()
        miranha_hospital.janelah_hospital()

    def parque():
        janelab.destroy()
        miranha_park.janelah_park()

    def estacao():
        janelab.destroy()
        miranha_estacao.janelah_estacao()

    #############################################################################################################################################################################################
    aluno = variaveis.nome
    # aluno="blabla"
    historia = tk.Text(foreground="black", wrap=tk.WORD,
                       font=("ADVERTURE", 12), width=84, height=5)
    historia.insert(
        '1.0', f"Em uma manhã muito agitada na cidade de Nova York, o Homem Aranha estava fazendo a sua vigia diária junto com uma pessoa muito especial {aluno} para ajudá-lo a proteger a população. Afinal são muitas ocorrências e decisões, que o deixam muito ocupado, mas acima de tudo, muito feliz por ter companhia e poder ensinar as crianças a lutar por um mundo mais justo aprendendo inglês comigo.")
    historia.grid(row=0, column=1, pady=(415, 0), padx=(60, 0))

    janelab.after(100, falar, "Em uma manhã muito agitada na cidade de Nova York, o Homem Aranha estava fazendo a sua vigia diária junto com uma pessoa muito especial, " + aluno + "para ajudá-lo a proteger a população. Afinal são muitas ocorrências e decisões, que o deixam muito ocupado, mas acima de tudo, muito feliz por ter companhia e poder ensinar as crianças a lutar por um mundo mais justo, aprendendo inglês comigo.")

    repetiir = tk.Button(text="Repetir", highlightthickness=0, background="green",
                         foreground="blue", font=("ADVERTURE", 15), command=avancar)
    repetiir.grid_forget()
    imagem = PhotoImage(file="seta.png")
    avancar_b = tk.Button(text="-->", highlightthickness=0,
                          foreground="black", font=("ADVERTURE", 15), command=avancar1, image=imagem)
    avancar_b.grid(row=1, column=2, padx=(240, 0), pady=(200, 0))
    avancar_b1 = tk.Button(text="-->", highlightthickness=0,
                           foreground="black", font=("ADVERTURE", 15), command=avancar, image=imagem)
    avancar_b1.grid(row=1, column=2, padx=(240, 0), pady=(200, 0))
    avancar_b1.grid_forget()

    cozinha = tk.Button(text="Beco", highlightthickness=0,
                        foreground="black", font=("ADVERTURE", 15), command=beco)

    closet = tk.Button(text="Parque", highlightthickness=0,
                       foreground="black", font=("ADVERTURE", 15), command=parque)

    quarto = tk.Button(text="Hospital", highlightthickness=0,
                       foreground="black", font=("ADVERTURE", 15), command=hospital)

    escritorio = tk.Button(text="Estaçao de trem", highlightthickness=0,
                           foreground="black", font=("ADVERTURE", 15), command=estacao)

    lugares = tk.Text(foreground="black",
                      wrap=tk.WORD, font=("ADVERTURE", 12), width=40, height=3)
    lugares.insert(
        '1.0', f"Escolha em qual ambiente deseja começar com o incrível homem-aranha.")

    janelab.mainloop()
