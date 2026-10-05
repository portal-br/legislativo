---
myst:
  html_meta:
    "description": "Como criar um site com a distribuição do Portal Modelo"
    "property=og:description": "Como criar um site com a distribuição do Portal Modelo"
    "property=og:title": "Criar um site com a distribuição"
    "keywords": "Plone, PortalBrasil: Legislativo, distribuição, criar site"
---

# Criar um site com a distribuição

Este guia mostra como criar um site do Portal Modelo com valores próprios: identificador, título, idioma e conteúdo de exemplo.

## Com valores padrão

Na raiz do repositório, com o backend instalado:

```shell
make backend-create-site
```

O site é criado com o identificador `Plone`, o título "Câmara Modelo" e o conteúdo de exemplo.

## Com valores próprios

Defina as variáveis de ambiente antes do comando.
Por exemplo, para criar o site `exemplo`, com o título "Câmara de Exemplo" e sem o conteúdo de exemplo:

```shell
SITE_ID=exemplo SITE_TITLE="Câmara de Exemplo" SITE_SETUP_CONTENT=false make backend-create-site
```

A lista completa de variáveis está em {doc}`/reference/variaveis-de-ambiente`.

## Recriar um site existente

Se já existir um site com o mesmo identificador, a criação é interrompida e o site existente é mantido.
Para apagá-lo e criá-lo de novo, use `DELETE_EXISTING=1`:

```shell
DELETE_EXISTING=1 make backend-create-site
```

```{warning}
`DELETE_EXISTING=1` apaga o site e todo o seu conteúdo.
```
