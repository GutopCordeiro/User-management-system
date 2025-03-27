# automind-technical-test
Descrição

Este projeto é um sistema simples de gerenciamento de usuários em Python, que permite registrar, listar, buscar e remover usuários diretamente da memória (sem banco de dados).

Funcionalidades

Registrar novo usuário: O usuário insere nome, e-mail e idade. O sistema valida se a idade é um número.

Listar todos os usuários: Exibe todos os usuários registrados.

Buscar usuário por nome: Permite procurar um usuário pelo nome.

Remover usuário: Exclui um usuário do sistema.

Sair do programa: Encerra a execução.

Como Executar

Certifique-se de ter o Python instalado (versão 3.x recomendada).

Salve o código em um arquivo usuarios.py.

No terminal, execute:

python usuarios.py

Siga as instruções no menu interativo.

Estrutura do Código

register_user(): Registra um novo usuário e adiciona à lista users.

list_users(): Exibe todos os usuários cadastrados.

search_user(): Permite buscar um usuário pelo nome.

remove_user(): Exclui um usuário, se encontrado.

display_menu(): Exibe o menu de opções.

main(): Controla o fluxo do programa.

Melhorias Futuras

Implementação de persistência de dados (ex.: uso de arquivos JSON ou banco de dados).

Melhor tratamento de erros e validações.

Interface gráfica para facilitar o uso.

Autor

Projeto criado para fins de aprendizado e prática de manipulação de dados em Python.