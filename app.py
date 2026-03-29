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
    lista.delete(0, ctk.END) #apaga tudo

    tarefas = listarTarefas(todo)

    for i, tarefa in enumerate(tarefas, start=1):
        status = "✔" if tarefa["feito"] else "❌"
        texto = f"{i}. {tarefa['tarefa']} {status}"
        lista.insert(ctk.END, texto)

def concluir():
    selecionado = lista.curselection()

    if selecionado:
        i = selecionado[0] + 1 #a funcao retorna o indice em tupla, ent somamos 1 pq a logica começa em 1

        if concluirTarefa(todo, i):
            atualizarLista(todo)

def remover():
    selecionado = lista.curselection()

    if selecionado:
        i = selecionado[0] + 1

        if removerTarefa(todo, i):
            atualizarLista(todo)

ctk.set_appearance_mode("dark")  # dark mode
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("To-Do List")
janela.geometry("500x600")

entrada = ctk.CTkEntry(janela, width=300, placeholder_text="Digite uma tarefa...")
entrada.pack(pady=10) #o .pack serve para colocar o elemento na janela, pady é o padding vertical

botao = ctk.CTkButton(janela, text="Adicionar", command=adicionar)
botao.pack()

botao_concluir = ctk.CTkButton(janela, text="Concluir", command=concluir)
botao_concluir.pack(pady=5)

botao_remover = ctk.CTkButton(janela, text="Remover", command=remover)
botao_remover.pack(pady=5)

lista = tk.Listbox(janela, width=50)
lista.pack(pady=10)

atualizarLista(todo)
janela.mainloop() #mantem ela aberta

