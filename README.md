---

# 🔐 Sistema de Login Seguro em Python

## 📌 Descrição

Este projeto é um **Sistema de Login Seguro** desenvolvido em Python com foco em **boas práticas de segurança**, organização de código e estruturação de projeto.
O sistema permite **cadastrar usuários**, **autenticar login**, **armazenar senhas com hash**, **controlar tentativas de acesso** e **bloquear usuários após múltiplas falhas**.

O objetivo é demonstrar conhecimentos em **programação**, **segurança da informação** e **arquitetura de software**, sendo ideal para **portfólio acadêmico e processos seletivos de estágio**.

---

## 🚀 Funcionalidades

* ✅ Cadastro de usuários
* 🔐 Armazenamento de senha com hash (SHA-256)
* 🔑 Login seguro
* 🚫 Bloqueio de usuário após 3 tentativas inválidas
* 💾 Persistência de dados em arquivo JSON
* 🧱 Estrutura de projeto modular (main, auth, storage)

---

## 🗂️ Estrutura do Projeto

```
sistema-login-seguro-python/
 ├── main.py
 ├── auth.py
 ├── storage.py
 ├── usuarios.json
 └── README.md
```

---

## ⚙️ Tecnologias Utilizadas

* Python 3
* Biblioteca padrão (`hashlib`, `json`, `os`)

---

## ▶️ Como Executar o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/sistema-login-seguro-python.git
```

2. Entre na pasta do projeto:

```bash
cd sistema-login-seguro-python
```

3. Execute o programa:

```bash
python main.py
```

---

## 🧪 Como Testar

* Cadastre um novo usuário
* Tente errar a senha 3 vezes
* Observe o bloqueio automático
* Tente logar novamente após o bloqueio

---

## 🧠 Conceitos Aplicados

* Hash de senha
* Autenticação segura
* Separação de responsabilidades
* Persistência de dados
* Tratamento básico de erros
* Organização de código em módulos

---

## 🔒 Possíveis Melhorias Futuras

* 🔐 Salting de senha
* 🗄️ Uso de banco de dados (SQLite)
* 🖥️ Interface gráfica
* 👮 Sistema de desbloqueio por administrador
* 📜 Log de tentativas de login

---

## 👨‍💻 Autor

**Wesley de Jesus dos Santos**

Estudante de Ciências da Computação

📍 Rio de Janeiro – RJ

📧 [wesleydjds@outlook.com.br](mailto:wesleydjds@outlook.com.br)

---

## ⭐ Observação

Este projeto foi desenvolvido com fins **educacionais e de portfólio**.


