import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def organizar_arquivos():
    diretorio = entry_path.get()
    if not diretorio:
        messagebox.showerror("Erro", "Um diretório precisa ser especificado")
        return

    extensoes = {
        "Apps": [".apk", ".aab"],
        "Compactados": [".zip", ".rar", ".7z"],
        "Documentos": [".docx", ".txt", ".html", ".pptx"],
        "PDFs": [".pdf"],
        "Imagens": [".jpg", ".jpeg", ".png", ".jfif"],
        "Planilhas": [".xlsx", ".xls", ".csv"],
        "Vídeos": [".mp4", ".mkv", ".avi", ".mov"]
    }

    try:
        for pasta in extensoes.keys():
            caminho_pasta = os.path.join(diretorio, pasta)
            if not os.path.exists(caminho_pasta):
                os.makedirs(caminho_pasta)

        for arquivo in os.listdir(diretorio):
            caminho_arquivo = os.path.join(diretorio, arquivo)
            
            if os.path.isfile(caminho_arquivo) and not arquivo.startswith('.'):
                extensao = os.path.splitext(arquivo)[1].lower()
                movido = False

                for pasta, exts in extensoes.items():
                    if extensao in exts:
                        pasta_destino = os.path.join(diretorio, pasta, arquivo)
                        shutil.move(caminho_arquivo, pasta_destino)
                        movido = True
                        break

                if not movido:
                    pasta_outros = os.path.join(diretorio, "Outros")
                    if not os.path.exists(pasta_outros):
                        os.makedirs(pasta_outros)
                    shutil.move(caminho_arquivo, os.path.join(pasta_outros, arquivo))

        messagebox.showinfo("Sucesso", "Os arquivos foram organizados com sucesso")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

def selecionar_diretorio():
    diretorio = filedialog.askdirectory()
    if diretorio:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, diretorio)

dir = tk.Tk()
dir.title("Organizador de Arquivos")
dir.geometry("400x150")

frame = tk.Frame(dir)
frame.pack(pady=20)

label = tk.Label(frame, text="Diretório:")
label.grid(row=0, column=0)

entry_path = tk.Entry(frame, width=35)
entry_path.grid(row=0, column=1)

btn_browse = tk.Button(frame, text="Procurar", command=selecionar_diretorio)
btn_browse.grid(row=0, column=2, padx=5)

btn_organizar = tk.Button(dir, text="Organizar Arquivos", command=organizar_arquivos)
btn_organizar.pack(pady=10)

dir.mainloop()