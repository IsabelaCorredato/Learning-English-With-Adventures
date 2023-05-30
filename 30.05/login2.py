import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
from urllib import request
from io import BytesIO
import win32api
from tkinter import font
import subprocess
import tela_barbie
import time
import variaveis
import tela_miranha
##########################################################################################################################################################################################################################################

def login():
    janela = tk.Tk()  # abre a janela
    janela.title("joguinho cabuloso")
    janela.option_add("*Button*takeFocus", 0)

    imagem = Image.open("background.png")
    imagem_de_fundo = ImageTk.PhotoImage(imagem)
    janela.resizable(False, False)  # bloqueia a janela de ser mudada

    botao_en_imagem = Image.open("botao_en.png")
    botao_entrar_imagem = ImageTk.PhotoImage(botao_en_imagem)

    botao_b_imagem = Image.open("botao_bar.png")
    botao_bar_imagem = ImageTk.PhotoImage(botao_b_imagem)

    botao_ha_imagem = Image.open("botao_ha.png")
    botao_homem_imagem = ImageTk.PhotoImage(botao_ha_imagem)


    monitor_largura_x = win32api.GetSystemMetrics(0)
    monitor_altura_y = win32api.GetSystemMetrics(1)

    largura_janela = 1200
    altura_janela = 600

    x_centro = monitor_largura_x // 2
    y_centro = monitor_altura_y // 2

    x_janela = x_centro - (largura_janela // 2)
    y_janela = y_centro - (altura_janela // 2)

    imagem = imagem.resize((largura_janela, altura_janela))

    label_fundo = tk.Label(janela, image=imagem_de_fundo)
    label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

    janela.geometry(f"{largura_janela}x{altura_janela}+{x_janela}+{y_janela}")


    ##################################################################################################





    def barbie():
        global nome
        if caixa_nome.get() != "":
            variaveis.nome = caixa_nome.get()
            time.sleep(0.2)
            janela.destroy()
            tela_barbie.janelab()
            
        else:
            alerta_nome.grid(row=1, column=0, pady=(310, 0), padx=(20, 0))


    def Homem_aranha():
        global nome
        if caixa_nome.get() != "":
            variaveis.nome = caixa_nome.get()
            time.sleep(0.2)
            janela.destroy()
            tela_miranha.janelah()
            
        else:
            alerta_nome.grid(row=1, column=0, pady=(310, 0), padx=(20, 0))



    ###############################################################################################################

        

    fonte_nome = font.Font(size=22)
    cor_rgb = "#CACACA"
    escolha = tk.IntVar()


    caixa_nome = tk.Entry(janela, width=20, font=fonte_nome, bg=cor_rgb,
                        highlightthickness=0, borderwidth=0)  # cria janela de nome
    nome = caixa_nome.grid(row=1, column=0, pady=(219, 0),
                        padx=(40, 0))
    nome = ""

    alerta_nome = tk.Message(
        text="* Por favor, insira um nome antes de proseguir", foreground="red", background=cor_rgb, width=1000, font=("ADVERTURE", 12,))

    alerta_nome.grid_forget()


    botao_homem = tk.Button(janela, text="HM", command=Homem_aranha,
                            background="gray", font=("ADVERTURE", 20,), highlightthickness=0, bd=0, image=botao_homem_imagem, )
    botao_homem.grid(row=1, column=4, padx=(95, 0), pady=(185, 0))


    botao_barbie = tk.Button(janela, text="Barbie", borderwidth=0,
                            background=cor_rgb, font=("ADVERTURE", 20,), bd=0, highlightthickness=0, image=botao_bar_imagem, command=barbie, )
    botao_barbie.grid(row=1, column=5, padx=(199, 0), pady=(184, 0))


    janela.mainloop()
login()