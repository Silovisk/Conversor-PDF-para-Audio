import pyttsx3
import PyPDF2
import tkinter as tk
from tkinter import filedialog
import os

# função para selecionar arquivo
def selecionar_arquivo():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[('PDF Files', '*.pdf')])
    return file_path

# seleciona o arquivo PDF
file_path = selecionar_arquivo()

# leitura do arquivo PDF
with open(file_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    texto = ""
    for num_pagina in range(len(reader.pages)):
        texto += reader.pages[num_pagina].extract_text()
    texto_limpo = texto.strip().replace('\n', ' ')
    print(texto_limpo)

# criação do arquivo de áudio MP3 com o mesmo nome do arquivo de entrada
nome_arquivo = os.path.splitext(os.path.basename(file_path))[0] + '.mp3'
auto_falante = pyttsx3.init()
auto_falante.save_to_file(texto_limpo, nome_arquivo)
auto_falante.runAndWait()
auto_falante.stop()
