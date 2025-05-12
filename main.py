import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def organizar_arquivos():
    diretorio = caminho.get()
    if not diretorio:
        messagebox.showerror("Erro", "Um diretório precisa ser especificado")
        return

    extensoes = {
        "Apps": [".apk", ".aab"],
        "Compactados": [".zip", ".rar", ".7z"],
        "Documentos": [".docx", ".txt", ".html", ".pptx"],
        "PDFs": [".pdf"],
        "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
        "Planilhas": [".xlsx", ".xls", ".csv"],
        "Vídeos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"]
    }

    try:
        for pasta in extensoes.keys():
            caminho_pasta = os.path.join(diretorio, pasta) #concatena os caminhos, criando um caminho unico
            if not os.path.exists(caminho_pasta):
                os.makedirs(caminho_pasta)

        for arquivo in os.listdir(diretorio):
            caminho_arquivo = os.path.join(diretorio, arquivo)
            
            if os.path.isfile(caminho_arquivo) and not arquivo.startswith("."): #verifica se é um arquivo e ignora arquivos que começam com "."
                extensao = os.path.splitext(arquivo)[1].lower() #separa o nome do arquivo da extensao
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
                        os.makedirs(pasta_outros) #cria a pasta "Outros" caso o arquivo nao tenha sido movido
                    shutil.move(caminho_arquivo, os.path.join(pasta_outros, arquivo)) #move os arquivos para a pasta "Outros"

        messagebox.showinfo("Sucesso", "Os arquivos foram organizados com sucesso")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

def selecionar_diretorio():
    diretorio = filedialog.askdirectory()
    if diretorio:
        caminho.delete(0, tk.END)
        caminho.insert(0, diretorio)

dir = tk.Tk()
#dir.iconphoto(False, tk.PhotoImage(file="images\python_with_glasses.png"))
dir.title("Organizador de Arquivos")
dir.geometry("400x150")

principal = tk.Frame(dir)
principal.pack(pady=20)

label = tk.Label(principal, text="Diretório:")
label.grid(row=0, column=0)

caminho = tk.Entry(principal, width=35)
caminho.grid(row=0, column=1)

botao_procurar = tk.Button(principal, text="Procurar", activebackground= "#708090", command=selecionar_diretorio)
botao_procurar.grid(row=0, column=2, padx=0)

botao_organizar = tk.Button(dir, text="Organizar Arquivos", activebackground= "#708090", command=organizar_arquivos)
botao_organizar.pack(pady=10)

dir.mainloop()