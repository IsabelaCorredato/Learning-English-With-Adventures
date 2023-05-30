# biblioteca(as)
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
from urllib import request
from io import BytesIO
import win32api
from tkinter import font
import keyboard
#############################################################################################################################################################################################################

# codigo
root = tk.Tk()  # cria a janela principal do aplicativo.


url = "https://imgur.com/OR7DhRx.png"
with request.urlopen(url) as u:
    raw_data = u.read()
iimage = Image.open(BytesIO(raw_data))

url2 = "https://imgur.com/67wVsaU.png"
with request.urlopen(url) as u2:
    raw_data2 = u2.read()
iimage2 = Image.open(BytesIO(raw_data2))


root.resizable(False, False)
teste_image = ImageTk.PhotoImage(iimage)
# ele pega da pasta do codigo um arquivo chamado "imagem" e mostra ela....
bg_image = ImageTk.PhotoImage(iimage)


width = bg_image.width()  # pega largura da janela para a mesma largura da imagem
height = bg_image.height()  # pega altura da janela para a mesma largura da imagem
monitor_width = win32api.GetSystemMetrics(0)
monitor_height = win32api.GetSystemMetrics(1)
screen_width = root.winfo_screenwidth()  # obtem a largura da tela.
screen_height = root.winfo_screenheight()  # obtem a altura da tela.

# calcula a posição horizontal da janela para centralizá-la na tela.
x = (screen_width // 2) - (width // 2)
# calcula a posição vertical da janela para centralizá-la na tela.
y = (screen_height // 2) - (height // 2)
# define a posição da janela na tela.

root.geometry(f"{monitor_width-150}x{monitor_height-150}+{x+50}+{y+50}")

# define a geometria da janela principal para ter a mesma largura e altura da imagem carregada
# root.geometry("800x800")


# cria um rótulo para exibir a imagem carregada.
bg_label = tk.Label(root, image=bg_image, compound=tk.CENTER)

# posiciona o rótulo na janela para que ocupe todo o espaço disponível.
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


# cria um rótulo para exibir o texto "Nome:" com fundo cinza.
# name_label = tk.Label(root, text="Nome:",
#                       background="gray", width=70, height=6)
# # posiciona o rótulo "Nome:" na janela.
# name_label.pack(side="left", anchor="center", padx=64, pady=(55,0))

# cria uma caixa de entrada para o usuário digitar seu nome.
fonte_nome = font.Font(size=28)
cor_rgb = "#B8B8B8"
name_entry = tk.Entry(root, width=22, font=fonte_nome,
                      bg=cor_rgb, highlightthickness=0, borderwidth=0)

0
# posiciona a caixa de entrada na janela.
nome = name_entry.pack(side="left", anchor="center",
                       padx=77, pady=(55, 0), ipady=17)


# define a função show_name que será executada quando o botão for pressionado.
def show_name():
    # exibe o nome digitado pelo usuário no console.
    print(name_entry.get())


# cria um botão com o texto "ENTRAR" e define a função show_name como o comando que será executado quando o botão for pressionado. (Toda vez q apertar ele mostra no terminal o nome)
show_button = tk.Button(root, text="ENTRAR",
                        command=show_name, background="gray", bd=0)
# posiciona o botão na janela.
show_button.pack(side="bottom", anchor='w', after=(nome), pady=5)

# inicia o loop principal da interface gráfica, permitindo que o usuário interaja com a janela.


def escolher_barbie():
    print("escolheu barbie")


# Botão para escolha de personagens
show_bar = tk.Button(root, text="Barbie", command=escolher_barbie,
                     background="gray", font=("ADVERTURE", 20,), bd=0)

# posição
show_bar.pack(side="top", padx=5, after=show_button)


def escolher_homem():
    print("escolheu homem aranha")


# Botão para escolha de personagens
show_hom = tk.Button(root, text="Homem-aranha", command=escolher_homem,
                     background="gray", font=("ADVERTURE", 20,), bd=0)

# posição
show_hom.pack(side="top", pady=5, after=show_bar, anchor="e")

root.mainloop()
if keyboard.is_pressed ()"c":
 root.destroy