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
# import tela_barbie
from tkinter import PhotoImage
import login2
import pyttsx3

def janelah_park():
    janelab = tk.Tk()  # abre a janelab
    janelab.title("joguinho barbie")

    imagem1 = Image.open("Homem Aranha Vem Ajudar no Park.jpg")
    imagem = imagem1.resize((1280, 900))
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

# \

    def falar(texto):
        engine.say(texto)
        engine.runAndWait()

    def avancar0():
        historia.delete("1.0", "end")
        historia.insert(
            "1.0", f"Aqui Homem Aranha, estou no lugar que tem muitas árvores. Me ajude.")
        historia.configure(height=1)

        janelab.after(100, falar, "Aqui Homem Aranha, estou no lugar que tem muitas árvores. Me ajude.")
        
        avancar_b.grid_forget()

        historia.configure(height=2)

        avancar_b1.grid(row=1, column=2, padx=(240, 0), pady=(200, 0))

    def avancar1():
        avancar('Alleway', 'Park', 'Hospital', 'Parking Lot')
        avancar_b1.grid_forget()

    def avancar(esc1, esc2, esc3, esc4):
        global escolha1, escolha2, escolha3, escolha4, lugares, repetiir, acertos
        historia.grid_forget()
        avancar_b.grid_forget()
        escolha1 = tk.Button(text=esc1, highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado)
        escolha2 = tk.Button(text=esc2, highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=certo1)
        escolha3 = tk.Button(text=esc3, highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado)
        escolha4 = tk.Button(text=esc4, highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado)
        lugares = tk.Text(foreground="black",
                          wrap=tk.WORD, font=("ADVERTURE", 15), width=50, height=2)
        lugares.insert(
            '1.0', f"Não estou conseguindo achar, me ajude a encontrá-la {aluno}.")
        
        janelab.after(100, falar, "Não estou conseguindo achar, me ajude a encontrá-la, " + aluno)
        janelab.after(100, falar, "Ela esta no Alleyway? no Park? No Hospital? ou no Parking Lot?")

        repetiir = tk.Button(text="Repetir", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=repetir)

        lugares.grid(row=0, column=0, columnspan=4,
                     padx=(180, 0), pady=(240, 0))
        escolha1.grid(row=1, column=1, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha2.grid(row=1, column=2, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha3.grid(row=1, column=3, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha4.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)

        acertos = tk.Text(foreground="black",
                          wrap=tk.WORD, font=("ADVERTURE", 15), width=50, height=6)

    def certo1():
        acertos.grid(row=0, column=0, padx=(100, 0),
                     pady=(20, 0), columnspan=17)
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        parte3()

    def parte3():
        global escolha1, escolha2, escolha3, escolha4, lugares, repetiir, acertos
        escolha1 = tk.Button(text="Cat", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=certo2)
        escolha2 = tk.Button(text="Monkey", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado1)
        escolha3 = tk.Button(text="Bird", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado1)
        escolha4 = tk.Button(text="Spider", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado1)
        lugares = tk.Text(foreground="black",
                          wrap=tk.WORD, font=("ADVERTURE", 15), width=50, height=2)

        lugares.insert(
            '1.0', f"Qual é o animal que devemos resgatar {aluno}?")
        repetiir = tk.Button(text="Repetir", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=repetir)

        lugares.grid(row=0, column=0, columnspan=4,
                     padx=(180, 0), pady=(240, 0))
        escolha1.grid(row=1, column=1, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha2.grid(row=1, column=2, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha3.grid(row=1, column=3, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha4.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)

        acertos.delete("1.0", "end")
        acertos.insert(
            '1.0', f"Isso mesmo {aluno}!!\n\nObrigada por me encontrar, eu preciso muito da ajuda de vocês. Meu gatinho amarelo subiu na árvore e está preso, mas eu não o vejo. Vocês poderiam me ajudar a resgatar ele?")

        janelab.after(100, falar, "Isso mesmo, " + aluno + "Obrigada por me encontrar, eu preciso muito da ajuda de vocês. Meu gatinho amarelo subiu na árvore e está preso, mas eu não o vejo. Vocês poderiam me ajudar a resgatar ele?")
        janelab.after(100, falar, "Qual é o animal que devemos resgatar, " + aluno + "?")
        janelab.after(100, falar, "Seria o Cat? O Monkey? O Bird? ou a Spider?")

    def certo2():
        acertos.grid(row=0, column=0, padx=(100, 0),
                     pady=(20, 0), columnspan=17)
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        parte4()

    def parte4():
        global escolha1, escolha2, escolha3, escolha4, lugares, repetiir
        escolha1 = tk.Button(text="Black", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado2)
        escolha2 = tk.Button(text="White", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado2)
        escolha3 = tk.Button(text="Gray", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado2)
        escolha4 = tk.Button(text="Yellow", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=certo3)
        lugares = tk.Text(foreground="black",
                          wrap=tk.WORD, font=("ADVERTURE", 15), width=50, height=2)
        lugares.insert(
            '1.0', f"Que cor o gato dela é mesmo?")
        repetiir = tk.Button(text="Repetir", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=repetir)

        lugares.grid(row=0, column=0, columnspan=4,
                     padx=(180, 0), pady=(240, 0))
        escolha1.grid(row=1, column=1, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha2.grid(row=1, column=2, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha3.grid(row=1, column=3, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha4.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)
        acertos.delete("1.0", "end")
        acertos.insert(
            '1.0', f"Isso mesmo {aluno} estamos quase conseguindo. Agora precisamos pegar o gatinho.")
        
        janelab.after(100, falar, "Isso mesmo, " + aluno + "estamos quase conseguindo. Agora precisamos pegar o gatinho.")
        janelab.after(100, falar, "Que cor o gato dela é mesmo?")
        janelab.after(100, falar, "Black? White? Gray? ou Yellow?")

        acertos.configure(height=3)

    def certo3():
        acertos.grid(row=0, column=0, padx=(100, 0),
                     pady=(20, 0), columnspan=17)
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        parte5()

    def parte5():
        global escolha1, escolha2, escolha3, escolha4, lugares, repetiir, acertos
        escolha1 = tk.Button(text="Candy Shop", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado3)
        escolha2 = tk.Button(text="Restaurant", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado3)
        escolha3 = tk.Button(text="Bakery", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=certo4)
        escolha4 = tk.Button(text="Coffee Shop", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado3)
        lugares = tk.Text(foreground="black",
                          wrap=tk.WORD, font=("ADVERTURE", 15), width=50, height=2)
        lugares.insert(
            '1.0', f"Vamos até a padaria, {aluno}? \nConsegue achar ela na rua?")
        repetiir = tk.Button(text="Repetir", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=repetir)

        lugares.grid(row=0, column=0, columnspan=4,
                     padx=(180, 0), pady=(240, 0))
        escolha1.grid(row=1, column=1, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha2.grid(row=1, column=2, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha3.grid(row=1, column=3, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha4.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)
        acertos.configure( height=5)
        acertos.delete("1.0", "end")
        acertos.insert(
            '1.0', f"Isso mesmo {aluno}, esse é o meu gatinho.  \n\nVocês são a salvação dessa nação!! Eu gostaria de recompensar vocês com um vale da padaria para simbolizar a minha gratidão!!")
        acertos.configure(height=6)

        janelab.after(100, falar, "Isso mesmo, " + aluno  + ", esse é o meu gatinho. Vocês são a salvação dessa nação!! Eu gostaria de recompensar vocês com um vale da padaria para simbolizar a minha gratidão!!")
        janelab.after(100, falar, "Vamos até a padaria, " + aluno + "? Consegue achar ela na rua?")
        janelab.after(100, falar, "A padaria é a Candy Shop, O Restaurant, A Bakery ou A Coffee Shop?")

    def certo4():
        lugares.delete("1.0", "end")
        lugares.insert(
            '1.0', f"Estou muito orgulhosa por ter me ajudado até aqui! Agora podemos continuar nossa aventura em outro lugar!")
        janelab.after(100, falar, "Estou muito orgulhosa por ter me ajudado até aqui! Agora podemos continuar nossa aventura em outro lugar!")
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
        avancar_b.grid(row=1, column=2, padx=(400, 0), pady=(557, 0))


    def retornar():
        janelab.destroy()
        login2.login()
        # tela_barbie.janelab()


##################################################################################################################################################################################################

    aluno = variaveis.nome

    historia = tk.Text(foreground="black", wrap=tk.WORD,
                       font=("ADVERTURE", 15), width=75, height=5)
    historia.insert(
        '1.0', f"Durante o primeiro passeio, Peter com a sua super audição escutou uma senhora idosa gritando por ajuda, mas ele não sabia onde ela estava. Então, subiu no topo de um prédio e avistou 4 possíveis lugares em que ela podia estar. Então a senhora gritou:")
    historia.grid(row=0, column=0, pady=(100, 0), padx=(60, 0))

    janelab.after(100, falar, "Durante o primeiro passeio, Peter com a sua super audição escutou uma senhora idosa gritando por ajuda, mas ele não sabia onde ela estava. Então, subiu no topo de um prédio e avistou 4 possíveis lugares em que ela podia estar. Então a senhora gritou:")

    imagem=PhotoImage(file="seta.png")
    avancar_b = tk.Button(text="-->", highlightthickness=0,
                          foreground="black", font=("ADVERTURE", 15), command=avancar0,image=imagem)
    avancar_b.grid(row=2, column=2, padx=(240, 0), pady=(200, 0))

    avancar_b1 = tk.Button(text="-->", highlightthickness=0,
                           foreground="black", font=("ADVERTURE", 15), command=avancar1,image=imagem)
    avancar_b1.grid(row=2, column=2, padx=(240, 0), pady=(200, 0))
    avancar_b1.grid_forget()

##################################################################################################################################################################################################

    def errado():
        acertos.grid_forget()
        avancar_b.grid_forget()
        lugares.delete("1.0", "end")
        lugares.insert(
            "1.0", "Ela não estava lá. Vamos procurar em outro lugar! Preste atenção na dica dela:\nLugar com muitas árvores.")
        
        janelab.after(100, falar, "Ela não estava lá. Vamos procurar em outro lugar! Preste atenção na dica dela, Lugar com muitas árvores.")

        lugares.configure(height=4)
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        repetiir.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)

    def repetir():
        lugares.grid_forget()
        repetiir.grid_forget()
        avancar1()

    def errado1():
        acertos.grid_forget()
        avancar_b.grid_forget()
        lugares.delete("1.0", "end")
        lugares.insert(
            "1.0", "Esse animal é nativo desse habitat, não precisando da nossa ajuda! Vamos começar de novo!.")
        
        janelab.after(100, falar, "Esse animal é nativo desse habitat, não precisando da nossa ajuda! Vamos começar de novo!.")

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
            "1.0", "Esse não é a cor do meu gatinho querido!!!")
        
        janelab.after(100, falar, "Esse não é a cor do meu gatinho querido!!!")

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
            "1.0", f"Essa não é a Padaria, é outro lugar.")  
        
        janelab.after(100, falar, "Essa não é a Padaria, é outro lugar.")
        
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

