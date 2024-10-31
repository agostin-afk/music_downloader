from pytubefix import YouTube, Playlist
from testespytube import *
import threading
import os
import datetime

class Audio:
    def __init__(self):
        self.playlist_url = Playlist(playlist_url)
        self.name_arqv = self.create_Arqv()
    def download_audio(self):
        for video_url in self.playlist_url:
            try:
                yt = YouTube(video_url)
                audio_stream = yt.streams.filter(only_audio=True).first()
                audio_file = audio_stream.download(mp3=True)  # type: ignore
                print(f'Áudio do vídeo {yt.title.encode("utf-8").decode("utf-8")} baixado e convertido para mp3 com sucesso.')
            except Exception as e:
                print(f'Erro ao baixar o áudio do vídeo {video_url}: {e}')
                add_Arquivo_erro(video_url, self.name_arqv)    

    def create_Arqv(self, name="list_erro_videos"):
        try:
            name = datetime.date.today()
        except Exception as e:
            print(f"Erro: {e}")
            pass
        name = str(name)+".txt"
        try:
            with open(name, 'x', encoding="UTF-8") as arqv:
                pass
        except FileExistsError:
            print("Arqv já existe, apagando e trocando os valores")
            os.remove(name)
            self.create_Arqv(name)
        except Exception as e:
            print(f"Erro: {e}")
            return None
        return name
    def add_Video_Erro_List(self, name_video, name_arqv):
        try:
            with open(name_arqv, 'a') as file:
                file.write(name_video+"\n")
        except:
            print("Erro")
    def add_Arquivo_erro(self,url, name_arqv):
        add_Video_Erro_List(f"{url}", name_arqv)
