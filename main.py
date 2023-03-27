import pyttsx3
from PyPDF2 import PdfReader

ler_pdf = PdfReader('Profile.pdf')
auto_falante = pyttsx3.init()

texto = ""
for numero_pagina in range(len(ler_pdf.pages)):
    texto += ler_pdf.pages[numero_pagina].extract_text()

texto_limpo = texto.strip().replace("\n", ' ')
print(texto_limpo)

auto_falante.save_to_file(texto_limpo, "Profile.mp3")  
auto_falante.runAndWait()
auto_falante.stop()
