---
myst:
  html_meta:
    "description": "Como subir a demonstração do Portal Modelo com Docker Compose"
    "property=og:description": "Como subir a demonstração do Portal Modelo com Docker Compose"
    "property=og:title": "Subir a demonstração com Docker Compose"
    "keywords": "Plone, PortalBrasil: Legislativo, Docker, Docker Compose, demonstração"
---

# Subir a demonstração com Docker Compose

Este guia mostra como experimentar o Portal Modelo sem instalar Python nem Node.js, usando as imagens publicadas.

## Pré-requisitos

- Uma versão recente do Docker, com o Docker Compose.
- A porta 80 livre no seu computador.

No Windows com WSL, acrescente ao arquivo `C:\Windows\System32\Drivers\etc\hosts` a linha:

```text
127.0.0.1  portal-modelo.localhost
```

## Demonstração sem persistência

1.  Crie uma pasta chamada `PortalModelo`.
2.  Salve nela o arquivo [`docker-compose-demo.yml`](https://raw.githubusercontent.com/portal-br/legislativo/refs/heads/main/docker-compose-demo.yml) com o nome `docker-compose.yml`.
3.  Dentro da pasta, inicie a stack:

    ```shell
    docker compose up
    ```

4.  Acesse `http://portal-modelo.localhost` no navegador.

```{warning}
Os dados da demonstração **não são persistidos**: ao remover os contêineres, o conteúdo criado se perde.
Não use este arquivo em produção.
```

## Portal Modelo com dados persistentes

Use o arquivo [`docker-compose.yml`](https://raw.githubusercontent.com/portal-br/legislativo/refs/heads/main/docker-compose.yml) no lugar do arquivo de demonstração.
Ele inclui um banco de dados PostgreSQL, e os dados ficam no volume Docker `portal-modelo_vol-site-data`.

1.  Salve o arquivo com o nome `docker-compose.yml` em uma pasta própria.
2.  Inicie a stack em segundo plano:

    ```shell
    docker compose up -d
    ```

3.  Na primeira vez, crie o site no banco de dados:

    ```shell
    docker compose run --rm backend create-site
    ```

    As variáveis de {doc}`/reference/variaveis-de-ambiente` também valem aqui, com a opção `-e` do `docker compose run`.

4.  Acesse `http://portal-modelo.localhost` no navegador.

## Servir em outro endereço

Use a variável `STACK_HOSTNAME`:

```shell
STACK_HOSTNAME=novo.camara.sp.leg.br docker compose up
```

As demais variáveis estão em {doc}`/reference/variaveis-de-ambiente`.
