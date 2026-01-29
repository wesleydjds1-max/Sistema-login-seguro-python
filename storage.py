import json
import os

ARQUIVO_USUARIOS = "usuarios.json"


def carregar_usuarios() -> dict:
    """
    Carrega os usuários do arquivo JSON.
    Se o arquivo não existir ou estiver vazio/corrompido, retorna um dicionário vazio.
    """
    if not os.path.exists(ARQUIVO_USUARIOS):
        # Se o arquivo não existe, cria um vazio
        with open(ARQUIVO_USUARIOS, "w", encoding="utf-8") as f:
            json.dump({}, f, indent=4)
        return {}

    try:
        with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as f:
            conteudo = f.read().strip()
            if not conteudo:
                return {}
            return json.loads(conteudo)
    except (json.JSONDecodeError, IOError):
        # Se o arquivo estiver corrompido ou ilegível
        print("⚠️ Aviso: arquivo de usuários corrompido. Criando um novo.")
        return {}


def salvar_usuarios(usuarios: dict) -> None:
    """
    Salva o dicionário de usuários no arquivo JSON.
    """
    with open(ARQUIVO_USUARIOS, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)


