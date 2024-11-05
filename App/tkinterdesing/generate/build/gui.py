from dotenv import load_dotenv
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import os
from Scripts.downloader import Audio
import time

from pytubefix import Playlist

# Diretório base e carregamento de variáveis de ambiente
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent
load_dotenv(BASE_DIR / 'dotenv_files' / '.env', override=True)
OUTPUT_PATH = os.getenv('DIR_FILE')
ASSETS_PATH = str(OUTPUT_PATH) + "\\assets\\frame0"

# Função auxiliar para obter o caminho dos assets
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Função de download que exibe o título da playlist e mensagens de progresso
def download():
    p = Audio()
    playlist_url = entry_1.get()
    playlist = Playlist(playlist_url)
    
    # # Atualiza o título da playlist
    title_box = playlist.title.encode("utf-8").decode("utf-8")
    canvas.itemconfig(text_id, text=title_box)

    # Exibe mensagem de progresso no Text widget
    for _ in playlist:
        text_widget.config(state="normal")
        text_widget.insert("end",f"{p.download_audio(_)}\n")
        text_widget.config(state="disabled")

# Configurações principais da janela e Canvas
window = Tk()
window.geometry("670x450")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=450,
    width=670,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Desenho dos elementos de interface
canvas.create_rectangle(0.0, 0.0, 670.0, 450.0, fill="#D9D9D9", outline="")  # Background direita
canvas.create_rectangle(0.0, 0.0, 261.0, 450.0, fill="#717171", outline="")  # Background esquerda

# Ícone do YouTube
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
canvas.create_image(130.0, 117.0, image=image_image_1)

# Texto abaixo do ícone do YouTube
canvas.create_text(127.0, 230.0, text="Downloader", fill="#000000", font=("Inter", 21 * -1))

# Caixa de entrada de URL
entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
canvas.create_image(130.5, 320.5, image=entry_image_1)
entry_1 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_1.place(x=26.5, y=305.0, width=208.0, height=35.0)

# Título da playlist
canvas.create_text(292.0, 27.0, anchor="nw", text="Playlist title:", fill="#000000", font=("Inter", 21 * -1))
text_id = canvas.create_text(410.0, 27.0, anchor="nw", text="", fill="#000000", font=("Inter", 21 * -1))

# Área para vídeos baixados
canvas.create_rectangle(292.0, 113.0, 632.0, 338.0, fill="#9F9F9F", outline="")
canvas.create_text(292.0, 89.0, anchor="nw", text="Videos baixados:", fill="#000000", font=("Inter", 21 * -1))

# Criação do Text widget para exibir mensagens de progresso
text_widget = Text(
    window,
    width=47,
    height=13.4,
    bg="#9F9F9F",
    fg="#000000",
    font=("Inter", 10),
    wrap="word",
    bd=0,
    highlightthickness=0
)
text_widget.insert("end", "Mensagens do terminal:\n")
text_widget.config(state="disabled")  # Desabilita a edição inicial

# Adiciona o Text widget ao Canvas
canvas.create_window(300, 120, anchor="nw", window=text_widget)

# Botão de download
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=download,
    relief="flat"
)
button_1.place(x=75.0, y=359.0, width=111.0, height=40.0)

# Texto informativo sobre erros de download
canvas.create_text(
    302.0,
    347.0,
    anchor="nw",
    text="""Videos com erros no download vão ser salvos em
um .txt na área de trabalho""",
    fill="#000000",
    font=("Inter", 14 * -1)
)


# Configuração final da janela
window.resizable(False, False)
window.mainloop()
