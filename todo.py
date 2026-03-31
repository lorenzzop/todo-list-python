import json

# todo = [] (antigo)

try:
    with open("tarefas.json", "r") as f: #se o arquivo ja existe, inicia a lista a partir dele
        todo = json.load(f) #.load serve pra ler
except:
    todo = [] #se n existe, inicia vazia

def adicionarTarefa(todo, tarefa):
        todo.append({
                "tarefa": tarefa,
                "feito": False
            })

        with open("tarefas.json", "w") as arq: #o with open (...) abre o arquivo no modo escrita (por causa do "w", q apaga o arquivo e reescreve)
            json.dump(todo, arq) #.dump sempre pra salvar

                #outros termos q podem ser usados alem do "w": "a" (append, adiciona sem apagar) e "r" (de leitura)

def listarTarefas(todo):
    return todo

def concluirTarefa(todo, i):
    if (i < 1 or i > len(todo)):
        return False
    else:
        todo[i-1]['feito'] = True

        with open("tarefas.json", "w") as arq:
            json.dump(todo, arq)
            
        return True

def removerTarefa(todo, i):
    if (i < 1 or i > len(todo)):
        return False
    else:
        todo.pop(i-1)

        with open("tarefas.json", "w") as arq:
            json.dump(todo, arq)
        
        return True

while True:

    print("\n  -- TO-DO LIST --")
    print("\n 1 - Adicionar")
    print(" 2 - Listar")
    print(" 3 - Concluir")
    print(" 4 - Remover")
    print(" 5 - Sair")

    op = (input("\nEscolha a opção: "))

    match op:
        case "1":
            tarefa = input("Insira a tarefa: ")
            adicionarTarefa(todo, tarefa)
            
        case "2":
            listarTarefas(todo)
            
        case "3": 
            i = int(input("Qual tarefa deseja concluir? "))
            concluirTarefa(todo, i)

        case "4":
            i = int(input("Qual tarefa deseja remover? "))
            removerTarefa(todo, i)

        case "5":
            print("Programa finalizado")
            break
    


    