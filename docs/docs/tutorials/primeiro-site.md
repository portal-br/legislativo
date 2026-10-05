---
myst:
  html_meta:
    "description": "Do clone ao site no ar: instalar o Portal Modelo para desenvolvimento"
    "property=og:description": "Do clone ao site no ar: instalar o Portal Modelo para desenvolvimento"
    "property=og:title": "Do clone ao site no ar"
    "keywords": "Plone, PortalBrasil: Legislativo, instalação, desenvolvimento"
---

# Do clone ao site no ar

Neste tutorial você vai instalar o Portal Modelo no seu computador, criar um site com o conteúdo de exemplo e abri-lo no navegador.

## Pré-requisitos

- [uv](https://docs.astral.sh/uv/), que instala o Python 3.14 usado pelo backend.
- Node.js 24 e pnpm 10, para o frontend.
- Git e GNU Make.

## Clone o repositório

```shell
git clone https://github.com/portal-br/legislativo.git
cd legislativo
```

## Instale o backend e o frontend

```shell
make install
```

O comando cria o ambiente Python do backend com o `uv`, instala as dependências do frontend com o `pnpm` e cria um site Plone com o conteúdo de exemplo.

## Crie o site

Se você precisar recriar o site depois, use:

```shell
make backend-create-site
```

O site é criado com o identificador `Plone` e o título "Câmara Modelo", em português do Brasil, com o fuso horário `America/Sao_Paulo`.
Para escolher outros valores, veja {doc}`/how-to-guides/criar-site`.

## Inicie o backend

```shell
make backend-start
```

O backend responde em `http://localhost:8080`.
O usuário administrador é `admin`, com a senha `admin`.

## Inicie o frontend

Em outro terminal, na pasta do repositório:

```shell
make frontend-start
```

Abra `http://localhost:3000` no navegador.
A página inicial mostra o site "Câmara Modelo" com o conteúdo de exemplo.

## Próximos passos

- {doc}`/how-to-guides/demo-docker-compose`, para experimentar o Portal Modelo sem instalar Python e Node.js.
- {doc}`/reference/tipos-de-conteudo`, para conhecer os tipos de conteúdo disponíveis.
