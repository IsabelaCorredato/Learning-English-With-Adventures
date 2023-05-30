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
import tela_barbie
import variaveis
from tkinter import PhotoImage


def janelab_closet():
    janelab = tk.Tk()  # abre a janelab
    janelab.title("joguinho barbie")

    imagem = Image.open("Barbie Closet.jpg")

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

##################################################################################################################################################################################################
    def avancar1():
        avancar("Sofa", "Board", "Clothes-press", "Cooker")

    def avancar(esc1, esc2, esc3, esc4):
        global escolha1, escolha2, escolha3, escolha4, lugares, repetiir, acertos
        historia.grid_forget()
        avancar_b.grid_forget()
        escolha1 = tk.Button(text=esc1, highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado1)
        escolha2 = tk.Button(text=esc2, highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado1)
        escolha3 = tk.Button(text=esc3, highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=certo1)
        escolha4 = tk.Button(text=esc4, highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado1)
        lugares = tk.Text(background="white", foreground="black",
                          wrap=tk.WORD, font=("ADVERTURE", 15), width=65, height=2)
        # aumentar a caixa
        lugares.insert(
            '1.0', f"Nesse momento nós vamos nos aventurar em um dos meus cômodos preferidos da casa! Está pronto?")
        repetiir = tk.Button(text="Repetir", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=repetir)

        lugares.grid(row=0, column=0, columnspan=4,
                     padx=(200, 0), pady=(180, 0))
        escolha1.grid(row=1, column=1, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha2.grid(row=1, column=2, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha3.grid(row=1, column=3, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha4.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)

        acertos = tk.Text(background="white", foreground="black",
                          wrap=tk.WORD, font=("ADVERTURE", 15), width=40, height=4)
        acertos.insert(
            '1.0', f"Isso mesmo, o guarda-roupa é muito importante para a composição do Closet.")

    def certo1():
        lugares.grid_forget()
        acertos.grid(row=0, column=0, padx=(
            100, 0), pady=(0, 0), columnspan=17)
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        parte3()

    def parte3():
        global escolha1, escolha2, escolha3, escolha4, lugares, repetiir, acertos
        escolha1 = tk.Button(text="Clothes", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=certo2)
        escolha2 = tk.Button(text="Foods", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado2)
        escolha3 = tk.Button(text="Books", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado2)
        escolha3 = tk.Button(text="Stones", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado2)
        lugares = tk.Text(background="white", foreground="black",
                          wrap=tk.WORD, font=("ADVERTURE", 15), width=65, height=2)

        lugares.insert(
            '1.0', f"Agora que já sabe o móvel, pode dizer o que pode ser guardado dentro dele?")
        repetiir = tk.Button(text="Repetir", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=repetir)

        lugares.grid(row=0, column=0, columnspan=4,
                     padx=(200, 0), pady=(180, 0))
        escolha1.grid(row=1, column=1, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha2.grid(row=1, column=2, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha3.grid(row=1, column=3, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha4.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)

        acertos.delete("1.0", "end")
        acertos.insert(
            '1.0', f"Você está entendendo certinho a funcionalidade desse cômodo que amo tanto!!")

    def certo2():
        lugares.grid_forget()
        acertos.grid(row=0, column=0, padx=(
            100, 0), pady=(0, 0), columnspan=17)
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        parte4()

    def parte4():
        global escolha1, escolha2, escolha3, escolha4, lugares, repetiir
        escolha1 = tk.Button(text="Brown", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado3)
        escolha2 = tk.Button(text="Green", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado3)
        escolha3 = tk.Button(text="Gray", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado3)
        escolha4 = tk.Button(text="Pink", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=certo3)
        lugares = tk.Text(background="white", foreground="black",
                          wrap=tk.WORD, font=("ADVERTURE", 15), width=65, height=4)
        lugares.insert(
            '1.0', f"Bom, acho que chegamos a conclusão que eu sou uma fashionista e adoro compor diversos looks. Mas será que você sabe qual a cor que eu mais gosto que minhas roupas tenham?")
        # aumentar a caixa
        repetiir = tk.Button(text="Repetir", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=repetir)

        lugares.grid(row=0, column=0, columnspan=4,
                     padx=(200, 0), pady=(180, 0))
        escolha1.grid(row=1, column=1, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha2.grid(row=1, column=2, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha3.grid(row=1, column=3, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha4.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)
        acertos.delete("1.0", "end")
        acertos.insert(
            '1.0', f"É essa mesma! Você é uma pessoa tão atenciosa!!")
        acertos.configure(height=2)

    def certo3():
        lugares.grid_forget()
        acertos.grid(row=0, column=0, padx=(
            100, 0), pady=(0, 0), columnspan=17)
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        parte5()

    def parte5():
        global escolha1, escolha2, escolha3, escolha4, lugares, repetiir, acertos
        escolha1 = tk.Button(text="Whale", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado4)
        escolha2 = tk.Button(text="Cow", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado4)
        escolha3 = tk.Button(text="Cat", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=certo4)
        escolha4 = tk.Button(text="Lion", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado4)
        lugares = tk.Text(background="white", foreground="black",
                          wrap=tk.WORD, font=("ADVERTURE", 15), width=65, height=4)
        lugares.insert(
            '1.0', f"Eu tenho muitas bolsas guardadas aqui, pois eu adoro esse acessório, toda fashionista precisa de uma! Além disso, eu também posso carregar a minha Marie para os lugares comigo! Qual animal minha Marie é? Você poderia me dizer?")
        # aumentar a caixa
        repetiir = tk.Button(text="Repetir", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=repetir)

        lugares.grid(row=0, column=0, columnspan=4,
                     padx=(200, 0), pady=(180, 0))
        escolha1.grid(row=1, column=1, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha2.grid(row=1, column=2, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha3.grid(row=1, column=3, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha4.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)
        acertos.configure(width=40, height=5)
        acertos.delete("1.0", "end")
        acertos.insert(
            '1.0', f"Acertou, minha Marie é uma gatinha! Obrigada por me acompanhar no meu Closet! Foi muito divertido!!")
        acertos.configure(height=3)

    def certo4():
        global lugares, imagem
        imagem = PhotoImage(file="seta.png")

        lugares.delete("1.0", "end")
        lugares.insert(
            '1.0', f"Vamos para outro lugar da casa agora!")
        lugares.configure(height=1, width=40)
        acertos.delete("1.0", "end")
        lugares.configure(height=2, width=60)
        acertos.grid_forget()
        print("acabou!!!")  # faz essa frase aparecer
        acertos.configure(height=3, width=50)
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        avancar_b = tk.Button(highlightthickness=0,
                              foreground="black", font=("ADVERTURE", 15), command=retornar, image=imagem)
        avancar_b.grid(row=1, column=2, padx=(255, 0), pady=(200, 0))

    def retornar():
        janelab.destroy()
        tela_barbie.janelab()


##################################################################################################################################################################################################

    aluno = variaveis.nome
    imagem = PhotoImage(file="seta.png")
    historia = tk.Text(background="white", foreground="black", wrap=tk.WORD,
                       font=("ADVERTURE", 15), width=70, height=3)
    historia.insert(
        '1.0', f"Bom dia {aluno}, muito obrigada por me acompanhar em minha rotina de muito trabalho e estudo. Estamos aqui para aprender juntos e nos divertirmos, vamos começar?")
    historia.grid(row=0, column=1, pady=(70, 0), padx=(200, 0))

    avancar_b = tk.Button(text="-->", highlightthickness=0,
                          foreground="black", font=("ADVERTURE", 15), command=avancar1, image=imagem)
    avancar_b.grid(row=1, column=2, padx=(255, 0), pady=(200, 0))


##################################################################################################################################################################################################

    def errado1():
        acertos.grid_forget()
        avancar_b.grid_forget()
        lugares.delete("1.0", "end")
        lugares.insert(
            "1.0", "Esse objeto não deve ficar no Closet, vamos tentar de novo?! ")
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        repetiir.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)

    def repetir():
        lugares.grid_forget()
        repetiir.grid_forget()
        avancar1()  # precisa voltar pra antes disso

    def errado2():
        acertos.grid_forget()
        avancar_b.grid_forget()
        lugares.delete("1.0", "end")
        lugares.insert(
            "1.0", "Acho que você não entendeu tão bem quanto eu imaginei a função do guarda-roupa. Acho melhor voltarmos um pouco!")
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        repetiir.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)

    def repetir():
        lugares.grid_forget()
        repetiir.grid_forget()
        avancar1()

    def errado3():
        acertos.grid_forget()
        avancar_b.grid_forget()
        lugares.delete("1.0", "end")
        lugares.insert(
            "1.0", "Acho que você não reparou direito, pois não é essa. Vamos ver de novo.")
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        repetiir.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)

    def repetir():
        lugares.grid_forget()
        repetiir.grid_forget()
        parte3()

    def errado4():
        acertos.grid_forget()
        avancar_b.grid_forget()
        lugares.delete("1.0", "end")
        lugares.insert(
            "1.0", "Esse bicho não dá para carregar dentro de uma bolsa! Tenta de novo.")
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        repetiir.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)

    def repetir():
        lugares.grid_forget()
        repetiir.grid_forget()
        parte4()

    janelab.mainloop()



