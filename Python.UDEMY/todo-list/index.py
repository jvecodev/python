
import json

# Lista de tarefas
todo_list = []



# Função para exibir o menu
def show_menu():
    print("\nTo-Do List")
    print("1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Listar Tarefas")
    print("4. Sair")

# Função para adicionar uma tarefa
def add_task():
    task = input("Digite a tarefa: ")
    todo_list.append(task)
    print(f"Tarefa '{task}' adicionada!")

# Função para remover uma tarefa
def remove_task():
    list_tasks()
    try:
        task_index = int(input("Digite o número da tarefa que deseja remover: ")) - 1
        removed_task = todo_list.pop(task_index)
        print(f"Tarefa '{removed_task}' removida!")
    except (IndexError, ValueError):
        print("Número de tarefa inválido!")

# Função para listar todas as tarefas
def list_tasks():
    if not todo_list:
        print("Nenhuma tarefa adicionada.")
    else:
        print("\nTarefas:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")

# Função principal
def main():
    while True:
        show_menu()
        choice = input("\nEscolha uma opção: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            list_tasks()
        elif choice == "4":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()

# Salvando a lista de tarefas em um arquivo JSON





with open ("todo_list.json", "w") as arquivo:
    
    json.dump(todo_list, arquivo, indent=4)	
