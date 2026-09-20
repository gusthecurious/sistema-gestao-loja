# 🍪 Sistema de Gestão para Loja

Sistema de gestão desenvolvido para uma loja, com foco em controle de produtos, estoque, vendas e, futuramente, gestão financeira.

O projeto está sendo desenvolvido como um MVP e também como projeto de estudo para praticar desenvolvimento de APIs, banco de dados e arquitetura de aplicações.

## 🚀 Tecnologias

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Uvicorn

## 📋 Funcionalidades

### Produtos

* [x] Criar produto
* [x] Listar produtos
* [x] Buscar produto
* [x] Atualizar produto
* [x] Excluir produto

### Estoque

* [x] Controle de quantidade
* [x] Entrada de estoque
* [x] Saída de estoque
* [x] Histórico de movimentações
* [x] Registro de data e hora
* [x] Validação de estoque insuficiente

### Vendas

* [x] Criar venda
* [x] Adicionar múltiplos produtos à venda
* [x] Calcular subtotal dos itens
* [x] Calcular valor total da venda
* [x] Atualizar estoque automaticamente após a venda
* [x] Registrar saída de estoque relacionada à venda

### Financeiro

* [ ] Registro de receitas
* [ ] Registro de despesas
* [ ] Controle de custos
* [ ] Relatórios financeiros

### Clientes

* [ ] Cadastro de clientes
* [ ] Histórico de compras

### Dashboard

* [ ] Resumo de vendas
* [ ] Produtos em estoque
* [ ] Indicadores financeiros

### Autenticação

* [ ] Cadastro de usuários
* [ ] Login
* [ ] Controle de permissões

## 🗂️ Estrutura do projeto

```text
sistema_loja/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── produto.py
│   │   ├── movimentacao.py
│   │   ├── venda.py
│   │   └── item_venda.py
│   │
│   └── schemas/
│       ├── __init__.py
│       ├── produto.py
│       ├── movimentacao.py
│       └── venda.py
│
├── .gitignore
└── README.md
```

## ⚙️ Como executar

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Entrar na pasta

```bash
cd sistema_loja
```

### 3. Criar o ambiente virtual

```bash
python -m venv .venv
```

### 4. Ativar o ambiente virtual

Windows:

```bash
.venv\Scripts\activate
```

### 5. Instalar as dependências

```bash
pip install "fastapi[standard]" sqlalchemy
```

### 6. Executar a aplicação

```bash
python -m uvicorn app.main:app --reload
```

A API estará disponível em:

```text
http://127.0.0.1:8000
```

A documentação interativa do FastAPI pode ser acessada em:

```text
http://127.0.0.1:8000/docs
```

## 📌 Status do projeto

🚧 Em desenvolvimento

O projeto está sendo construído de forma incremental. Novas funcionalidades serão adicionadas conforme o desenvolvimento do MVP avança.

## 🎯 Objetivo

O objetivo deste projeto é desenvolver uma aplicação de gestão para uma loja.

Além de resolver necessidades reais da operação, o projeto está sendo utilizado para aprofundar conhecimentos em:

* Desenvolvimento de APIs REST
* Python
* FastAPI
* SQLAlchemy
* Bancos de dados relacionais
* Modelagem de dados
* Controle de estoque
* Regras de negócio
* Boas práticas de desenvolvimento

## 📚 Próximos passos

* [ ] Melhorar o módulo de vendas
* [ ] Criar módulo financeiro
* [ ] Criar cadastro de clientes
* [ ] Criar dashboard
* [ ] Adicionar autenticação e permissões
* [ ] Melhorar tratamento de erros
* [ ] Adicionar testes automatizados
* [ ] Avaliar migração para PostgreSQL
* [ ] Preparar arquitetura para possível versão SaaS
