tarefas = []

def mostrar_menu():
    #Exibe o menu de opções para o usuário.
    print("Menu de tarefas:")
    print("1. Adicionar tarefa")
    print("2. Visualizar tarefas")
    print("3. Concluir tarefa/ Remover tarefa")
    print("4. Sair")
    return input("Escolha uma tarefa(1-4):")

def adicionar_tarefa():
    #Solicita e adiciona uma nova tarefa à lista.
    tarefa = input("Digite a a tarefa que você deseja adicionar:")
    tarefas.append(tarefa)
    print(f'✅Tarefa "{tarefa}"adicionada com sucesso')

def visualizar_tarefas():
    #Exibe todas as tarefas atuais com seus respectivos índices
    if not tarefas:
        print("Nenhuma tarefa pendente")
        return
    print("\n SUAS TAREFAS:")
    # Usamos enumerate para obter o índice (i) e a tarefa (t) ao mesmo tempo.
    for i, t in enumerate(tarefas):
    # O índice é somado a 1 para ser mais amigável ao usuário (começar em 1).
        print(f'{i + 1}. {t}')
    print("-------------------")

def concluir_tarefas():
    #Remove uma tarefa da lista pelo índice fornecido pelo usuário.
    visualizar_tarefas()# Primeiro mostra a lista para o usuário ver os números
    if not tarefas:
        return# Sai da função se a lista estiver vazia
    try:
        # Pede o número da tarefa
        num_tarefa = int(input("Digite a tarefa que deseja concluir/remover:"))
        # Converte o número amigável (começa em 1) para o índice da lista (começa em 0)
        indice_remover = num_tarefa - 1
        # Verifica se o índice é válido
        if 0 <= indice_remover < len(tarefas):
            # Remove a tarefa e armazena o nome removido
            tarefa_removida = tarefas.pop(indice_remover)
            print(f'🗑️ Tarefa "{tarefa_removida}"concluída e removida com sucesso')
        else:
            print("❌ Número de tarefa inválido.")
    except ValueError:
        # Captura o erro se o usuário digitar algo que não seja um número
        print("❌ Insira um número válido.")
# Função principal

def main():
    #Ponto de entrada do programa, responsável pelo loop principal.
    # O loop 'while True' mantém o programa rodando até o usuário escolher Sair (opção 4)
    while True:
        escolha = mostrar_menu()
        if escolha == '1':
            adicionar_tarefa()
        elif escolha == '2':    
            visualizar_tarefas()
        elif escolha == '3':
            concluir_tarefas()
        elif escolha == '4':       
            print("Saindo do programa!")
            break# Sai do loop while True
        else:
            print(" Opção inválida... Tente novamente.")
# Garante que a função 'main' seja executada quando o script for iniciado
if __name__ == "__main__":
    main()