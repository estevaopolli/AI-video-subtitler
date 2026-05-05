import whisper
from whisper.utils import get_writer
import os
import tkinter as tk
from tkinter import filedialog

from moviepy import TextClip, CompositeVideoClip
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.io.VideoFileClip import VideoFileClip

class Application:
    def __init__(self, mainWindow):
        #Textbox for transcription / Caixa de texto para a transcrição
        self.textBox = tk.Text(mainWindow, width=100, height = 30)
        self.textBox.pack(pady=10)

        #Textbox for view the file path / Caixa de texto para visualizar o caminho do arquivo
        self.dir = tk.Entry(mainWindow, width=100)
        self.dir.pack(pady=10)
        self.dir.config(state="readonly")

        #Button for select file / Botão para selecionar o arquivo
        self.selectFileBtn = tk.Button(mainWindow, text="Selecionar Arquivo", command=self.get_file)
        self.selectFileBtn.pack(pady=10)

        #Button for generate the transcription / Botão para gerar a transcrição
        self.transcriptionBtn = tk.Button(mainWindow, text="Transcrever", command=self.get_transcription)
        self.transcriptionBtn.pack(pady=10)

        #Button for create the new video with captions / Botão para iniciar a criação do novo video com a legenda
        self.startBtn = tk.Button(mainWindow, text="Gerar Video", command=self.create_video)
        self.startBtn.pack(pady=10)

    #Get the file / Pega o arquivo
    def get_file(self):
        fileSelect = tk.filedialog.askopenfile(initialdir="/Videos")
        self.clip = VideoFileClip(fileSelect.name)
        self.fileName = fileSelect.name

        #Edit the file path textBox / Edita a caixa de texto do caminho do arquivo
        self.dir.config(state="normal")
        self.dir.delete(0, tk.END)
        self.dir.insert(0, self.fileName)
        self.dir.config(state="readonly")

    #Get the transcription / Pega a transcrição
    def get_transcription(self):
        if os.path.exists(self.fileName):
            print("Arquivo existe")

            #Transcription AI Model / Modelo de IA de transcrição
            model = whisper.load_model("turbo", device="cuda")
            result = model.transcribe(self.fileName, language="pt", fp16=False)
            print(result)

            self.textBox.delete("1.0", tk.END)
            self.edited_subscriptions = []

            #Transform the Whisper's output into a readable SRT pattern / Transforma a saída do Whisper para o um padrão SRT legível
            for sentence in result["segments"]:
                total_ms_start = int(round(sentence['start'] * 1000))
                total_ms_end = int(round(sentence['end'] * 1000))

                start_hours = total_ms_start // 3600000
                start_minutes = (total_ms_start % 3600000) // 60000
                start_seconds = (total_ms_start % 600000) // 1000
                start_milliseconds = total_ms_start % 1000

                end_hours = total_ms_end // 3600000
                end_minutes = (total_ms_end % 3600000) // 60000
                end_seconds = (total_ms_end % 600000) // 1000
                end_milliseconds = total_ms_end % 1000

                converted_start = f"{start_hours:02}:{start_minutes:02}:{start_seconds:02},{start_milliseconds:03}"
                converted_end = f"{end_hours:02}:{end_minutes:02}:{end_seconds:02},{end_milliseconds:03}"

                self.edited_subscriptions.append({
                    "id": sentence['id'],
                    "start": converted_start,
                    "end": converted_end,
                    "transcription": sentence['text']
                })
                self.textBox.insert(tk.END,f"{sentence['text']}\n")
        else:
            print("Arquivo nao existe")


    def create_video(self):
        print(self.edited_subscriptions)

        #Add the edit made to the "transcription item" / Adiciona a edição feita no item "transcription"
        for i, item in enumerate(self.edited_subscriptions):
            self.edited_subscriptions[i].update({"transcription": self.textBox.get(f"{i + 1}.1", f"{i + 1}.end")})

        #Create the srt file / Cria o arquivo srt

        with open("captions.srt", "w", encoding="UTF-8") as file:
            for caption in self.edited_subscriptions:
                file.write(f"{int(caption['id']) + 1}\n")
                file.write(f"{caption['start']} -> {caption['end']}\n")
                file.write(f"{caption['transcription']}\n \n")

        #Text settings / Configurações do texto
        generator = lambda text: TextClip(
            text = text,
            font="arial.ttf",
            font_size= int(self.clip.h * 0.05),
            color='white',
            stroke_color = 'black',
            stroke_width = 2,
            method='caption',
            text_align='center',
            size=(int(self.clip.w * 0.9), int(self.clip.h * 0.2)))

        print(generator)

        #Composite and Render the video / #Compõe e renderiza o vídeo
        sub = SubtitlesClip("captions.srt", make_textclip = generator, encoding="utf-8")
        video = CompositeVideoClip([self.clip, sub.with_position(("center", 0.75), relative=True)])
        video.write_videofile("result.mp4", fps=self.clip.fps, codec="libx264", audio_codec="aac", bitrate="5000k")


#Main Screen / Tela principal
mainWindow = tk.Tk()
mainWindow.geometry("1080x720")
mainWindow.title("Legendador de Vídeo")
app = Application(mainWindow)

mainWindow.mainloop()










