# from pytube import Playlist, YouTube
from pytubefix import YouTube, Playlist
import threading
import os

p = Playlist("https://www.youtube.com/playlist?list=PLc0FtbJjhNUyOVaQ5r0sqd9YewHM9PSoL")

print(f'A playlist escolhida foi: {p.title.encode("utf-8").decode("utf-8")}')

videos_erros = []

def download_audio(video_url):
    try:
        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_file = audio_stream.download(mp3=True)  # type: ignore
        print(f'Áudio do vídeo {yt.title.encode("utf-8").decode("utf-8")} baixado e convertido para mp3 com sucesso.')
    except Exception as e:
        videos_erros.append(video_url)
        print(f'Erro ao baixar o áudio do vídeo {video_url}: {e}')

threads = []

for i in p.video_urls:
    t = threading.Thread(target=download_audio, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

if videos_erros:
    print(f'Os seguintes vídeos tiveram erros durante o download: {videos_erros}')
else:
    print('Todos os vídeos foram baixados com sucesso.')

for _ in videos_erros:
    download_audio(_)
