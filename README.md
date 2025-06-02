# Portal Modelo 🚀
## PortalBrasil: Legislativo

[![Testes](https://github.com/portal-br/legislativo/actions/workflows/main.yml/badge.svg)](https://github.com/portal-br/legislativo/actions/workflows/main.yml)

Ferramenta de portais para casas do legislativo brasileiro

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
- Inicie a stack com o comando `docker compose up`. Após o download das imagens do backend e frontend, acesse o endereço [http://portal-modelo.localhost](http://portal-modelo.localhost) no seu navegador.
- Caso deseje servir essa stack em outro endereço, por exemplo **novo.camara.sp.leg.br**, utilize a variável `STACK_HOSTNAME` como no exemplo:
  `STACK_HOSTNAME=novo.camara.sp.leg.br docker compose up`

Os dados desta stack serão persistidos no volume Docker chamado `portal-modelo_vol-site-data`.
## Desenvolvimento do Portal Modelo

### Pré-requisitos ✅

Certifique-se de ter os seguintes softwares instalados:

- UV 🐍
- Node 22 🟩 e pnpm 🧶
- Docker 🐳

### Instalação 🔧

1. Clone o repositório:

```shell
git clone git@github.com:portal-br/legislativo.git
cd legislativo
```

2. Instale o Backend e o Frontend:

```shell
make install
```

### Suba os Servidores 🔥

1. Crie um novo site Plone na primeira execução:

```shell
make backend-create-site
```

2. Inicie o Backend em [http://localhost:8080/](http://localhost:8080/):

```shell
make backend-start
```

3. Em outro terminal, inicie o Frontend em [http://localhost:3000/](http://localhost:3000/):

```shell
make frontend-start
```

Voilà! Seu Portal Modelo deve estar no ar e funcionando! 🎉

### Implantação Local com Docker 📦

Implemente um ambiente local com `Docker Compose` que inclui:

- Imagens Docker para Backend e Frontend 🖼️
- Uma stack com Traefik como roteador e banco de dados Postgres 🗃️
- Acessível em [http://portal-modelo.localhost](http://portal-modelo.localhost) 🌐 ou em qualquer outro endereço definido pela variável de ambiente `STACK_HOSTNAME`.

Execute o seguinte:

```shell
make stack-start
make stack-create-site
```

E pronto! Seu site Plone está rodando localmente! 🚀

## Estrutura do Projeto 🏗️

Este monorepositório é composto por três seções distintas: `backend`, `frontend` e `devops`.

- **backend**: Contém a API e a instalação do Plone, utilizando pip em vez de buildout, e inclui um pacote de política chamado `portalbrasil.legislativo`.
- **frontend**: Contém o pacote React (Volto) chamado `@portalbrasil/legislativo`.

### Por que essa estrutura? 🤔

- Todo o código necessário para executar o site está contido no repositório (excluindo os addons existentes para Plone e React).
- Workflows específicos do GitHub são disparados com base nas alterações em cada base de código (consulte `.github/workflows`).
- Facilita a criação de imagens Docker para cada base de código.
- Demonstra a instalação/configuração do Plone sem utilizar buildout.

## Garantia de Qualidade de Código 🧐

Para formatar automaticamente seu código e garantir aderência aos padrões de qualidade, execute:

```shell
make check
```

Também é possível executar apenas o `format`:

```shell
make format
```

ou o `lint`:

```shell
make lint
```

Os linters podem ser executados individualmente nas pastas `backend` ou `frontend`.

## Internacionalização 🌐

Gere arquivos de tradução para Plone e Volto com facilidade:

```shell
make i18n
```

## Créditos e Agradecimentos 🙏

Gerado utilizando [Cookieplone (0.8.4)](https://github.com/plone/cookieplone) e [cookieplone-templates (86480b4)](https://github.com/plone/cookieplone-templates/commit/86480b44baa3953c98534071089ac3c6b656f3f5) em 2025-03-14 15:47:43.801432. Um agradecimento especial a todos os colaboradores e apoiadores!
