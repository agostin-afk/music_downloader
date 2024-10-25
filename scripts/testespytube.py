from pytube import Playlist, YouTube
teste_playlist = Playlist("https://www.youtube.com/watch?v=Vi6bjV876fY&list=PLc0FtbJjhNUyOVaQ5r0sqd9YewHM9PSoL")
def teste_Criar_arqv(url):
    for _ in url.videos:
        try:
            # print(_.watch_url)
            print(_.title)
        except KeyError:
            print(f"Erro ao obter título do vídeo: {_}")

teste_Criar_arqv(teste_playlist)
# lembrar de criar um jeito de tentar baixar 3 vezes e depois criar um arquivo com o nome e/ou a url
# do video caso não dê certo
