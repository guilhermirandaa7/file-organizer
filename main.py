import os
from tkinter.filedialog import askdirectory 

caminho = askdirectory(title='selecione uma pasta')

lista_caminhos = os.listdir(caminho)
lista_caminhos.sort()
print(lista_caminhos)

locals = {
    "imagens": (".png", ".jpg", ".jpeg"),
    "videos": (".mp4", ".avi", ".mkv"),
    "documentos": (".pdf", ".docx", ".txt"),
    "csv": (".csv"),
}

for arquivo in lista_caminhos:
   nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
   