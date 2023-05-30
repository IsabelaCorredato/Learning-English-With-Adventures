import tkinter as tk
from tkinter import PhotoImage
from tkinter import font
from PIL import Image, ImageTk
from io import BytesIO
import win32api
from tkinter import ttk
import variaveis
import login2
import pyttsx3

def janelah_beco():
    janelab = tk.Tk()  # abre a janelab
    janelab.title("joguinho barbie")

    imagem1 = Image.open("Beco - Começo.jpg")
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
        avancar('Black and White T-Shirt',
                'Purple Jacket', 'Blue Jeans', 'Black Cap')
        # avancar_b1.grid_forget()

    def avancar(esc1, esc2, esc3, esc4):
        global escolha1, escolha2, escolha3, escolha4, lugares, repetiir, acertos, lugares1
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
            '1.0', f"{aluno}, você consegue me dizer como ele está vestido? Pois assim reconheceremos ele mais facilmente!")
        
        janelab.after(100, falar, aluno + ", você consegue me dizer como ele está vestido? Pois assim reconheceremos ele mais facilmente!")
        janelab.after(100, falar, "Sera que ele esta usando Black and white t-shirt?, purple jacket?, blue jeans? ou black cap?")

        repetiir = tk.Button(text="Repetir", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=repetir)

        lugares.grid(row=0, column=0, columnspan=4,
                     padx=(200, 0), pady=(240, 0))
        escolha1.grid(row=1, column=1, padx=(1, 0), pady=(10, 0), columnspan=1)
        escolha2.grid(row=1, column=2, padx=(1, 0), pady=(10, 0), columnspan=1)
        escolha3.grid(row=1, column=3, padx=(1, 0), pady=(10, 0), columnspan=1)
        escolha4.grid(row=1, column=4, padx=(1, 0), pady=(10, 0), columnspan=1)

        acertos = tk.Text(foreground="black",
                          wrap=tk.WORD, font=("ADVERTURE", 15), width=50, height=6)

    def certo1():
        acertos.grid(row=0, column=0, padx=(120, 0),
                     pady=(20, 0), columnspan=17)
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        parte3()

    def parte3():
        global escolha1, escolha2, escolha3, escolha4, lugares, repetiir, acertos
        escolha1 = tk.Button(text="Car", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado1)
        escolha2 = tk.Button(text="Bicycle", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=certo2)
        escolha3 = tk.Button(text="Bus", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado1)
        escolha4 = tk.Button(text="Motorcycle", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado1)
        lugares = tk.Text(foreground="black",
                          wrap=tk.WORD, font=("ADVERTURE", 15), width=50, height=2)

        lugares.insert(
            '1.0', f"No nosso caminho tem 4 objetos para nos locomover. {aluno}, Qual é o que devemos recuperar?")

        repetiir = tk.Button(text="Repetir", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=repetir)
        lugares.grid(row=0, column=0, columnspan=4,
                     padx=(200, 0), pady=(240, 0))
        escolha1.grid(row=1, column=1, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha2.grid(row=1, column=2, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha3.grid(row=1, column=3, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha4.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)

        acertos.delete("1.0", "end")
        acertos.insert(
            '1.0', f"Era assim mesmo que ele estava vestido!\nEstamos mais próximos graças a você! Agora, Garoto, o que ele roubou de você?\nEle passou e pegou minha bicicleta, subiu muito rápido e levou embora!")
        acertos.configure(height=4)
        janelab.after(100, falar, "Era assim mesmo que ele estava vestido!, Estamos mais próximos graças a você! Agora, Garoto, o que ele roubou de você?, Ele passou e pegou minha bicicleta, subiu muito rápido e levou embora!")
        janelab.after(100, falar, "No nosso caminho tem 4 objetos para nos locomover." + aluno + ", Qual é o que devemos recuperar?")
        janelab.after(100, falar, "Seria um car? uma bycicle? um bus? ou uma motorcycle?")

    def certo2():
        trocar_imagem_fundo()
        acertos.grid(row=0, column=0, padx=(120, 0),
                     pady=(20, 0), columnspan=17)
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        parte4()

    def parte4():
        global escolha1, escolha2, escolha3, escolha4, lugares, repetiir, acertos,label_fundo
        
        
        
        escolha1 = tk.Button(text="Basketball", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=certo3)
        escolha2 = tk.Button(text="Soccer", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado2)
        escolha3 = tk.Button(text="Hockey", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado2)
        escolha4 = tk.Button(text="Volleyball", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado2)
        lugares = tk.Text(foreground="black",
                          wrap=tk.WORD, font=("ADVERTURE", 15), width=50, height=2)
        lugares.insert(
            '1.0', f"Em qual esporte você acha que ele está?")

        repetiir = tk.Button(text="Repetir", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=repetir)

        lugares.grid(row=0, column=0, columnspan=4,
                     padx=(200, 0), pady=(240, 0))
        escolha1.grid(row=1, column=1, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha2.grid(row=1, column=2, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha3.grid(row=1, column=3, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha4.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)
        acertos.delete("1.0", "end")
        acertos.insert(
            '1.0', f"Isso mesmo {aluno}\nÉ essa mesma! Vamos pegá-la!\nNo meio da corrida para conseguir recuperar a bicicleta, o homem que a pegou entrou em uma quadra poliesportiva. Quando todo mundo entrou na quadra, percebeu que dentre todos os esportes, somente os jogadores de basquete usavam camisetas branca e preta listrada. Então, o ladrão provavelmente teria se escondido junto com eles.")
        
        janelab.after(100, falar, "Isso mesmo, " + aluno + ", Vamos pegá-la!. No meio da corrida para conseguir recuperar a bicicleta, o homem que a pegou entrou em uma quadra poliesportiva. Quando todo mundo entrou na quadra, percebeu que dentre todos os esportes, somente os jogadores de basquete usavam camisetas branca e preta listrada. Então, o ladrão provavelmente teria se escondido junto com eles.")
        janelab.after(100, falar, "Em qual esporte você acha que ele está?")
        janelab.after(100, falar, "Seria no Basketball, no Soccer, No Hockey, ou no Volleyball?")

        acertos.configure(height=6,width=50)

        
    def trocar_imagem_fundo():
        imagem_nova = Image.open("Beco - Meio.jpg")  # Substitua "nova_imagem.jpg" pelo caminho da nova imagem
        imagem_redimensionada = imagem_nova.resize((1280, 900))
        nova_imagem_fundo = ImageTk.PhotoImage(imagem_redimensionada)
        label_fundo.configure(image=nova_imagem_fundo)
        label_fundo.image = nova_imagem_fundo
    def certo3():
        
        acertos.grid(row=0, column=0, padx=(120, 0),
                     pady=(20, 0), columnspan=17)
        escolha1.grid_forget()
        escolha2.grid_forget()
        escolha3.grid_forget()
        escolha4.grid_forget()
        parte5()

    def parte5():

        global escolha1, escolha2, escolha3, escolha4, lugares, repetiir, acertos
        escolha1 = tk.Button(text="Wednesday", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado3)
        escolha2 = tk.Button(text="Sunday", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado3)
        escolha3 = tk.Button(text="Tuesday and Friday", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=certo4)
        escolha4 = tk.Button(text="Monday", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=errado3)
        lugares = tk.Text(foreground="black",
                          wrap=tk.WORD, font=("ADVERTURE", 15), width=50, height=2)
        lugares.insert(
            '1.0', f"Você sabe me dizer quais dias eles têm treino na verdade?")

        repetiir = tk.Button(text="Repetir", highlightthickness=0,
                             foreground="black", font=("ADVERTURE", 15), command=repetir)

        lugares.grid(row=0, column=0, columnspan=4,
                     padx=(200, 0), pady=(240, 0))
        escolha1.grid(row=1, column=1, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha2.grid(row=1, column=2, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha3.grid(row=1, column=3, padx=(1, 0), pady=(20, 0), columnspan=1)
        escolha4.grid(row=1, column=4, padx=(1, 0), pady=(20, 0), columnspan=1)
        acertos.configure(width=40, height=5)
        acertos.delete("1.0", "end")
        acertos.insert(
            '1.0', f"Isso mesmo {aluno} \nÉ lá mesmo que devemos procurar. Vamos!!!\nDurante a busca pelo grupo, o Homem-Aranha perguntou qual era o dia da semana em que treinavam. Todos responderam terça-feira e sexta-feira, exceto um homem que disse treinar aos sábados, levantando suspeitas sobre ele ser o impostor")
        
        janelab.after(100, falar, "Isso mesmo, " + aluno + ", É lá mesmo que devemos procurar. Vamos!!!, Durante a busca pelo grupo, o Homem-Aranha perguntou qual era o dia da semana em que treinavam. Todos responderam terça-feira e sexta-feira, exceto um homem que disse treinar aos sábados, levantando suspeitas sobre ele ser o impostor")

        janelab.after(100, falar, "Você sabe me dizer quais dias eles têm treino na verdade?")
        janelab.after(100, falar, "Seria Na Wednesday? No Sunday? Na Tuesday and Friday? ou Na Monday?")

        

        acertos.configure(height=6,width=50)

    def certo4():
        lugares.delete("1.0", "end")
        lugares.insert(
            '1.0', f"Muito obrigado Homem-aranha por recuperar minha bicicleta e garantir a segurança de toda a cidade!\nA vizinhança agradece!")

        janelab.after(100, falar, "Muito obrigado Homem-aranhapor recuperar minha bicicleta e garantir a segurança de toda a cidade!, A vizinhança agradece!")

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


##################################################################################################################################################################################################

    aluno = variaveis.nome
    imagem = PhotoImage(file="seta.png")
    historia = tk.Text(foreground="black", wrap=tk.WORD,
                       font=("ADVERTURE", 15), width=75, height=3)
    historia.insert(
        '1.0', f"Nesse momento, vocês encontram um garoto pedindo ajuda em um beco, pois ele havia acabado de ter sido roubado por um homem de blusa branca e preta.")
    historia.grid(row=0, column=1, pady=(140, 0), padx=(60, 0))

    janelab.after(100, falar, "Nesse momento, vocês encontram um garoto pedindo ajuda em um beco, pois ele havia acabado de ter sido roubado por um homem de blusa branca e preta.")

    avancar_b = tk.Button(text="-->", highlightthickness=0,
                          foreground="black", font=("ADVERTURE", 15), command=avancar1, image=imagem)
    avancar_b.grid(row=1, column=2, padx=(240, 0), pady=(200, 0))


##################################################################################################################################################################################################

    def errado():
        acertos.grid_forget()
        avancar_b.grid_forget()
        lugares.delete("1.0", "end")
        lugares.insert(
            "1.0", "Ele não estava vestido assim. Melhor eu explicar de novo.")
        janelab.after(100, falar, "Ele não estava vestido assim, Melhor eu explicar de novo.")
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
            "1.0", "Esse não é o meu meio de locomoção! Tenta outro!")
        
        janelab.after(100, falar, "Esse não é o meu meio de locomoção! Tenta outro!")

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
            "1.0", "Mas nesse esporte não tem ninguém usando verde! Acho que quem procuramos não está ai.")
        
        janelab.after(100, falar, "Mas nesse esporte não tem ninguém usando verde! Acho que quem procuramos não está ai.")

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
            "1.0", f"Você errou {aluno}. Não foi o que a maioria das pessoas afirmaram. Acho que você entendeu errado! ")

        janelab.after(100, falar, "você errou, " + aluno + "Não foi o que a maioria das pessoas afirmaram. Acho que você entendeu errado!")

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

