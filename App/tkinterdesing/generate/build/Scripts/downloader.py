from pytubefix import YouTube, Playlist
import threading
from pydub import AudioSegment
import os
import datetime

class Audio:
    def __init__(self):
        self.name_arqv = self.create_Arqv()
    def download_audio(self, video_url):
            try:
                yt = YouTube(video_url)
                audio_stream = yt.streams.filter(only_audio=True).first()
                audio_file = audio_stream.download(output_path="C:\\Users\\agost\\OneDrive\\Área de Trabalho\\Musicas")  # type: ignore
                # print(audio_file[:-4])#type: ignore
                self.convert_m4a_to_mp3(audio_file) # type: ignore
                return f'Áudio do vídeo {yt.title.encode("utf-8").decode("utf-8")} baixado e convertido para mp3 com sucesso.'
            except Exception as e:
                self.add_Arquivo_erro(video_url, self.name_arqv)    
                return f'Erro ao baixar o áudio do vídeo {video_url}: {e}'
    def convert_m4a_to_mp3(self, m4a_file: str):
        try: 
            AudioSegment.from_file(f"{m4a_file}", format="m4a").export(f"{m4a_file[:-4]}.mp3", format="mp3")
            os.remove(m4a_file)
        except:
            pass

    def create_Arqv(self):
        file_name = f"{datetime.date.today()}.txt"
        try:
            with open("C:\\Users\\agost\\OneDrive\\Área de Trabalho\\"+file_name, 'x', encoding="UTF-8") as arqv:
                pass
        except FileExistsError:
            os.remove("C:\\Users\\agost\\OneDrive\\Área de Trabalho\\"+file_name)
            return self.create_Arqv()  
        except Exception as e:
            return f"Erro ao criar o arquivo: {e}"
        return "create: " + file_name
    def add_Video_Erro_List(self, name_video, name_arqv):
        try:
            with open(name_arqv, 'a') as file:
                file.write(name_video+"\n")
                return f"Video{name_video} adicionado na lista de erros"
        except:
            return "Erro"
    def add_Arquivo_erro(self, url, name_arqv):
        self.add_Video_Erro_List(url, name_arqv)