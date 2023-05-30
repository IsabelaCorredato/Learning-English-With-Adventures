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
import pyttsx3

def janelah_estacao():
    global imagem1, label_fundo
    janelab = tk.Tk()  # abre a janelab
    janelab.title("joguinho barbie")

    imagem1 = Image.open("Estação InícioMeio.jpg")
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
        avancar_b.grid_forget()

        historia.configure(height=2)

        # avancar_b1.grid(row=0, column=2, padx=(240, 0), pady=(200, 0))

    def avancar1():
        avancar('Park', 'Train Station', 'Beach', 'Mall')
        # avancar_b1.grid_forget()

    def avancar(esc1, esc2, esc3, esc4):
        global escolha1, escolha2, escolha3, escolha4, lugares, repetiir, acertos, lugares1

        # nova_imagem = ImageTk.PhotoImage(Image.open("Beco - Meio.jpg"))
        # label_fundo.configure(image=nova_imagem)

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
                          wrap=tk.WORD, font=("ADVERTURE", 15), width=40, height=2)
        lugares.insert(
            '1.0', f"{aluno}, como é Estação de Trem, o lugar que precisam da nossa ajuda, em inglês?")
        
        janelab.after(100, falar, aluno + ", como é Estação de Trem, o lugar que precisam da nossa ajuda, em inglês?")
        janelab.after(100, falar, "é o Park? A Train Station? A Beach? Ou o Mall?")

        repetiir = tk.Button(text="Repetir", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=repetir)

        lugares.grid(row=0, column=0, columnspan=4,
                     padx=(200, 0), pady=(140, 0))
        escolha1.grid(row=1, column=1, padx=(1, 0), pady=(10, 0), columnspan=1)
        escolha2.grid(row=1, column=2, padx=(1, 0), pady=(10, 0), columnspan=1)
        escolha3.grid(row=1, column=3, padx=(1, 0), pady=(10, 0), columnspan=1)
        escolha4.grid(row=1, column=4, padx=(1, 0), pady=(10, 0), columnspan=1)

        acertos = tk.Text(foreground="black",
                          wrap=tk.WORD, font=("ADVERTURE", 15), width=50, height=6)

    def certo1():
        acertos.grid(row=0, column=0, padx=(125, 0),
                     pady=(0, 0), columnspan=17)
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        parte3()

    def parte3():

        global escolha1, escolha2, escolha3, escolha4, lugares, repetiir, acertos, lugares1
        escolha1 = tk.Button(text="Green", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado1)
        escolha2 = tk.Button(text="blue", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=certo2)
        escolha3 = tk.Button(text="White", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado1)
        escolha4 = tk.Button(text="Yellow", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado1)
        lugares = tk.Text(foreground="black",
                          wrap=tk.WORD, font=("ADVERTURE", 15), width=50, height=2)

        lugares.insert(
            '1.0', f"Rápido, qual a cor da roupa do homem que devemos deter?")
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
            '1.0', f"É lá mesmo que precisam de nós. Vamos!\nQuando chegam na estação, avistam bandidos vestidos de azul armados e fazendo passageiros de reféns. Peter sabia que não podia deixar isso acontecer e precisava da sua ajuda para pegá-los.")
        
        janelab.after(100, falar, "É lá mesmo que precisam de nós. Vamos! Quando chegam na estação, avistam bandidos vestidos de azul armados e fazendo passageiros de reféns. Peter sabia que não podia deixar isso acontecer e precisava da sua ajuda para pegá-los.")
        janelab.after(100, falar, "Rápido, qual a cor da roupa do homem que devemos deter?")
        janelab.after(100, falar, "Green?, Blue?, White?, Ou Yellow?")

        acertos.configure(height=5)

    def certo2():
        acertos.grid(row=0, column=0, padx=(125, 0),
                     pady=(0, 0), columnspan=17)
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        parte4()

    def parte4():
        global escolha1, escolha2, escolha3, escolha4, lugares, repetiir
        escolha1 = tk.Button(text="Dentist", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado2)
        escolha2 = tk.Button(text="Fireman", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado2)
        escolha3 = tk.Button(text="Doctor", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado2)
        escolha4 = tk.Button(text="Policeman", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=certo3)
        lugares = tk.Text(foreground="black",
                          wrap=tk.WORD, font=("ADVERTURE", 15), width=50, height=2)
        lugares.insert(
            '1.0', f"Não vamos conseguir pegá-lo, vamos precisar da ajuda de profissionais. Quem devemos chamar?")
        
        

        lugares.configure(height=2)
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
            '1.0', f"Isso mesmo {aluno}\nEsse é o bandido!")
        
        janelab.after(100, falar, "Isso mesmo, " + aluno + "Esse é o bandido!")
        janelab.after(100, falar, "Não vamos conseguir pegá-lo, vamos precisar da ajuda de profissionais. Quem devemos chamar?")
        janelab.after(100, falar, "O Dentist? O Fireman? O Doctor? ou o Policeman?")

        acertos.configure(height=2)

    def certo3():
        acertos.grid(row=0, column=0, padx=(125, 0),
                     pady=(0, 0), columnspan=17)
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        parte5()

    def parte5():

        global escolha1, escolha2, escolha3, escolha4, lugares, repetiir, acertos
        escolha1 = tk.Button(text="Milk", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado3)
        escolha2 = tk.Button(text="Soda", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado3)
        escolha3 = tk.Button(text="Coffee", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=certo4)
        escolha4 = tk.Button(text="Water", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado3)
        lugares = tk.Text(foreground="black",
                          wrap=tk.WORD, font=("ADVERTURE", 15), width=50, height=2)
        lugares.insert(
            '1.0', f"Gostou das aventuras, {aluno}? Espero que sim. Você poderia pedir para mim um café?")
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
            '1.0', f"Isso mesmo,{aluno}! São eles que vão nos ajudar a completar essa missão.")
        
        janelab.after(100, falar, "Isso mesmo, " + aluno + "! São eles que vão nos ajudar a completar essa missão.")
        janelab.after(100, falar, "Gostou das aventuras, " + aluno + "? Espero que sim. Você poderia pedir para mim um café?")
        janelab.after(100, falar, "Qual seria o café? O Milk? A Soda? O Coffee? ou a Water?")

        acertos.configure(height=3)

    def certo4():
        lugares.delete("1.0", "end")
        lugares.insert(
            '1.0', f"Isso mesmo {aluno}, Você será incrível como cozinheiro. Estou muito orgulhosa por ter me ajudado até aqui! Agora podemos continuar nossa aventura em outro lugar")
        
        janelab.after(100, falar, "Isso mesmo, " + aluno + ", Você será incrível como cozinheiro. Estou muito orgulhosa por ter me ajudado até aqui! Agora podemos continuar nossa aventura em outro lugar")

        acertos.delete("1.0", "end")
        lugares.configure(height=3, width=60)
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


