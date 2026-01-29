from auth import cadastrar_usuario, autenticar_usuario

def mostrar_menu():
    print("\n==============================")
    print("   🔐 Sistema de Login Seguro")
    print("==============================")
    print("1 - Cadastrar usuário")
    print("2 - Fazer login")
    print("3 - Sair")
    print("==============================")

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("\n=== Cadastro de Usuário ===")
            usuario = input("Digite o nome de usuário: ").strip()

