<div align="center">
  
# 🌆 DARK API

<img width="400" height="350" alt="imagem" src="https://github.com/user-attachments/assets/78a9bafd-bdb6-4a9b-8092-0bb75e48e8a5" />

--- 

`DARK API` é uma API de gerenciamento de usuários robusta, performática e desenhada com foco em segurança defensiva. Desenvolvida em Python com **FastAPI** e **SQLModel**, a aplicação implementa mitigações severas contra vulnerabilidades web comuns, além de controle estrito de fluxo de requisições.

---

## 🛠️ Tecnologias & Ferramentas

* **FastAPI:** Framework moderno e assíncrono de alta performance.
* **SQLModel:** ORM que combina o poder do SQLAlchemy com a validação do Pydantic.
* **MySQL:** Banco de dados relacional para persistência segura dos dados.
* **Redis:** Armazenamento em cache e em memória utilizado para a camada de Rate Limiting.
* **Docker & Docker Compose:** Containerização completa do ambiente para deploy rápido e isolado.

---

## 🔒 Funcionalidades de Segurança

* **Anti SQL Injection:** Camada de persistência puramente estruturada via **SQLModel / SQLAlchemy**, utilizando *Prepared Statements* (declarações preparadas) e parametrização nativa, impedindo a execução de queries maliciosas via inputs.
* **Rate Limiting (Anti-Spam):** Proteção baseada em Redis nas rotas críticas (como criação de usuários e autenticação), mitigando ataques de força bruta (*Brute Force*) e denial-of-service (*DoS*).
* **Autenticação JWT (JSON Web Tokens):** Controle de acesso seguro, stateless e com tempo de expiração rigoroso para proteção dos endpoints restritos.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
* Docker instalado
* Docker Compose instalado

---

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/dark-api.git](https://github.com/seu-usuario/dark-api.git)
   cd dark-api

    Configure as Variáveis de Ambiente:
    Crie um arquivo .env na raiz do projeto com base no modelo abaixo (nunca suba suas credenciais reais para o GitHub):
    Snippet de código

    DATABASE_URL=mysql+aiomysql://user:password@db:3306/dark_db
    REDIS_URL=redis://redis:6379/0
    JWT_SECRET_KEY=sua_chave_secreta_super_segura_aqui
    JWT_ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30

    Suba os Containers:
    Bash

    docker compose up -d --build

A API estará disponível em: http://localhost:8000

# A documentação interativa (Swagger UI) pode ser acessada em: http://localhost:8000/docs

---

### 💡 Dicas de Implementação do Protocolo de Segurança
Como você está usando **SQLModel**, lembre-se de seguir estas boas práticas no código:
1. **Evite strings puras nas queries:** Nunca faça algo como `session.exec(f"SELECT * FROM user WHERE name = '{input}'")`. Sempre use o construtor do SQLModel: `select(User).where(User.name == input)`. O próprio ORM cuida de sanitizar os dados.
2. **Redis para Rate Limit:** Você pode usar a biblioteca `slowapi` (baseada em Limits) ou criar um decorator personalizado usando `aioredis` para incrementar chaves baseadas no IP do cliente no Redis.
</div>
