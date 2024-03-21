import psutil
from tkinter import *

# Cores
COR_FUNDO = "#ffffff"
COR_TEXTO = "#000000"

# Janela principal
janela = Tk()
janela.geometry("800x600")
janela.title("Monitor de Processos")

# Lista de processos
lista_processos = Listbox(janela, bg=COR_FUNDO, fg=COR_TEXTO)
lista_processos.pack(fill=BOTH, expand=True)

# Atualizar lista de processos
def atualizar_lista():
    lista_processos.delete(0, END)
    for processo in psutil.process_iter(["pid", "name", "cpu_percent"]):
        texto = f"PID: {processo.info['pid']}"
        texto += f" - Nome: {processo.info['name']}"
        texto += f" - Uso CPU: {processo.info['cpu_percent']:.2f}%"
        lista_processos.insert(END, texto)

# Atualizar lista a cada segundo
janela.after(5000, atualizar_lista)

# Iniciar loop principal
janela.mainloop()
