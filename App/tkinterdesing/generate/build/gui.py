from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import os
import threading
from Scripts.downloader import Audio
from pytubefix import Playlist


def relative_to_assets(file: str) -> str:
    "Para não usar .env || so as not to use .env"
    base_path = os.path.join(os.path.dirname(__file__), "assets", "frame0")
    return os.path.join(base_path, file)


def update_ui_callback(result: str) -> None:
    """
    Vai ser chamada sempre que for necessario imprimir algo na interface || It will be called whenever you need to print something in the interface
    .see() trava o scroller para o final
    """
    text_widget.config(state="normal")
    text_widget.insert("end", f"{result}\n")
    text_widget.see("end")
    text_widget.update()
    text_widget.config(state="disabled")
    return None


def download() -> None:
    """
        Função principal responsável por iniciar o processo de download de áudios de uma playlist do YouTube:
        1. Capturar a URL da playlist inserida pelo usuário.
        2. Obter informações sobre a playlist, como o título.
        3. Processar os vídeos da playlist e fazer o download dos áudios.
        4. Atualizar a interface gráfica com o progresso e os resultados.
        ||
        Main function responsible for starting the process of downloading audios from a YouTube playlist:
        1. Capturing the URL of the playlist entered by the user.
        2. Obtain information about the playlist, such as the title.
        3. Process the videos in the playlist and download the audio.
        4. Update the graphical interface with the progress and results.

        """
    def background_task():
        """
        Função que realiza o processamento da playlist e os downloads em uma thread:
        - Inicializa a classe `Audio` com o callback para atualizar a interface gráfica.
        - Obtém a URL da playlist a partir do campo de entrada da interface.
        - Carrega as informações da playlist (título e URLs dos vídeos).
        - Atualiza o título da playlist na interface.
        - Processa e realiza o download dos áudios dos vídeos da playlist.
        - Exibe mensagens de sucesso ou erro no `Text Widget` da interface.
        ||
        Function that processes the playlist and downloads in one thread:
        - Initializes the `Audio` class with the callback to update the graphical interface.
        - Gets the playlist URL from the interface input field.
        - Loads the playlist information (title and video URLs).
        - Updates the playlist title in the interface.
        - Processes and downloads the audios of the videos in the playlist.
        - Displays success or error messages in the interface's Text Widget.
        """
        p = Audio(update_ui_callback) 
        playlist_url = entry_1.get()
        playlist = Playlist(playlist_url)

        title_box = str(playlist.title)
        canvas.itemconfig(text_id, text=title_box)

        video_urls = playlist.video_urls 
        results = p.process_playlist(playlist_url)

        text_widget.config(state="normal")
        for result in results:
            text_widget.insert("end", f"{result}\n")
            text_widget.see("end")
            text_widget.update()
        text_widget.config(state="disabled")

    download_thread = threading.Thread(target=background_task)
    download_thread.start()
    return None

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


canvas.create_rectangle(0.0, 0.0, 670.0, 450.0, fill="#D9D9D9", outline="")  
canvas.create_rectangle(0.0, 0.0, 261.0, 450.0, fill="#717171", outline="") 

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

# Text widget para exibir mensagens de progresso
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
text_widget.config(state="disabled")

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
window.resizable(False, False) #Recomendação: não habilitar o resizable
window.mainloop()
