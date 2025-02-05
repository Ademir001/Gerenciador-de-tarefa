import json

File_name = "tarefa.json"

def carregar():
    try:
        with open(File_name, "r") as f :
            return json.load(f)
    except FileNotFoundError:
        return{}
def salvar(tarefas):
        with open(File_name, "w") as f:
             json.dump(tarefas, f , indent= 4 )
def adicionar(tarefas):
     descricao = input("Digite a tarefa")
     id_tarefa = str(len(tarefas) +1)
     tarefas[id_tarefa] = {"descricao" : descricao, "concluida" : False}
     salvar(tarefas)
     print("Tarefa adicionada") 
def listar(tarefas):
     if not tarefas:
          print("Nenhuma tarefa disponivel ")
          return
     for id , tarefa in tarefas.items():
          status  = "[X]" if tarefa["concluida"] else "[ ]"
          print(f"{id}, -  {status} {tarefa['descricao']}")
def concluido(tarefas):
    listar(tarefas)
    id_tarefa = input("Digite o numero de tarefas para serem concluidas: ")
    if id_tarefa in tarefas: 
        tarefas[id_tarefa]["concluida"] = True
        salvar(tarefas)
        print("Tarefa concluída!")
    else:
         print("Tarefa não encontrada.")
def remover(tarefas):
    listar(tarefas)
    id_tarefa = input("Digite o numero de tarefas para remover")
    if id_tarefa in tarefas:
         del tarefas[id_tarefa]
         salvar(tarefas)
         print("tarefa removida")
    else:
         print("Tarefa não encontrada")
def main():
     tarefas = carregar()
     while True:
          print("\n1. Adicionar Tarefa  \n2. listar Tarefa\n3. concluir Tarefa\n4. remover Tarefa\n5. Sair")
          opcao = input("\n Digite um opção")
          if opcao == "1":
               adicionar(tarefas)
          elif opcao == "2":
               listar(tarefas)
          elif opcao == "3":
               concluido(tarefas)
          elif opcao == "4":
               remover(tarefas)
          elif opcao == "5":
               break
          else:
               print("opção invalidade")
if __name__ == "__main__":
     main()
         
 