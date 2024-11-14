# Dock Digital Account API

## Descrição

Este projeto, que visa resolver esse [desafio](https://github.com/cdt-baas/desafio-dev-api-rest), implementa uma API para gerenciar contas digitais para clientes da Dock. Com essa API, é possível criar e remover portadores de contas, bem como realizar operações bancárias comuns, como depósitos e saques. 

## Tecnologias

- FastAPI
- Mysql
- Docker-compose

## Como rodar

Para rodar o projeto, é necessário ter o Docker e o Docker-compose instalados.

1. Clone o repositório;
2. Entre na pasta do projeto;
3. Entre na pasta docker;
4. Rode o comando `docker-compose --env-file ../.config/.env up`;
5. Acesse a documentação da API em `http://localhost:8080/docs`.


## Observações

O arquivo `.config/.env` contém as variáveis de ambiente necessárias para rodar o projeto. Essa solução foi adotada para facilitar a configuração do projeto, já que não é um ambiente produtivo. Em um ambiente produtivo, essas variáveis de ambiente devem ser configuradas de forma mais segura.

