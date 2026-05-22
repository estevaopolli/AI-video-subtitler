This is a Brazilian project, so the first part is written in Portuguese. If Portuguese is not your first language, you can find the English version at the end of this page.

# AI Video Subtitler

> MVP experimental focado em geração automática de legendas utilizando inteligência artificial e processamento de vídeo em Python.

O AI Video Subtitler é uma aplicação desenvolvida em Python capaz de gerar legendas automaticamente para vídeos utilizando inteligência artificial.

O projeto utiliza o Whisper da OpenAI para realizar a transcrição do áudio e o MoviePy para renderizar as legendas diretamente no vídeo final.

A aplicação executa o modelo de IA localmente para a transcrição do vídeo. Também é possível visualizar e editar a transcrição antes de exportar o vídeo legendado.
---

# Funcionalidades

* Transcrição automática de áudio utilizando IA
* Execução local do modelo Whisper
* Campo editável para correção das legendas
* Geração automática de arquivos `.srt`
* Renderização das legendas diretamente no vídeo
* Suporte à aceleração por GPU com CUDA
* Fallback automático para CPU caso CUDA não esteja disponível

---

# Tecnologias Utilizadas

* Python
* OpenAI Whisper
* MoviePy
* FFmpeg
* PyTorch

---

# Como Funciona

1. O usuário envia um vídeo
2. O Whisper realiza a transcrição localmente
3. O texto gerado pode ser editado manualmente
4. A aplicação cria um arquivo `.srt`
5. O MoviePy renderiza o vídeo final legendado

---

# Requisitos

* Python 3.10+
* FFmpeg instalado e adicionado ao PATH
* GPU compatível com CUDA (opcional, mas recomendado)

---

# Instalação

Clone o repositório:

```bash id="5g1yms"
git clone https://github.com/estevaopolli/AI-video-subtitler.git
```

Entre na pasta do projeto:

```bash id="g2mmdg"
cd AI-video-subtitler
```

Instale as dependências:

```bash id="mtq4ji"
pip install -r requirements.txt
```

---

# Instalando o FFmpeg

O FFmpeg é necessário para o processamento de vídeo.

Builds para Windows:
https://www.gyan.dev/ffmpeg/builds/

Site oficial:
https://ffmpeg.org/

Após instalar, certifique-se de adicionar o FFmpeg ao PATH do sistema.

---

# Aceleração por GPU (Opcional)

Para obter uma geração de legendas mais rápida, instale a versão do PyTorch compatível com a sua versão do CUDA.

Guia oficial:
https://pytorch.org/get-started/locally/

Exemplo para CUDA 13.0:

```bash id="s1dmy8"
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu130
```

A aplicação detecta automaticamente se CUDA está disponível:

```python id="hvokd4"
device = "cuda" if torch.cuda.is_available() else "cpu"
```

---

# Executando o Projeto

```bash id="cpr3qh"
python main.py
```

---

# Melhorias Futuras

* Melhorias de UI/UX
* Personalização do estilo das legendas
* Tradução automática
* Versão SaaS/cloud
* Pipeline de renderização mais rápido
* Processamento em lote
* Legendas animadas
* Detecção automática de speakers

---

# Licença

Este projeto foi desenvolvido para fins de estudo e experimentação com inteligência artificial aplicada ao processamento de vídeo.

---

# AI Video Subtitler

> Experimental MVP focused on AI-powered subtitle generation and video processing using Python.

AI Video Subtitler is a Python-based application that automatically generates subtitles for videos using artificial intelligence.

The project uses OpenAI Whisper for speech transcription and MoviePy for subtitle rendering directly into the final video.

The application runs the AI model locally for vídeo transcription. Also, it's possible view and edit the transcript before exporting the subtitle video.
---

# Features

* Automatic audio transcription using AI
* Local Whisper model execution
* Editable subtitle text
* Automatic `.srt` subtitle generation
* Subtitle rendering directly into the video
* GPU acceleration with CUDA support
* Automatic CPU fallback when CUDA is unavailable

---

# Technologies

* Python
* OpenAI Whisper
* MoviePy
* FFmpeg
* PyTorch

---

# How It Works

1. Upload a video file
2. Whisper transcribes the audio locally
3. The generated text can be manually edited
4. The application creates an `.srt` subtitle file
5. MoviePy renders the final subtitled video

---

# Requirements

* Python 3.10+
* FFmpeg installed and added to PATH
* CUDA-compatible GPU (optional, but recommended)

---

# Installation

Clone the repository:

```bash id="o95ph7"
git clone https://github.com/estevaopolli/AI-video-subtitler.git
```

Enter the project folder:

```bash id="4y3ydh"
cd AI-video-subtitler
```

Install dependencies:

```bash id="3dxyuh"
pip install -r requirements.txt
```

---

# Installing FFmpeg

FFmpeg is required for video processing.

Windows builds:
https://www.gyan.dev/ffmpeg/builds/

Official website:
https://ffmpeg.org/

After installation, make sure FFmpeg is added to your system PATH.

---

# GPU Acceleration (Optional)

For faster subtitle generation, install the CUDA-compatible version of PyTorch for your GPU.

Official installation guide:
https://pytorch.org/get-started/locally/

Example for CUDA 13.0:

```bash id="yb7utg"
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu130
```

The application automatically detects CUDA support:

```python id="v8gwv8"
device = "cuda" if torch.cuda.is_available() else "cpu"
```

---

# Running the Project

```bash id="iowm61"
python main.py
```

---

# Future Improvements

* Better UI/UX
* Subtitle style customization
* Translation support
* Cloud/SaaS version
* Faster rendering pipeline
* Batch video processing
* Animated subtitles
* Automatic speaker detection

---

# License

This project was created for study purposes and experimentation with AI-powered video processing.

