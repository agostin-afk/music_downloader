# Playlist Downloader
![GitHub repo size](https://img.shields.io/github/repo-size/agostin-afk/music_downloader?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/agostin-afk/music_downloader?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/agostin-afk/music_downloader?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/agostin-afk/music_downloader?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/agostin-afk/music_downloader?style=for-the-badge)
>Surgiu da necessidade e da minha gigantesca Playlist


## 🚀 Funcionalidades
- 🎶 Baixar músicas do YouTube em formato MP3.
- 📃 Baixar playlists completas, independentemente do tamanho.
- 🕒 Atualização em tempo real sobre o progresso do download.
- ✅ Arquivos baixados são automaticamente convertidos e organizados na pasta "Músicas" na área de trabalho.

## ⚙️ Requisitos
Antes de começar, certifique-se de ter o [FFmpeg](https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/) instalado no seu sistema. Ele é essencial para conversões de áudio.
Rode esses comandos no terminal da raiz do projeto:
## 🛠️ Instalação
1. Configurar ambiente virtual
Execute os seguintes comandos na raiz do projeto:
```bash
python -m venv nome_ambienteVirtual
nome_ambienteVirtual/Scripts/Activate.ps1
pip install -r requirements.txt
```
2. Iniciar o projeto
Para rodar a interface gráfica, use:
```bash
cd App/tkinterdesing/generate/build && python gui.py
```

## 🎨 Interface
<br></br>
<div align="center">
<p>🔗 Inserir a URL da Playlist</p>
  <img src="https://github.com/user-attachments/assets/4b0da67b-60eb-41cc-b14b-3873541998a1" width="400">
<br></br>
<p>📜 Acompanhar o progresso em tempo real</p>
<img src="https://github.com/user-attachments/assets/77091e96-b1fd-4cb3-a078-dc6c4082155b" width="400">
<br></br>
<p>📂 Arquivos baixados</p>
<img src="https://github.com/user-attachments/assets/ac19a221-4f48-4511-a4d1-4a1f3376b5a8" width="400">

</div>
<p><I>No final do processo, todas as músicas baixadas e convertidas estarão na pasta **Músicas** na sua área de trabalho.</I></p>
<br></br>

## 📌 Observações
Caso ocorra algum erro no download, ele será registrado automaticamente em um arquivo .txt salvo na área de trabalho.
Sinta-se à vontade para contribuir com o projeto ou abrir issues no repositório.
## 🧑‍💻 Tecnologias utilizadas
- Python para lógica e processamento.
- Tkinter para a interface gráfica.
- Pytube para comunicação com o YouTube.
- FFmpeg para conversão de áudios.
- Pydub para manipulação de arquivos de áudio.
## 💡 Dicas para Contribuição
- Faça um fork deste repositório.
- Crie um branch para suas alterações: git checkout -b minha-feature.
- Envie suas mudanças: git push origin minha-feature.
- Abra um pull request.
