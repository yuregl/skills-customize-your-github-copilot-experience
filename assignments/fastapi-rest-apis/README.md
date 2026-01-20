# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objective

Você aprenderá a construir uma API REST completa usando o framework FastAPI. Ao final desta tarefa, você será capaz de criar endpoints, gerenciar requisições HTTP, validar dados e estruturar um projeto profissional de API em Python.

## 📝 Tasks

### 🛠️ Criar uma API REST com Operações CRUD

#### Description
Construa uma API REST que implemente operações CRUD (Create, Read, Update, Delete) para gerenciar uma coleção de recursos. Utilize o FastAPI para criar endpoints que respondam a diferentes métodos HTTP e retornem dados em formato JSON.

#### Requirements
Completed program should:

- Implementar pelo menos 5 endpoints (GET, POST, PUT, DELETE)
- Usar modelos Pydantic para validação de dados de entrada e saída
- Incluir tratamento de erros com códigos HTTP apropriados (200, 201, 400, 404)
- Documentação automática Swagger acessível em `/docs`


### 🛠️ Implementar Validação e Filtros Avançados

#### Description
Adicione validação robusta de dados, tratamento de exceções personalizadas e funcionalidades de filtro/busca em seus endpoints. Implemente lógica para validar entrada do usuário e retornar mensagens de erro descritivas.

#### Requirements
Completed program should:

- Validar tipos de dados, tamanhos e formatos usando Pydantic validators
- Implementar filtros de busca em endpoints GET
- Criar exceções personalizadas com mensagens claras
- Retornar respostas estruturadas com mensagens de erro informaticas


### 🛠️ Estruturar e Testar a API

#### Description
Organize o código da API em uma estrutura profissional com separação de responsabilidades. Implemente testes unitários para validar o comportamento dos endpoints.

#### Requirements
Completed program should:

- Separar o código em múltiplos arquivos (models, routes, main)
- Implementar pelo menos 5 testes unitários usando pytest
- Usar fixtures do pytest para dados de teste
- Todos os testes devem passar sem erros
