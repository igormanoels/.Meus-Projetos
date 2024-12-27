from tkinter import *
from tkinter import messagebox


# Antes do programa iniciar ele deve descobrir se o sistema é windows ou linux, pra definir o local padrão
# Variáveis Globais
SISTEMA = 'windows'
LOCAL = None
FORMATO = 0
LINK = None


# Cores
preto = "#1E1E1E"
laranja = "#DF9C57"
branco = "#F1F1F1"
vermelho = "#721B1B"


# Funções
def buscarDiretorio():
    pass

def alteraFormatoMP4():
    global FORMATO, LOCAL
    FORMATO = 'MP4'
    LOCAL = "C://Users//Public//Videos//YT Download//Videos"

def alteraFormatoMP3():
    global FORMATO, LOCAL
    FORMATO = 'MP3'
    LOCAL = "C://Users//Public//Videos//YT Download//Audio"

def iniciarDownload():
    global LINK, FORMATO
    LINK = etLink.get()

    if FORMATO == 0:
        messagebox.showinfo("Atenção", "Antes de inciar o download selecione um formato.")
        return

    if LINK is None:
        print(LINK)
        messagebox.showinfo("Atenção", "Antes de inciar o download informe o link desejado.")
        return

    match FORMATO:
        Case 'MP4':
            try:
                yt = YouTube(url, on_progress_callback=on_progress)  # Cria o objeto YouTube
                print(f"Título do vídeo: {yt.title}")  # Exibe o título do vídeo
                ys = yt.streams.get_highest_resolution()  # Obtém o stream de maior resolução
                ys.download(output_path=destinoVideos)  # Faz o download do vídeo
                print("Download concluído!")
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
        '''
        Case 'MP3':
            try:
                options = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '320',
                    }],
                    'ffmpeg_location': 'src/bin/ffmpeg.exe',  # Caminho relativo para o FFmpeg
                    'outtmpl': 'audios/%(title)s.%(ext)s',
                }

                with yt_dlp.YoutubeDL(options) as ydl:
                    ydl.download([url])
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
'''


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
etDestino.insert(0, 'Informe aqui a pasta de destino')
etDestino.place(x=80, y=183)

btnProcurar = Button(tela, text='Procurar', font='Viga', bg=branco, fg=laranja, width=12, height=2)
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