##################################################################################################################################################################################################

    aluno = variaveis.nome

    historia = tk.Text(foreground="black", wrap=tk.WORD,
                       font=("ADVERTURE", 15), width=75, height=6)
    historia.insert(
        '1.0', f"Em um dia ensolarado, enquanto Peter Parker se balançava entre os prédios do centro da cidade, uma mensagem em seu celular chamou sua atenção. Era a polícia de Nova York pedindo ajuda para ele e seu ajudante {aluno}, pois um bandido havia roubado um saco de dinheiro na estação central de Manhattan. Sem hesitar, o Homem-Aranha precisa de sua ajuda para se dirigir imediatamente à estação.")
    historia.grid(row=0, column=1, pady=(140, 0), padx=(60, 0))

    janelab.after(100, falar, "Em um dia ensolarado, enquanto Peter Parker se balançava entre os prédios do centro da cidade, uma mensagem em seu celular chamou sua atenção. Era a polícia de Nova York pedindo ajuda para ele e seu ajudante," + aluno + ", pois um bandido havia roubado um saco de dinheiro na estação central de Manhattan. Sem hesitar, o Homem-Aranha precisa de sua ajuda para se dirigir imediatamente à estação.")

    imagem = PhotoImage(file="seta.png")
    avancar_b = tk.Button(text="-->", highlightthickness=0,
                          foreground="black", font=("ADVERTURE", 15), command=avancar1, image=imagem)
    avancar_b.grid(row=1, column=2, padx=(240, 0), pady=(200, 0))

    # avancar_b1 = tk.Button(text="-->", highlightthickness=0,
   #                        foreground="black", font=("ADVERTURE", 15), command=avancar1)
   # avancar_b1.grid(row=0, column=2, padx=(240, 0), pady=(200, 0))
    # avancar_b1.grid_forget()

##################################################################################################################################################################################################

    def errado():
        acertos.grid_forget()
        avancar_b.grid_forget()

        lugares.delete("1.0", "end")
        lugares.insert(
            "1.0", "Esse não é o lugar que devemos ir. Melhor tentar de novo.")
        
        janelab.after(100, falar, "Esse não é o lugar que devemos ir. Melhor tentar de novo.")

        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        repetiir.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)

    def repetir():
        lugares1.grid_forget()
        repetiir.grid_forget()
        avancar1()

    def errado1():
        acertos.grid_forget()
        avancar_b.grid_forget()
        lugares.delete("1.0", "end")
        lugares.insert(
            "1.0", "Nãoooo, as pessoas que estão com essa cor, são apenas pedestres!")
        
        janelab.after(100, falar, "Nãoooo, as pessoas que estão com essa cor, são apenas pedestres!")

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
            "1.0", "O trabalho dessa pessoa não pode nos ajudar a capturar ele. Vamos rápido, tente de novo")
        
        janelab.after(100, falar, "O trabalho dessa pessoa não pode nos ajudar a capturar ele. Vamos rápido, tente de novo")

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
            "1.0", f"Não era essa a bebida q eu tinha em mente. Pode pedir outra?")
        
        janelab.after(100, falar, "Não era essa a bebida q eu tinha em mente. Pode pedir outra?")

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

