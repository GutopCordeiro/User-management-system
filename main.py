# Armazenamento em memória para usuários
users = []

def register_user():
    """ Solicita ao usuário o nome, email e idade, e então adiciona o usuário à lista de usuários."""
    while True:
        name = input ("Qual seu nome? ").lower()
        if name.isalpha():
            name =str(name).lower()
            break
        else:
            print("Por favor digite apenas letras")
    while True:
        age = input ("Qual a sua idade? ")
        if age.isdigit():
            age =int(age)
            break
        else:
            print("Por favor digite apenas números")
    email = input("Qual é o seu e-mail? ")
    users.append({"nome": name, "email": email, "idade": age})
    print("\nUsuário registrado!")
    input("\nPressione Enter para voltar ao menu")

def list_users():
    """Lista todos os usuários armazenados na memória, imprimindo suas informações no console."""
    
    if not users:
            print("\nAinda não existem usuários registrados")
            input("\n Pressione Enter para voltar ao menu")
    else:
        print("Usuários cadastrados: ")
        for user in users:
            print(f"Usuários:{user}")
        input("\nPressione Enter para voltar ao menu")

def search_user():
    """Solicita ao usuário que insira um nome e busca por um usuário correspondente na lista.
    Se encontrado, exibe as informações do usuário."""
   
    nome_busca = input("Qual é o nome do usuário? ").lower()
    found = False
    for user in users:
        if user["nome"] == nome_busca:
            print(user)
            found = True
            input("\nPressione Enter para voltar ao menu")
            break
    if not found:
        print("Usuário não encontrado.")


def remove_user():
    """Pergunta ao usuário qual usário qual usuário ele deseja excluir. Caso encontrado, remove as informações do usuário do sistema """
    
    user_remove = input("Qual o nome do usuário que deseja excluir? ").lower()
    found = False  

    for user in users:
        if user["nome"] == user_remove:
            users.remove(user)  
            print("Usuário removido com sucesso!")
            input("\nPressione Enter para voltar ao menu")
            found = True  
            break  

    if not found:  
        print("Usuário não encontrado!")            

def edit_user():
    """Permite que o usuário edite suas informações."""
    user_name = input("Qual usuário o nome do usuário que você gostaria de editar? ")
    found = False
    for user in users:
        if user["nome"] == user_name.lower():
            found = True
            print(f"Usuário encontrado: {user_name}")
            while True:
                print("1- Editar nome")
                print("2- Editar idade")
                print("3- Editar email")
                print("4- Voltar para o menu")
                choose = input("Escolha um número 1-4: ")
                if choose == '1':
                    while True:
                        new_name = input("Qual o novo nome? ")
                        if new_name.isalpha():
                            user["nome"] = new_name.lower()
                            print("Nome atualizado com sucesso!")
                            break
                        else:
                            print("Por favor digite apenas letras")
                elif choose == '2':
                    while True:
                        new_age = input("Qual a nova idade? ")
                        if new_age.isdigit():
                            user["idade"] = int(new_age)
                            print("Idade atualizada com sucesso!")
                            break
                        else: 
                            print("Por favor digite apenas números")
                elif choose == '3':
                    new_email = input("Qual o novo email? ")
                    user["email"] = new_email.lower()
                    print ("Email atualizado com sucesso!")
                elif choose == '4':
                    print("Edição cancelada")
                    break
                else:
                    print("insira uma opção valida (1-4)")
            break
    if not found:
        print("usuário não encontrado :(")
        input("\n Pressione enter para voltar ao menu")

def display_menu():
    """
    Exibe as opções disponíveis para o usuário.
    """
    print("\n--- Menu de Gerenciamento de Usuários ---")
    print("1. Registrar novo usuário")
    print("2. Listar todos os usuários")
    print("3. Buscar usuário por nome")
    print("4. Deletar usuário") 
    print("5. Editar dados do usuário")
    print("6. Sair do programa")
    

def main():
    """
    Função principal que executa o loop da aplicação.
    """
    while True:
        display_menu()
        choice = input("Escolha uma opção (1-6): ")

        if choice == '1':
            register_user()
        elif choice == '2':
            list_users()
        elif choice == '3':
            search_user()
        elif choice == '4':
            remove_user()  
        elif choice == '5':
            edit_user()
        elif choice == '6':
            print("Saindo do programa, obrigado :)")  
            break
        else:
            print("Opção inválida. Por favor, escolha entre 1 e 5.")
            
main()
