from dotenv import load_dotenv
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import os
from Scripts.testespytube import *
import time
# from scripts.testespytube import get_nome_plalist
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent
load_dotenv(BASE_DIR / 'dotenv_files' / '.env', override=True)
OUTPUT_PATH = os.getenv('DIR_FILE')
ASSETS_PATH = str(OUTPUT_PATH) + "\\assets\\frame0"

from pytube import Playlist, YouTube
def update_terminal_output(new_message):
    current_text = canvas.itemcget(terminal_text_id, "text") 
    messages = current_text.split("\n")                      
    messages.append(new_message)                            
    max_lines = 10
    if len(messages) > max_lines:
        messages.pop(0) 


    updated_text = "\n".join(messages)
    canvas.itemconfig(terminal_text_id, text=updated_text)
def get_nome_plalist():
    nome_playlist_get = entry_1.get()  # Pega o texto da Entry
    p = Playlist(f"{nome_playlist_get}")
    print(f"Nome digitado: {nome_playlist_get}")
    nome_playlist = p.title.encode("utf-8").decode("utf-8")
    canvas.itemconfig(text_id, text=nome_playlist)
    
    teste_Criar_arqv(nome_playlist_get)
    for i in range(20):
        update_terminal_output(f"Título da playlist: {nome_playlist}")
        print(f"{p.title.encode('utf-8').decode('utf-8')}")
    return f"{p.title.encode('utf-8').decode('utf-8')}"
# print(BASE_DIR)
# print(f"OUTPUT_PATH: {OUTPUT_PATH}")
# print(f"ASSETS_PATH: {ASSETS_PATH}\n")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("670x450")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 450,
    width = 670,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
"""background direita"""
canvas.create_rectangle(
    0.0,
    0.0,
    670.0,
    450.0,
    fill="#D9D9D9",
    outline="")

"""background esquerda"""
canvas.create_rectangle(
    0.0,
    0.0,
    261.0,
    450.0,
    fill="#717171",
    outline="")

"""Youtube icon"""
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    130.0,
    117.0,
    image=image_image_1
)

"""text abaixo do youtube icon"""
canvas.create_text(
    127.0,
    230.0,
    text="Downloader",
    fill="#000000",
    font=("Inter", 21 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    130.5,
    320.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=26.5,
    y=305.0,
    width=208.0,
    height=35.0
)


canvas.create_text(
    292.0,
    27.0,
    anchor="nw",
    text="Playlist title:",
    fill="#000000",
    font=("Inter", 21 * -1)
)
"""Caixa de texto - playlist title"""
text_id = canvas.create_text(
    410.0,
    27.0,
    anchor="nw",
    text="",
    fill="#000000",
    font=("Inter", 21 * -1)
)
""""""
"""Caixa de texto - videos baixados"""
canvas.create_rectangle(
    292.0,
    113.0,
    632.0,
    338.0,
    fill="#9F9F9F",
    outline=""
)

# Cria o texto inicial dentro do retângulo e salva o ID do texto em `terminal_text_id`
terminal_text_id = canvas.create_text(
    300.0,     # Posição X
    120.0,     # Posição Y
    anchor="nw",
    text="Mensagens do terminal:\n",
    fill="#000000",
    font=("Inter", 10),
    width=320   # Limita a largura do texto para caber no retângulo
)

canvas.create_text(
    292.0,
    89.0,
    anchor="nw",
    text="Videos baixados:",
    fill="#000000",
    font=("Inter", 21 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=get_nome_plalist,
    relief="flat"
)
button_1.place(
    x=75.0,
    y=359.0,
    width=111.0,
    height=40.0,
    
)

canvas.create_text(
    302.0,
    347.0,
    anchor="nw",
    text="""Videos com erros no download vão ser salvos em
um .txt na área de trabalho""",
    fill="#000000",
    font=("Inter", 14 * -1)
)
window.resizable(False, False)
window.mainloop()
