from pytubefix import YouTube, Playlist
from pydub import AudioSegment
import os
import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from platformdirs import user_desktop_dir
desktop_path = user_desktop_dir()
class Audio:
    def __init__(self, update_ui_callback):
        self.name_arqv = self.create_Arqv()
        self.update_ui_callback = update_ui_callback

    def download_audio(self, video_url):
        """Baixa o áudio do vídeo e converte para MP3."""
        try:
            yt = YouTube(video_url)
            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_file = audio_stream.download(output_path=desktop_path + "\\Musicas")  # type: ignore
            self.convert_m4a_to_mp3(audio_file)  # type: ignore
            result = f'Áudio do vídeo {yt.title} baixado e convertido para MP3 com sucesso.'
            self.update_ui_callback(result)
            return result
        except Exception as e:
            self.add_Arquivo_erro(video_url, self.name_arqv)
            error_msg = f'Erro ao baixar o áudio do vídeo {video_url}: {e}'
            self.update_ui_callback(error_msg)
            return error_msg

    def convert_m4a_to_mp3(self, m4a_file: str):
        """Converte arquivo .m4a para .mp3."""
        try:
            AudioSegment.from_file(m4a_file, format="m4a").export(f"{m4a_file[:-4]}.mp3", format="mp3")
            os.remove(m4a_file)
        except Exception as e:
            error_msg = f"Erro ao converter {m4a_file}: {e}"
            self.add_Arquivo_erro(f"Erro ao converter {m4a_file}: {e}", self.name_arqv)
            self.update_ui_callback(error_msg)

    def create_Arqv(self):
        """Cria um arquivo de log para registrar erros."""
        file_name = f"{datetime.date.today()}.txt"
        file_path = os.path.join(desktop_path+"\\", file_name)
        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding="UTF-8") as arqv:
                pass
        return file_path

    def add_Video_Erro_List(self, name_video, name_arqv):
        """Adiciona um vídeo à lista de erros."""
        try:
            with open(name_arqv, 'a') as file:
                file.write(name_video + "\n")
        except Exception as e:
            print(f"Erro ao registrar vídeo na lista de erros: {e}")

    def add_Arquivo_erro(self, message, name_arqv):
        """Adiciona uma mensagem de erro ao arquivo de log."""
        self.add_Video_Erro_List(message, name_arqv)

    def process_playlist(self, playlist_url):
        """Processa todos os vídeos de uma playlist em paralelo."""
        try:
            playlist = Playlist(playlist_url)
            video_urls = playlist.video_urls

            results = []
            with ThreadPoolExecutor(max_workers=4) as executor:
                future_to_url = {executor.submit(self.download_audio, url): url for url in video_urls}
                for future in as_completed(future_to_url):
                    url = future_to_url[future]
                    try:
                        result = future.result()
                        results.append(result)
                    except Exception as e:
                        error_msg = f"Erro ao processar {url}: {e}"
                        results.append(error_msg)

            return results
        except Exception as e:
            error_msg = f"Erro ao processar a playlist: {e}"
            print(error_msg)
            return [error_msg]
