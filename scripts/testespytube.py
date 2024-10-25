from pytube import Playlist, YouTube
import os
import datetime


def create_Arqv(name="list_erro_videos"):
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
        create_Arqv(name)
    except Exception as e:
        print(f"Erro: {e}")
        return None
    return name

def add_Video_Erro_List(name_video, name_arqv):
    try:
        with open(name_arqv, 'a') as file:
            file.write(name_video+"\n")
    except:
        print("Erro")

teste_playlist = Playlist("https://www.youtube.com/playlist?list=PLjpaTyNnuw2CVu4D1-OjK7KvocgRmDjDj")
def teste_Criar_arqv(url):
    name_arqv = create_Arqv()
    for _ in url:
        try:
            # print(_.watch_url)
            print(_)
        except KeyError:
            add_Video_Erro_List(f"{_}", name_arqv)
            print(f"Erro ao obter título do vídeo: {_}")
            

teste_Criar_arqv(teste_playlist)
# lembrar de criar um jeito de tentar baixar 3 vezes e depois criar um arquivo com o nome e/ou a url
# do video caso não dê certo
