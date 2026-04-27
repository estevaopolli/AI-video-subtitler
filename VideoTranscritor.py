import whisper
from whisper.utils import get_writer
import os
import tkinter as tk
from tkinter import filedialog

from moviepy import TextClip, CompositeVideoClip
from moviepy.video.tools.subtitles import SubtitlesClip, file_to_subtitles
from moviepy.video.io.VideoFileClip import VideoFileClip

class Application:
    def __init__(self, mainWindow):
        #Caixa de texto para a transcrição
        self.textBox = tk.Text(mainWindow, width=100, height = 30)
        self.textBox.pack(pady=10)

        #Caixa de texto para o nome do arquivo
        self.dir = tk.Entry(mainWindow, width=100)
        self.dir.pack(pady=10)
        self.dir.config(state="readonly")

        #Botão para selecionar o arquivo
        self.selectFileBtn = tk.Button(mainWindow, text="Selecionar Arquivo", command=self.get_file)
        self.selectFileBtn.pack(pady=10)

        #Botão para gerar a transcrição
        self.transcriptionBtn = tk.Button(mainWindow, text="Transcrever", command=self.get_transcription)
        self.transcriptionBtn.pack(pady=10)

        #Botão para iniciar a criação do video com legenda
        self.startBtn = tk.Button(mainWindow, text="Gerar Video", command=self.create_video)
        self.startBtn.pack(pady=10)

    #Pega o arquivo
    def get_file(self):
        fileSelect = tk.filedialog.askopenfile(initialdir="/Videos")
        self.clip = VideoFileClip(fileSelect.name)
        self.fileName = fileSelect.name
        self.dir.config(state="normal")
        self.dir.delete(0, tk.END)
        self.dir.insert(0, self.fileName)
        self.dir.config(state="readonly")

    #Pega a transcrição
    def get_transcription(self):
        if os.path.exists(self.fileName):
            print("Arquivo existe")

            #Modelo de IA para transcrever
            model = whisper.load_model("turbo", device="cuda")
            result = model.transcribe(self.fileName, language="pt", fp16=False)
            print(result)

            self.textBox.delete("1.0", tk.END)
            self.edited_subscriptions = []

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
            print(self.edited_subscriptions)
        else:
            print("Arquivo nao existe")

    def create_video(self):
        print(self.edited_subscriptions)

        #Adiciona a edição feita no item "transcription"
        for i in range(len(self.edited_subscriptions)):
            self.edited_subscriptions[i].update({"transcription": self.textBox.get(f"{i + 1}.1", f"{i + 1}.end")})

        #Cria o arquivo srt

        with open("captions.srt", "w", encoding="UTF-8") as file:
            for caption in self.edited_subscriptions:
                file.write(f"{int(caption['id']) + 1}\n")
                file.write(f"{caption['start']} -> {caption['end']}\n")
                file.write(f"{caption['transcription']}\n \n")

        generator = lambda text: TextClip(
            text = text,
            font="arial.ttf",
            font_size=24,
            color='yellow',
            method='caption',
            size=(int(self.clip.w * 0.9), None))

        print(generator)
        sub = SubtitlesClip("captions.srt", make_textclip = generator, encoding="utf-8")
        video = CompositeVideoClip([self.clip, sub.with_position(("center", 0.85), relative=True)])
        video.write_videofile("result.mp4", fps=self.clip.fps, codec="libx264", audio_codec="aac")


#Tela principal
mainWindow = tk.Tk()
mainWindow.geometry("1080x720")
mainWindow.title("Legendador de Vídeo")
app = Application(mainWindow)

mainWindow.mainloop()










