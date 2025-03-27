# Armazenamento em memória para usuários
users = []

def register_user():
    
    """ Solicita ao usuário o nome, email e idade, e então adiciona o usuário à lista de usuários."""
    name = input("Qual é o seu nome? ").strip
    age = input("Qual é a sua idade? ").strip
    email = input("Qual é o seu e-mail? ").strip
    users.append({"nome": name, "email": email, "idade": age})
    print("Usuário registrado!")
    input("\nPressione Enter para voltar ao menu")

def list_users():
    """Lista todos os usuários armazenados na memória, imprimindo suas informações no console."""
    
    if not users:
            print("\nAinda não existem usuários registrados")
    else:
        print("Usuários cadastrados")
        for user in users:
            print(user)
            input("\n Pressione Enter para voltar ao menu")

def search_user():
    """Solicita ao usuário que insira um nome e busca por um usuário correspondente na lista.
    Se encontrado, exibe as informações do usuário."""
   
    nome_busca = input("Qual é o nome do usuário? ").strip
    for user in users:
        if user["nome"] == nome_busca:
            print(user)
        else:
            print("Usuário não encontrado.")

def display_menu():
    """
    Exibe as opções disponíveis para o usuário.
    """
    print("\n--- Menu de Gerenciamento de Usuários ---")
    print("1. Registrar novo usuário")
    print("2. Listar todos os usuários")
    print("3. Buscar usuário por nome")
    print("4. Sair do programa") 
    

def main():
    """
    Função principal que executa o loop da aplicação.
    """
    while True:
        display_menu()
        choice = input("Escolha uma opção (1-4): ")

        if choice == '1':
            register_user()
        elif choice == '2':
            list_users()
        elif choice == '3':
            search_user()
        elif choice == '4':
            print("Saindo do programa. Obrigado!")
        else:
            print("Opção inválida. Por favor, escolha entre 1 e 4.")
            break

if __name__ == "__main__":
    main()
    """A fazer:
    - Criar função para remover usuário, limpar código e verificar se está condizente
    """