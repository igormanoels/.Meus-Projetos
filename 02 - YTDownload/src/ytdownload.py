from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory
from pytubefix import YouTube
from pytubefix.cli import on_progress
import yt_dlp



# Antes do programa iniciar ele deve descobrir se o sistema é windows ou linux, pra definir o local padrão
# Variáveis Globais
SISTEMA = 'windows'
LOCAL = 'Informe aqui a pasta de destino'
FORMATO = 0
LINK = 'null'


# Cores
preto = "#1E1E1E"
laranja = "#DF9C57"
branco = "#F1F1F1"
vermelho = "#721B1B"


# Funções
def buscarDiretorio():
    novo_local = askdirectory(title="Selecione a pasta desejada")
    atualizarDiretorio(novo_local)
    print(LOCAL)


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


def iniciarDownload():
    global LINK, FORMATO
    LINK = etLink.get()
    ffmpeg = '/src/bin/ffmpeg.exe'

    if LOCAL == 'Informe aqui a pasta de destino':
        messagebox.showinfo("Atenção!", "Antes de iniciar o download informe o local desejado.")
        return

    if FORMATO == 0:
        messagebox.showinfo("Atenção!", "Antes de inciar o download selecione um formato.")
        return

    if LINK == 'null' or LINK == 'Insira seu link aqui!' or LINK == '': 
        print(LINK)
        messagebox.showinfo("Atenção!", "Antes de inciar o download informe o link desejado.")
        return


    match FORMATO:
        case 'MP4':
            try:
                yt = YouTube(LINK, on_progress_callback=on_progress)  # Cria o objeto YouTube
                print(f"Título do vídeo: {yt.title}")  # Exibe o título do vídeo
                ys = yt.streams.get_highest_resolution()  # Alterar para escolher a qualidade de 720x480 
                ys.download(output_path=LOCAL)  # Faz o download do vídeo
                print("Download concluído!")
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
        case 'MP3':
            try:
                options = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '320',
                    }],
                    'ffmpeg_location': 'D:\\GitHub\\.Meus-Projetos\\02 - YTDownload\\src\\bin\\ffmpeg.exe',  
                    # alterar o caminho absoluto, pelo relativo dentro do projeto
                    'outtmpl': LOCAL+'/%(title)s.%(ext)s',
                }

                with yt_dlp.YoutubeDL(options) as ydl:
                    ydl.download([LINK])
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro: {e}")



# Propriedades da Tela
tela = Tk()
tela.title('YT Download')
#tela.iconphoto(False, PhotoImage(file='/docs/figma/design system/icon-janela.png'))
tela.geometry('720x480')
tela.resizable(width=False, height=False)
tela.config(background=branco, border=False)


## Componentes da tela

#lbLogo = Label(tela, image='D://GitHub//.Meus-Projetos//02 - YTDownload//docs//figma//design system//Logo final.png').place(x=255, y=44)

etDestino = Entry(tela, width=35, font=('Viga 16'))
etDestino.insert(0, LOCAL)
etDestino.place(x=80, y=183)

btnProcurar = Button(tela, text='Procurar', command=buscarDiretorio, font='Viga', bg=branco, fg=laranja, width=12, height=2)
btnProcurar.place(x=520, y=187)

etLink = Entry(tela, width=46, font=('Viga 16'))
etLink.insert(0, 'Insira seu link aqui!')
etLink.place(x=80, y=247)

btnFormato4 = Button(tela, command=alteraFormatoMP4, text='MP4', font='Viga', bg=branco, fg=laranja, width=12, height=2)
btnFormato4.place(x=248, y=311)

btnFormato3 = Button(tela, command=alteraFormatoMP3, text='MP3', font='Viga', bg=branco, fg=laranja, width=12, height=2)
btnFormato3.place(x=384, y=311)

btnDonwload = Button(tela, command=iniciarDownload, text='Download', font='Viga', bg=branco, fg=laranja, width=12, height=2)
btnDonwload.place(x=520, y=311)



tela.mainloop()
