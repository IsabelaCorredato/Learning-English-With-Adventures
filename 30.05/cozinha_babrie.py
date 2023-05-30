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
import tela_barbie
import pyttsx3
from tkinter import PhotoImage

# import tela_barbie

def janelab_cozinha():
    janelab = tk.Tk()  # abre a janelab
    janelab.title("joguinho barbie")

    imagem = Image.open("Cozinha da Barbie.jpg")

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

    def avancar1():
        avancar("Bed", "Clothes-press", "Cooker", "Board")

    def avancar(esc1, esc2, esc3, esc4):
        global escolha1, escolha2, escolha3, escolha4, lugares, repetiir, acertos
        historia.grid_forget()
        avancar_b.grid_forget()
        escolha1 = tk.Button(text=esc1, highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado)
        escolha2 = tk.Button(text=esc2, highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado)
        escolha3 = tk.Button(text=esc3, highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=certo1)
        escolha4 = tk.Button(text=esc4, highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado)
        lugares = tk.Text(background="white", foreground="black",
                          wrap=tk.WORD, font=("ADVERTURE", 15), width=40, height=2)
        lugares.insert('1.0', f"Então, qual móvel é típico da Kitchen?")

        janelab.after(100, falar, "Então, qual móvel é típico da Kitchen?")
        janelab.after(100, falar, "Seria a Bed? O Clothes-press? O Cooker? ou O Board?")

        repetiir = tk.Button(text="Repetir", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=repetir)

        lugares.grid(row=0, column=0, columnspan=4,
                     padx=(200, 0), pady=(470, 0))
        escolha1.grid(row=1, column=1, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha2.grid(row=1, column=2, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha3.grid(row=1, column=3, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha4.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)


        acertos = tk.Text(background="white", foreground="black",
                          wrap=tk.WORD, font=("ADVERTURE", 15), width=40, height=4)
        acertos.insert(
            '1.0', f"Isso mesmo {aluno}, ambientes como a Kitchen necessitam de um Cooker para permitir que façamos nossas comidas neles!")
        
        janelab.after(100, falar, "Isso mesmo, " + aluno + ", ambientes como a Kitchen necessitam de um Cooker para permitir que façamos nossas comidas neles!")
        janelab.after(100, falar, "Me diga qual outro objeto é muito importante para uma cozinha?")
        janelab.after(100, falar, "Um Shower? Uma Bed? Um Sofa? ou um Refrigerator?")
    

    def certo1():
        acertos.grid(row=0, column=0, padx=(100, 0), pady=(20, 0), columnspan=17)
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        parte3()

   

    def parte3():
        global escolha1, escolha2, escolha3, escolha4, lugares, repetiir,acertos
        escolha1 = tk.Button(text="Meat and Vegetables", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=certo2)
        escolha2 = tk.Button(text="Wood", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado1)
        escolha3 = tk.Button(text="Books", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado1)
        escolha4 = tk.Button(text="Clothes", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado1)
        lugares = tk.Text(background="white", foreground="black",
                          wrap=tk.WORD, font=("ADVERTURE", 15), width=40, height=2)
    
        lugares.insert(
            '1.0', f"Agora me diga, o que pode ser cozido na Kitchen dentro do Cooker?")
        repetiir = tk.Button(text="Repetir", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=repetir)


        lugares.grid(row=0, column=0, columnspan=4,
                     padx=(200, 0), pady=(470, 0))
        escolha1.grid(row=1, column=1, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha2.grid(row=1, column=2, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha3.grid(row=1, column=3, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha4.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)

        acertos.delete("1.0","end")
        acertos.insert(
            '1.0', f"Isso mesmo {aluno}, você conseguiu entender qual a função desse objeto. Mas ainda tem outros que eu gostaria de te mostrar!!")
        
        janelab.after(100, falar, "Isso mesmo, " + aluno + ", você conseguiu entender qual a função desse objeto. Mas ainda tem outros que eu gostaria de te mostrar!!")
        janelab.after(100, falar, "Agora me diga, o que pode ser cozido na Kitchen dentro do Cooker?")
        janelab.after(100, falar, "Seria Meat and Vegetables? Wood? Books? ou Clothes?")
       
    def certo2():
        acertos.grid(row=0, column=0, padx=(100, 0), pady=(20, 0), columnspan=17)
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        parte4()

    def parte4():
        global escolha1, escolha2, escolha3, escolha4, lugares, repetiir
        escolha1 = tk.Button(text="Shower", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado2)
        escolha2 = tk.Button(text="Bed", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado2)
        escolha3 = tk.Button(text="Sofa", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado2)
        escolha4 = tk.Button(text="Refrigerator", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=certo3)
        lugares = tk.Text(background="white", foreground="black",
                          wrap=tk.WORD, font=("ADVERTURE", 15), width=40, height=2)
        lugares.insert(
            '1.0', f"Me diga qual outro objeto é muito importante para uma cozinha?")
        repetiir = tk.Button(text="Repetir", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=repetir)

        lugares.grid(row=0, column=0, columnspan=4,
                     padx=(200, 0), pady=(470, 0))
        escolha1.grid(row=1, column=1, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha2.grid(row=1, column=2, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha3.grid(row=1, column=3, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha4.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)
        acertos.delete("1.0","end")
        acertos.insert(
            '1.0', f"Isso mesmo {aluno}, ambientes como a Kitchen necessitam de um Cooker para permitir que façamos nossas comidas neles!")
    def certo3():
        acertos.grid(row=0, column=0, padx=(100, 0), pady=(20, 0), columnspan=17)
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        parte5()

    def parte5():
        global escolha1, escolha2, escolha3, escolha4, lugares, repetiir,acertos
        escolha1 = tk.Button(text="Redaction", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado3)
        # escolha2 = tk.Button(text="Bed", highlightthickness=0,
        #                      foreground="black", font=("ADVERTURE", 15), command=errado)
        escolha3 = tk.Button(text="Cookbook", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=certo4)
        escolha4 = tk.Button(text="Comics Books", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado3)
        lugares = tk.Text(background="white", foreground="black",
                          wrap=tk.WORD, font=("ADVERTURE", 15), width=40, height=2)
        lugares.insert(
            '1.0', f"{aluno}, você sabia que até para fazer comida nós devemos estudar?! Estudar é muito importante nas nossas vidas. O que deve ser estudado para isso?")
        repetiir = tk.Button(text="Repetir", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=repetir)

        lugares.grid(row=0, column=0, columnspan=4,
                     padx=(200, 0), pady=(470, 0))
        escolha1.grid(row=1, column=1, padx=(1, 0), pady=(20, 0), columnspan=1)
        # escolha2.grid(row=1, column=2, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha3.grid(row=1, column=3, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha4.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)
        acertos.configure(width=40,height=5)
        acertos.delete("1.0","end")
        acertos.insert(
            '1.0', f"Isso mesmo {aluno}, é fundamental a existência de um Refrigerator dentro da Kitchen, pois ele mantém os alimentos preservados em baixas temperaturas, o que permite que eles demorem pra estragar! Legal né?!")
        
        janelab.after(100, falar, "Isso mesmo, " + aluno + ", é fundamental a existência de um Refrigerator dentro da Kitchen, pois ele mantém os alimentos preservados em baixas temperaturas, o que permite que eles demorem pra estragar! Legal né?!")
        janelab.after(100, falar, aluno + "você sabia que até para fazer comida nós devemos estudar?! Estudar é muito importante nas nossas vidas. O que deve ser estudado para isso?")
        janelab.after(100, falar, "Uma Redaction? Um Coockbook? ou Comics Books?")


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
        '1.0', f"Bom dia {aluno}, muito obrigada por me acompanhar em minha rotina de cozinheira.\nEstamos aqui para aprendermos juntos e nos divertirmos, vamos começar?")
    historia.grid(row=0, column=1, pady=(415, 0), padx=(60, 0))

    janelab.after(100, falar, "Bom dia, " + aluno + ", muito obrigada por me acompanhar em minha rotina de cozinheira. Estamos aqui para aprendermos juntos e nos divertirmos, vamos começar?")

    avancar_b = tk.Button(text="-->", highlightthickness=0,
                          foreground="black", font=("ADVERTURE", 15), command=avancar1, image=imagem)
    avancar_b.grid(row=1, column=2, padx=(255, 0), pady=(200, 0))


##################################################################################################################################################################################################
    def errado():
        acertos.grid_forget()
        avancar_b.grid_forget()
        lugares.delete("1.0", "end")
        lugares.insert(
            "1.0", "Esse objeto não deve ficar na Kitchen, vamos tentar de novo?!")
        janelab.after(100, falar, "Esse objeto não deve ficar na Kitchen, vamos tentar de novo?!")
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        repetiir.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)

    def repetir():

        repetiir.grid_forget()
        avancar1()

    def errado1():
        acertos.grid_forget()
        avancar_b.grid_forget()
        lugares.delete("1.0", "end")
        lugares.insert(
            "1.0", "Isso não é possível ser cozido dentro do Cooker, vamos voltar para entender melhor o que é esse objeto!")
        
        janelab.after(100, falar, "Isso não é possível ser cozido dentro do Cooker, vamos voltar para entender melhor o que é esse objeto!")

        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        repetiir.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)
        repetiir.config(command=repetir1)

    def repetir1():
        lugares.grid_forget()
        repetiir.grid_forget()
        parte3()

    def errado2():
        acertos.grid_forget()
        avancar_b.grid_forget()
        lugares.delete("1.0", "end")
        lugares.insert(
            "1.0", "Esse objeto não deve ficar na Kitchen, vamos tentar de novo?!")
        
        janelab.after(100, falar, "Esse objeto não deve ficar na Kitchen, vamos tentar de novo?!")

        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        repetiir.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)
        repetiir.config(command=repetir2)

    def repetir2():
        lugares.grid_forget()
        repetiir.grid_forget()
        parte4()

    def errado3():
        acertos.grid_forget()
        avancar_b.grid_forget()
        lugares.delete("1.0", "end")
        lugares.insert(
            "1.0", f"Apesar de importante, esse tipo de texto não pode nos ajudar a cozinhar. É melhor voltarmos um pouco!")

        janelab.after(100, falar, "Apesar de importante, esse tipo de texto não pode nos ajudar a cozinhar. É melhor voltarmos um pouco!")

        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        repetiir.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)
        repetiir.config(command=repetir3)

    def repetir3():
        lugares.grid_forget()
        repetiir.grid_forget()
        parte5()

    janelab.mainloop()
