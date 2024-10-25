# DropFy - Backend

Este repositório contém o código-fonte do backend da aplicação DropFy, desenvolvido com FastAPI. O backend fornece uma API REST para gerenciar produtos de uma loja de dropshipping, incluindo funcionalidades para:

* Cadastrar produtos com informações básicas.
* Gerar copys e descrições de produtos automaticamente usando a API do Gemini.
* Calcular preços de venda e margem de lucro com base em regras configuráveis.
* Integrar com a API da Shopify para gerenciar produtos na loja. (em desenvolvimento)

## Tecnologias utilizadas

* FastAPI
* Pydantic
* Google Generative AI
* SQLAlchemy (opcional, caso use um banco de dados)
* Docker

## Como executar

### Usando Docker

1. Construa a imagem Docker: `docker build -t nome-da-imagem .`
2. Execute o container: `docker run -p 8000:8000 nome-da-imagem`

### Executando localmente (sem Docker)

1. Clone o repositório: `git clone <URL_do_repositorio>`
2. Crie um ambiente virtual: `python -m venv .venv`
3. Ative o ambiente virtual: `source .venv/bin/activate`
4. Instale as dependências: `pip install -r requirements.txt`   

5. Configure as variáveis de ambiente (API Key do Gemini, etc.).
6. Execute a aplicação: `uvicorn main:app --reload`

## Documentação da API

A documentação da API está disponível em `/docs` após executar a aplicação.

## Dockerfile

```dockerfile
FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]   
