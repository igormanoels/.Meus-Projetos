from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.filedialog import askdirectory
from pytubefix import YouTube
from pytubefix.cli import on_progress
import yt_dlp
import threading
import os 


# Na próxima versão, antes do programa iniciar ele deve descobrir se o sistema é windows ou linux, pra definir o local padrão
# Variáveis Globais
SISTEMA = 'windows'
LOCAL = os.path.join(os.environ['USERPROFILE'], 'Downloads')
FORMATO = 0
LINK = 'Insira seu link aqui!'


# Usar na próxima versão essa tabela de cores, com a possibilidade de alterar os modos (Dark/Light)
preto = "#1E1E1E"
laranja = "#DF9C57"
branco = "#F1F1F1"
vermelho = "#721B1B"


# Funções
def buscarDiretorio():
    novo_local = askdirectory(title="Selecione a pasta desejada")
    atualizarDiretorio(novo_local)


def atualizarDiretorio(novo_local):
    global LOCAL
    LOCAL = novo_local
    etDestino.delete(0, END)
    etDestino.insert(0, LOCAL)


def alteraFormatoMP4():
    global FORMATO
    FORMATO = 'MP4'


def alteraFormatoMP3():
    global FORMATO
    FORMATO = 'MP3'


def zerarPrograma():
    global LINK
    barraProgresso['value'] = 0
    etLink.delete(0, END)
    etLink.insert(0, 'Insira aqui um novo link!')


def downloadVideo():
    # Na próxima versão necessariamente o programa deve mapear a pasta videos ou trocar pela escolhida
    # pastaVideos = os.path.join(os.environ['USERPROFILE'], 'Vídeos') 
    def progressoDaBarra(youtubestream, chunk, bytes_remaining):
        downloaded = youtubestream.filesize - bytes_remaining
        barraProgresso["value"] = downloaded
        tela.update_idletasks()

    # Na próxima versão trazer resoluções mais altas que 720p
    try:
        yt = YouTube(LINK, on_progress_callback=progressoDaBarra)  
        titulo = yt.title
        #youtubestream = yt.streams.get_highest_resolution()
        youtubestream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
 
        barraProgresso['maximum'] = youtubestream.filesize
        youtubestream.download(output_path=LOCAL)
        messagebox.showinfo("Download concluído com sucesso!", f"Título: {titulo} \nFormato: MP4") 
        zerarPrograma()
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
        zerarPrograma()


def downloadMusica():
    # Na próxima versão necessariamente o programa deve mapear a pasta videos ou trocar pela escolhida
    # pastaMusicas = os.path.join(os.environ['USERPROFILE'], 'Músicas')
    def status_hook(d):
        if d['status'] == 'downloading':
            progress = int(d['downloaded_bytes'] / d['total_bytes'] * 100)
            barraProgresso['value'] = progress
            tela.update_idletasks()

    try:
        options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio', 
            'preferredcodec': 'mp3', 
            'preferredquality': '320',}],
        'ffmpeg_location': 'D:\\GitHub\\.Meus-Projetos\\02 - YTDownload\\src\\bin\\ffmpeg.exe', # alterar o caminho absoluto, pelo relativo dentro do projeto
        'outtmpl': LOCAL+'/%(title)s.%(ext)s',
        'progress_hooks': [status_hook],
    }
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([LINK])
            info_dict = ydl.extract_info(LINK, download=False)
            titulo = info_dict.get('title', 'Título não disponível')
            messagebox.showinfo("Download concluído com sucesso!", f"Título: {titulo} \nFormato: MP3")
            zerarPrograma()

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}") 
        zerarPrograma()



def iniciarDownload():
    global LINK, FORMATO
    LINK = etLink.get()
    ffmpeg = '/src/bin/ffmpeg.exe'

    if LOCAL == 'Informe aqui a pasta de destino':
        messagebox.showinfo("Atenção!", "Antes de iniciar o download informe o local desejado.")
        return
    elif FORMATO == 0:
        messagebox.showinfo("Atenção!", "Antes de inciar o download selecione um formato.")
        return
    elif LINK == 'null' or LINK == 'Insira seu link aqui!' or LINK == '': 
        print(LINK)
        messagebox.showinfo("Atenção!", "Antes de inciar o download informe o link desejado.")
        return

    match FORMATO:
        case 'MP4':
            threading.Thread(target=downloadVideo).start()
        case 'MP3':
            threading.Thread(target=downloadMusica).start()


def gerarBotao(parent, text, command):
    return Button (
        parent, 
        text = text, 
        command = command, 
        font='Viga', 
        bg="#1E1E1E", 
        fg="#DF9C57", 
        width=12, 
        height=2, 
        relief="ridge", 
        bd=2, 
        activebackground="#DF9C57", 
        activeforeground="#1E1E1E",
    )


# Propriedades da Tela
tela = Tk()
tela.title('YT Download')
tela.geometry('720x480')
tela.resizable(width=False, height=False)
tela.config(background="#1E1E1E", border=False)


## Componentes da tela
img = PhotoImage(file="D:\GitHub\.Meus-Projetos//02 - YTDownload\src\img\logo.png")
lbLogo = Label(tela, image=img, bg="#1E1E1E")
lbLogo.place(x=255, y=44)

etDestino = Entry(tela, width=35, font=('Viga 16'), fg="#1E1E1E", bg="#DF9C57")
etDestino.insert(0, LOCAL)
etDestino.place(x=80, y=183)

btnProcurar = gerarBotao(tela, text='Procurar', command=buscarDiretorio)
btnProcurar.place(x=520, y=187)

etLink = Entry(tela, width=46, font=('Viga 16'), fg="#1E1E1E", bg="#DF9C57")
etLink.insert(0, LINK)
etLink.place(x=80, y=247)

btnFormato4 = gerarBotao(tela, command=alteraFormatoMP4, text='MP4')
btnFormato4.place(x=248, y=311)

btnFormato3 = gerarBotao(tela, command=alteraFormatoMP3, text='MP3')
btnFormato3.place(x=384, y=311)

btnDonwload = gerarBotao(tela, command=iniciarDownload, text='Download')
btnDonwload.place(x=520, y=311)


def configurarBarraProgresso():
    estilo = ttk.Style()
    estilo.theme_use('clam')
    estilo.configure("TProgressbar",
                     thickness=30,
                     troughcolor="#F1F1F1",
                     background="#DF9C57",
                     )

configurarBarraProgresso()

barraProgresso = ttk.Progressbar(tela, orient=HORIZONTAL, length=704, mode='determinate', style="TProgressbar")
barraProgresso.place(x=8, y=448)


# Dados do Desenvolvedor e Versão do projeto
lbDesenvolvedor = Label(tela, font=('Viga 10'), text="GitHub igormanoels", bg="#1E1E1E", fg="#F1F1F1")
lbDesenvolvedor.place(x=600, y=5)
lbVersao = Label(tela, font=('Viga 8'), text="Versão 1.0.0", bg="#1E1E1E", fg="#F1F1F1")
lbVersao.place(x=650, y=25)


tela.mainloop()

