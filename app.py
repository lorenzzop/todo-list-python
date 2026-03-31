import customtkinter as ctk
import tkinter as tk
import json
from todo import adicionarTarefa, listarTarefas, concluirTarefa, removerTarefa #importando funcoes criadas no todo.py

try:
    with open("tarefas.json", "r") as f: #se o arquivo ja existe, inicia a lista a partir dele
        todo = json.load(f) #.load serve pra ler
except:
    todo = [] #se n existe, inicia vazia

def adicionar():
    tarefa = entrada.get()

    if tarefa.strip() != "":
        adicionarTarefa(todo, tarefa)
        entrada.delete(0, ctk.END)
        atualizarLista(todo)

def atualizarLista(todo):
    for widget in frame_lista.winfo_children():
        widget.destroy()

    tarefas = listarTarefas(todo)

    for i, tarefa in enumerate(tarefas, start=1):
        texto = f"{tarefa['tarefa']}"
        status = "✔" if tarefa["feito"] else "❌"

        item_frame = ctk.CTkFrame(frame_lista)
        item_frame.pack(fill="x", pady=5, padx=10)

        label = ctk.CTkLabel(item_frame, text=f"{status} {texto}")
        label.pack(side="left", padx=10)

        botao_concluir = ctk.CTkButton(
            item_frame, text="✔", width=40,
            command=lambda i=i: concluir_click(i)
        )
        botao_concluir.pack(side="right", padx=5)

        botao_remover = ctk.CTkButton(
            item_frame, text="X", width=40,
            fg_color="red",
            command=lambda i=i: remover_click(i)
        )
        botao_remover.pack(side="right")

def concluir_click(i):
    if concluirTarefa(todo, i):
        atualizarLista(todo)

def remover_click(i):
    if removerTarefa(todo, i):
        atualizarLista(todo)

ctk.set_appearance_mode("dark")  # dark mode
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("To-Do List")
janela.geometry("450x600")

entrada = ctk.CTkEntry(janela, width=300, placeholder_text="Digite uma tarefa...")
entrada.pack(pady=10) #o .pack serve para colocar o elemento na janela, pady é o padding vertical

botao = ctk.CTkButton(janela, text="Adicionar", command=adicionar)
botao.pack()

frame_lista = ctk.CTkFrame(janela)
frame_lista.pack(pady=10, fill="both", expand=True)

atualizarLista(todo)
janela.mainloop() #mantem ela aberta
