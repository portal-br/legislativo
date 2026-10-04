# Portal Modelo 🚀
## PortalBrasil: Legislativo

[![Testes](https://github.com/portal-br/legislativo/actions/workflows/main.yml/badge.svg)](https://github.com/portal-br/legislativo/actions/workflows/main.yml)

Ferramenta de portais para casas do legislativo brasileiro, construída com Plone 6 e Volto.

A documentação está em [portal-br.github.io/legislativo](https://portal-br.github.io/legislativo/) e o Storybook dos componentes do frontend, em [portal-br.github.io/legislativo/storybook](https://portal-br.github.io/legislativo/storybook/). Os fontes da documentação ficam na pasta `docs`.

## Início Rápido 🏁

Se você deseja testar o Portal Modelo, a forma mais rápida é utilizando um dos arquivos [disponíveis em nosso repositório](https://github.com/portal-br/legislativo/) para iniciar uma stack com Docker Compose.

Para isso, é necessário ter uma versão recente do Docker instalada 🐳.

Caso esteja utilizando Windows com WSL, será necessário editar o arquivo `C:\Windows\System32\Drivers\etc\hosts` e adicionar, ao final do arquivo, uma entrada para o endereço desejado:

```
127.0.0.1  portal-modelo.localhost
```

### Demo do Portal Modelo

- Em seu computador, crie uma pasta chamada `PortalModelo`.
- Salve o arquivo [docker-compose-demo.yml](https://raw.githubusercontent.com/portal-br/legislativo/refs/heads/main/docker-compose-demo.yml) com o nome `docker-compose.yml` dentro da pasta criada.
- Inicie a stack com o comando `docker compose up`. Após o download das imagens do backend e frontend, acesse o endereço [http://portal-modelo.localhost](http://portal-modelo.localhost) no seu navegador.
- Caso deseje servir essa stack em outro endereço, por exemplo **novo.camara.sp.leg.br**, utilize a variável `STACK_HOSTNAME` como no exemplo:
  `STACK_HOSTNAME=novo.camara.sp.leg.br docker compose up`

⚠️ Importante: este ambiente não deve ser utilizado em produção, pois os dados **não são persistidos**.

### Portal Modelo com dados persistentes

- Em seu computador, crie uma pasta chamada `PortalModelo`.
- Salve o arquivo [docker-compose.yml](https://raw.githubusercontent.com/portal-br/legislativo/refs/heads/main/docker-compose.yml) com o nome `docker-compose.yml` dentro da pasta criada.
- Inicie a stack com o comando `docker compose up -d`.
- Na primeira execução, crie o site com o comando `docker compose run --rm backend create-site`.
- Acesse o endereço [http://portal-modelo.localhost](http://portal-modelo.localhost) no seu navegador.
- Caso deseje servir essa stack em outro endereço, por exemplo **novo.camara.sp.leg.br**, utilize a variável `STACK_HOSTNAME` como no exemplo:
  `STACK_HOSTNAME=novo.camara.sp.leg.br docker compose up -d`

Os dados desta stack serão persistidos no volume Docker chamado `portal-modelo_vol-site-data`.

## Desenvolvimento do Portal Modelo

### Pré-requisitos ✅

Certifique-se de ter os seguintes softwares instalados:

- [uv](https://docs.astral.sh/uv/) 🐍, que instala o Python 3.14
- Node 24 🟩 e pnpm 10 🧶
- Docker 🐳, para as imagens e a stack local

### Instalação 🔧

1. Clone o repositório:

```shell
git clone git@github.com:portal-br/legislativo.git
cd legislativo
```

2. Instale o Backend e o Frontend. O comando também cria um site Plone com o conteúdo de exemplo:

```shell
make install
```

### Suba os Servidores 🔥

1. Inicie o Backend em [http://localhost:8080/](http://localhost:8080/):

```shell
make backend-start
```

2. Em outro terminal, inicie o Frontend em [http://localhost:3000/](http://localhost:3000/):

```shell
make frontend-start
```

Voilà! Seu Portal Modelo deve estar no ar e funcionando! 🎉

Para recriar o site, use `DELETE_EXISTING=1 make backend-create-site`.

### Implantação Local com Docker 📦

Implemente um ambiente local com `Docker Compose` que inclui:

- Imagens Docker para Backend e Frontend, geradas a partir do código local 🖼️
- Uma stack com Traefik como roteador e banco de dados Postgres 🗃️
- Acessível em [http://legislativo.localhost](http://legislativo.localhost) 🌐

Execute o seguinte:

```shell
make stack-create-site
make stack-start
```

E pronto! Seu site Plone está rodando localmente! 🚀

Para parar a stack, use `make stack-stop`; para removê-la junto com os dados, `make stack-rm`.

## Estrutura do Projeto 🏗️

Este monorepositório é composto por três seções: `backend`, `frontend` e `docs`.

- **backend**: Contém a API e a instalação do Plone, gerenciada com `uv`, e o pacote `portalbrasil.legislativo`, com a distribuição `portalmodelo`.
- **frontend**: Contém o add-on do Volto `@portalbrasil/legislativo`, escrito em TypeScript.
- **docs**: Contém a documentação do projeto, em português do Brasil.

### Por que essa estrutura? 🤔

- Todo o código necessário para executar o site está contido no repositório (excluindo os addons existentes para Plone e React).
- Workflows específicos do GitHub são disparados com base nas alterações em cada base de código (consulte `.github/workflows`).
- Facilita a criação de imagens Docker para cada base de código.

## Garantia de Qualidade de Código 🧐

Para formatar automaticamente seu código e garantir aderência aos padrões de qualidade, execute:

```shell
make check
```

Também é possível executar apenas o `format`:

```shell
make format
```

ou o `lint`, que inclui a checagem de tipos com mypy no backend e TypeScript no frontend:

```shell
make lint
```

Para rodar os testes do backend e do frontend:

```shell
make test
```

Os linters e os testes podem ser executados individualmente nas pastas `backend` ou `frontend`.

## Internacionalização 🌐

Gere arquivos de tradução para Plone e Volto com facilidade:

```shell
make i18n
```

## Créditos e Agradecimentos 🙏

Gerado utilizando [Cookieplone (2.0.0)](https://github.com/plone/cookieplone) e [cookieplone-templates (99c2201)](https://github.com/plone/cookieplone-templates/commit/99c2201962371b182499a0d71f45ed878da0c33d) em 2026-10-04. Um agradecimento especial a todos os colaboradores e apoiadores!
