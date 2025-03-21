import json

File_name = "tarefa.json"

def carregar():
    try:
        with open(File_name, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def salvar(tarefas):
    with open(File_name, "w") as f:
        json.dump(tarefas, f, indent=4)

def adicionar(tarefas):
    descricao = input("Digite a descrição da tarefa: ")
    id_tarefa = str(len(tarefas) + 1)
    tarefas[id_tarefa] = {"descricao": descricao, "concluida": False}
    salvar(tarefas)
    print("Tarefa adicionada")

def listar(tarefas):
    if not tarefas:
        print("Nenhuma tarefa disponível.")
        return
    for id, tarefa in tarefas.items():
        status = "[X]" if tarefa["concluida"] else "[ ]"
        print(f"Tarefa {id}: {tarefa['descricao']} - Status: {status}")

def concluir(tarefas):
    listar(tarefas)
    id_tarefa = input("Digite o número da tarefa para marcar como concluída: ")
    if id_tarefa in tarefas:
        tarefas[id_tarefa]["concluida"] = True
        salvar(tarefas)
        print("Tarefa concluída!")
    else:
        print("Tarefa não encontrada.")

def remover(tarefas):
    listar(tarefas)
    id_tarefa = input("Digite o número da tarefa para remover: ")
    if id_tarefa in tarefas:
        del tarefas[id_tarefa]
        salvar(tarefas)
        print("Tarefa removida!")
    else:
        print("Tarefa não encontrada.")

def main():
    tarefas = carregar()
    while True:
        print("\n1. Adicionar Tarefa\n2. Listar Tarefas\n3. Concluir Tarefa\n4. Remover Tarefa\n5. Sair")
        opcao = input("Digite a opção desejada: ")
        if opcao == "1":
            adicionar(tarefas)
        elif opcao == "2":
            listar(tarefas)
        elif opcao == "3":
            concluir(tarefas)
        elif opcao == "4":
            remover(tarefas)
        elif opcao == "5":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()