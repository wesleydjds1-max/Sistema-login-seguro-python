import hashlib
from storage import carregar_usuarios, salvar_usuarios

MAX_TENTATIVAS = 3

def gerar_hash_senha(senha: str) -> str:
    """
    Gera o hash SHA-256 de uma senha.
    """
    return hashlib.sha256(senha.encode("utf-8")).hexdigest()


def cadastrar_usuario(usuario: str, senha: str) -> bool:
    """
    Cadastra um novo usuário.
    Retorna True se cadastrou com sucesso, False se o usuário já existe.
    """
    usuarios = carregar_usuarios()

    if usuario in usuarios:
        return False  # Usuário já existe

    hash_senha = gerar_hash_senha(senha)

    usuarios[usuario] = {
        "senha": hash_senha,
        "tentativas": 0,
        "bloqueado": False
    }

    salvar_usuarios(usuarios)
    return True


def autenticar_usuario(usuario: str, senha: str) -> bool:
    """
    Autentica um usuário.
    Retorna True se login for bem-sucedido, False caso contrário.
    """
    usuarios = carregar_usuarios()

    if usuario not in usuarios:
        print("❌ Usuário não encontrado.")
        return False

    dados_usuario = usuarios[usuario]

    if dados_usuario["bloqueado"]:
        print("⛔ Usuário bloqueado por excesso de tentativas.")
        return False

    hash_senha_digitada = gerar_hash_senha(senha)

    if hash_senha_digitada == dados_usuario["senha"]:
        # Login correto → zera tentativas
        dados_usuario["tentativas"] = 0
        salvar_usuarios(usuarios)
        return True
    else:
        # Senha errada
        dados_usuario["tentativas"] += 1

        if dados_usuario["tentativas"] >= MAX_TENTATIVAS:
            dados_usuario["bloqueado"] = True
            print("⛔ Usuário bloqueado após muitas tentativas incorretas.")
        else:
            tentativas_restantes = MAX_TENTATIVAS - dados_usuario["tentativas"]
            print(f"❌ Senha incorreta. Tentativas restantes: {tentativas_restantes}")

        salvar_usuarios(usuarios)
        return False

