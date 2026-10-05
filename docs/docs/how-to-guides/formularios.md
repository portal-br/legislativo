---
myst:
  html_meta:
    "description": "Como adicionar um formulário a uma página do Portal Modelo"
    "property=og:description": "Como adicionar um formulário a uma página do Portal Modelo"
    "property=og:title": "Adicionar um formulário"
    "keywords": "Plone, PortalBrasil: Legislativo, formulário, plone.formblock"
---

# Adicionar um formulário

O Portal Modelo usa o projeto [form-block](https://github.com/plone/form-block): o pacote `plone.formblock` no backend e o add-on `@plone/volto-form-block` no frontend.
Eles oferecem um bloco de formulário que envia as respostas por e-mail ou as guarda no site.

## Adicione o bloco

1.  Edite a página que vai receber o formulário.
2.  Adicione um novo bloco e escolha o bloco de formulário.
3.  Na barra lateral, crie os campos do formulário e defina o destinatário das mensagens.
4.  Salve a página.

## Envio de e-mails

Para que os formulários enviem e-mails, configure o servidor de e-mail do site no painel de controle **Correio**.

## Proteção contra spam

O `plone.formblock` é instalado com o extra `honeypot`, que inclui no formulário um campo escondido.
Envios que preenchem esse campo são descartados.
Nos arquivos Docker Compose do projeto, o nome do campo é definido pela variável `HONEYPOT_FIELD`.
