---
myst:
  html_meta:
    "description": "A distribuição portalmodelo e o que ela entrega"
    "property=og:description": "A distribuição portalmodelo e o que ela entrega"
    "property=og:title": "A distribuição do Portal Modelo"
    "keywords": "Plone, PortalBrasil: Legislativo, distribuição, plone.distribution"
---

# A distribuição do Portal Modelo

O Portal Modelo é entregue como uma {term}`distribuição` do Plone, chamada `portalmodelo`.
Uma distribuição é uma receita de criação de sites: diz quais perfis aplicar, quais perguntas fazer a quem cria o site e qual conteúdo importar.

## Perfis

O pacote `portalbrasil.legislativo` registra três perfis do GenericSetup, aplicados nesta ordem:

`base`
:   Perfil de base do site, no lugar do perfil padrão do Plone.
    Define as ferramentas, o fluxo de trabalho padrão e as configurações gerais.

`cmfdependencies`
:   Dependências do CMF que o Plone precisa para funcionar.

`default`
:   Configuração do Portal Modelo: tipos de conteúdo, registro, tema e add-ons como o `plone.formblock` e o tema `sc.voltolighttheme`.
    Ao final, importa um conteúdo básico, presente em todo site.

## Conteúdo

Há dois conjuntos de conteúdo:

- o **conteúdo básico**, importado sempre, pelo perfil `default`;
- o **conteúdo de exemplo**, importado quando a opção `setup_content` está ligada (o padrão).

Para atualizar o conteúdo de exemplo a partir de um site, use `make backend-update-example-content`.

## Por que uma distribuição

Com a distribuição, criar um site é um passo só, seja pela linha de comando (`make backend-create-site`), pela imagem de contêiner (`create-site`) ou pela tela de criação de sites do Plone.
O resultado é sempre o mesmo, e as mudanças na receita ficam versionadas no repositório.
