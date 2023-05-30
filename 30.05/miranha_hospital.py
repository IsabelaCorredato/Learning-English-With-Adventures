import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
from urllib import request
from io import BytesIO
import win32api
from tkinter import font
import subprocess
import login2
import math
from tkinter import ttk
import variaveis
# import tela_barbie
from tkinter import PhotoImage
import time
import pyttsx3


def janelah_hospital():
    janelab = tk.Tk()  # abre a janelab
    janelab.title("joguinho barbie")

    imagem1 = Image.open("Homem-Aranha no quarto de hospital.jpg")
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
            "1.0", f"Oi Homem-Aranha e {aluno}, eu caí brincando e quebrei o meu braço, e agora sinto muita dor!")
        
        janelab.after(100, falar, "Oi Homem-Aranha e, " +aluno + ", eu caí brincando e quebrei o meu braço, e agora sinto muita dor!")

        avancar_b.grid_forget()

        historia.configure(height=2)

        avancar_b1.grid(row=1, column=2, padx=(240, 0), pady=(200, 0))

    def avancar1():
        avancar('Arm', 'Leg', 'Hand', 'Foot')
        avancar_b1.grid_forget()

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
                          wrap=tk.WORD, font=("ADVERTURE", 15), width=50, height=2)
        lugares.insert(
            '1.0', f"Nossa, deve ter sido muito doloroso! {aluno}, você conseguiria me dizer que parte ele quebrou em inglês?")
        
        janelab.after(100, falar, "Nossa, deve ter sido muito doloroso!, " + aluno + ", você conseguiria me dizer que parte ele quebrou em inglês?")
        janelab.after(100, falar, "Ele quebrou o Arm? A Leg? A Hand? ou O Foot?")

        repetiir = tk.Button(text="Repetir", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=repetir)

        lugares.grid(row=0, column=0, columnspan=4,
                     padx=(200, 0), pady=(140, 0))
        escolha1.grid(row=1, column=1, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha2.grid(row=1, column=2, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha3.grid(row=1, column=3, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha4.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)

        acertos = tk.Text(foreground="black",
                          wrap=tk.WORD, font=("ADVERTURE", 15), width=50, height=6)

    def certo1():
        acertos.grid(row=0, column=0, padx=(136, 0),
                     pady=(20, 0), columnspan=17)
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        parte3()

    def parte3():
        global escolha1, escolha2, escolha3, escolha4, lugares, repetiir, acertos
        escolha1 = tk.Button(text="Teacher", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado1)
        escolha2 = tk.Button(text="Actor", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado1)
        escolha3 = tk.Button(text="Lawyer", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado1)
        escolha4 = tk.Button(text="Nurse", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=certo2)
        lugares = tk.Text(foreground="black",
                          wrap=tk.WORD, font=("ADVERTURE", 15), width=50, height=2)

        lugares.insert(
            '1.0', f"{aluno}, você sabe como é o nome das pessoas que trabalham no hospital com enfermagem?")
        
        repetiir = tk.Button(text="Repetir", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=repetir)

        lugares.grid(row=0, column=0, columnspan=4,
                     padx=(200, 0), pady=(140, 0))
        escolha1.grid(row=1, column=1, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha2.grid(row=1, column=2, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha3.grid(row=1, column=3, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha4.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)

        acertos.delete("1.0", "end")
        acertos.insert(
            '1.0', f"Isso mesmo {aluno}!!\n\n")
        acertos.configure(height=1)

        janelab.after(100, falar, "Isso mesmo, " + aluno + "!!")
        janelab.after(100, falar, aluno + ", você sabe como é o nome das pessoas que trabalham no hospital com enfermagem?")
        janelab.after(100, falar, "Um Teacher? Um Actor? Um Lawyer? ou uma Nurse?")


    def certo2():
        acertos.grid(row=0, column=0, padx=(136, 0),
                     pady=(20, 0), columnspan=17)
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        parte4()

    def parte4():
        global escolha1, escolha2, escolha3, escolha4, lugares, repetiir
        escolha1 = tk.Button(text="Cousin", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado2)
        escolha2 = tk.Button(text="Father", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado2)
        escolha3 = tk.Button(text="Aunt", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado2)
        escolha4 = tk.Button(text="Mother", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=certo3)
        lugares = tk.Text(foreground="black",
                          wrap=tk.WORD, font=("ADVERTURE", 15), width=50, height=2)
        lugares.insert(
            '1.0', f"Entre esses parentes, qual é o que devemos chamar?")
        repetiir = tk.Button(text="Repetir", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=repetir)

        lugares.grid(row=0, column=0, columnspan=4,
                     padx=(200, 0), pady=(140, 0))
        escolha1.grid(row=1, column=1, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha2.grid(row=1, column=2, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha3.grid(row=1, column=3, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha4.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)
        acertos.delete("1.0", "end")
        acertos.insert(
            '1.0', f"Mas mesmo assim me sinto muito sozinha aqui dentro, estou com saudades da minha mãe! Vocês poderiam me ajudar a encontrar ela?")
        acertos.configure(height=3)

        janelab.after(100, falar, "Mas mesmo assim me sinto muito sozinha aqui dentro, estou com saudades da minha mãe! Vocês poderiam me ajudar a encontrar ela?")
        janelab.after(100, falar, "Entre esses parentes, qual é o que devemos chamar?")
        janelab.after(100, falar, "Um Cousin? O Father? A Aunt? ou A Mother?")

    def certo3():
        acertos.grid(row=0, column=0, padx=(136, 0),
                     pady=(20, 0), columnspan=17)
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        parte5()

    def parte5():
        global escolha1, escolha2, escolha3, escolha4, lugares, repetiir, acertos
        escolha1 = tk.Button(text="Ball", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado3)
        escolha2 = tk.Button(text="Ballon", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado3)
        escolha3 = tk.Button(text="Teddy Bear", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=certo4)
        escolha4 = tk.Button(text="Car", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado3)
        lugares = tk.Text(foreground="black",
                          wrap=tk.WORD, font=("ADVERTURE", 15), width=50, height=2)
        lugares.insert(
            '1.0', f"{aluno}, você sabe qual é o nome do meu brinquedo favorito, que está no meu colo?")
        repetiir = tk.Button(text="Repetir", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=repetir)

        lugares.grid(row=0, column=0, columnspan=4,
                     padx=(200, 0), pady=(140, 0))
        escolha1.grid(row=1, column=1, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha2.grid(row=1, column=2, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha3.grid(row=1, column=3, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha4.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)
        acertos.configure(width=40, height=5)
        acertos.delete("1.0", "end")
        acertos.insert(
            '1.0', f"Obrigada por me ajudar a achar a minha mamãe. \n\n.")
        acertos.configure(height=1)

        janelab.after(100, falar, "Obrigada por me ajudar a achar a minha mamãe.")
        janelab.after(100, falar, aluno + ", você sabe qual é o nome do meu brinquedo favorito, que está no meu colo?")
        janelab.after(100, falar, "Uma ball? Um ballon? Um Teddy Bear? ou um Car?")

    def certo4():
        lugares.delete("1.0","end")
        lugares.insert('1.0', f"Obrigada por me trazer o meu melhor amigo! Agora me sinto menos sozinhos. Vocês são meus heróis!\nAgora podem ir ajudar outras pessoas que precisam de vocês!")

        janelab.after(100, falar, "Obrigado por me trazer o meu melhor amigo! Agora me sinto meno sozinho. Vocês são meus heróis! Agora podem ir ajudar outras pessoas que precisam de vocês!")

        acertos.delete("1.0", "end")
        lugares.configure(height=3,width=60)
        acertos.grid_forget()
        print("acabou!!!")  # faz essa frase aparecer
        acertos.configure(height=3,width=50)
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        avancar_b = tk.Button( highlightthickness=0,
                          foreground="black", font=("ADVERTURE", 15), command=retornar, image=imagem)
        avancar_b.grid(row=1, column=2, padx=(400, 0), pady=(557, 0))
        # time.sleep(5)
        #retornar()

    def retornar():
        
        janelab.destroy()
        login2.login()
        # tela_barbie.janelab()


##################################################################################################################################################################################################

    aluno = variaveis.nome

    historia = tk.Text(foreground="black", wrap=tk.WORD,
                       font=("ADVERTURE", 15), width=75, height=5)
    historia.insert(
        '1.0', f"Em um momento de silencioso na tarde nova iorquina, o Homem-Aranha pôde ouvir um choro baixinho vindo de uma janela de um dos prédios da cidade. Ao chegar nessa janela, percebeu que o choro era de um garotinho que estava internada em um hospital, prontamente decidiu que ele e o seu parceiro deveriam ajudar essa criança no que fosse possível.")
    janelab.after(100, falar, "Em um momento de silencioso na tarde nova iorquina, o Homem-Aranha pôde ouvir um choro baixinho vindo de uma janela de um dos prédios da cidade. Ao chegar nessa janela, percebeu que o choro era de um garotinho que estava internada em um hospital, prontamente decidiu que ele e o seu parceiro deveriam ajudar essa criança no que fosse possível.")
    historia.grid(row=0, column=1, pady=(140, 0), padx=(60, 0))
    imagem = PhotoImage(file="seta.png")
    avancar_b = tk.Button(text="-->", highlightthickness=0,
                          foreground="black", font=("ADVERTURE", 15), command=avancar0, image=imagem)
    avancar_b.grid(row=1, column=2, padx=(240, 0), pady=(200, 0))

    avancar_b1 = tk.Button(text="-->", highlightthickness=0,
                           foreground="black", font=("ADVERTURE", 15), command=avancar1, image=imagem)
    avancar_b1.grid(row=1, column=2, padx=(240, 0), pady=(200, 0))
    avancar_b1.grid_forget()

##################################################################################################################################################################################################

    def errado():
        acertos.grid_forget()
        avancar_b.grid_forget()
        lugares.delete("1.0", "end")
        lugares.insert("1.0", "Não foi essa a parte que eu machuquei não!")

        janelab.after(100, falar, "Não foi essa a parte que eu machuquei não!")

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
            "1.0", "Não, esse profissional não trabalha em hospitais! Deve prestar mais atenção ao local, vamos começar outra vez.")
        
        janelab.after(100, falar, "Não, esse profissional não trabalha em hospitais! Deve prestar mais atenção ao local, vamos começar outra vez.")

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
            "1.0", "Não é esse parente que ele está querendo chamar.")
        
        janelab.after(100, falar, "Não é esse parente que ele está querendo chamar.")

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
            "1.0", f"Você errou {aluno}, esse não é o meu melhor amigo! :(")
        
        janelab.after(100, falar, "Você errou " + aluno + ", esse não é o meu melhor amigo!")

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



