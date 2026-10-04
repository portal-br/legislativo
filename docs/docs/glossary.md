---
myst:
  html_meta:
    "description": "Termos usados na documentação do PortalBrasil: Legislativo."
    "property=og:description": "Termos usados na documentação do PortalBrasil: Legislativo."
    "property=og:title": "Glossário"
    "keywords": "Plone, Volto, PortalBrasil: Legislativo, glossário"
---

(glossary-label)=

# Glossário

```{glossary}
:sorted: true

Plone
    [Plone](https://plone.org/) é um sistema de gestão de conteúdo de código aberto, usado por governos, universidades e empresas no mundo todo.
    O Portal Modelo usa o Plone 6 como backend.

Volto
    [Volto](https://6.docs.plone.org/volto/index.html) é o frontend do Plone 6, escrito em React.
    Ele conversa com o backend pela API REST do Plone.

add-on
    Pacote que estende o Plone.
    No backend, um add-on é um pacote Python; no Volto, é um pacote JavaScript.

distribuição
    Receita de criação de sites do pacote [`plone.distribution`](https://github.com/plone/plone.distribution): perfis do GenericSetup, perguntas feitas ao criar o site e conteúdo inicial.
    O Portal Modelo registra a distribuição `portalmodelo`.

behavior
    Conjunto reutilizável de campos e comportamentos que pode ser ligado a um tipo de conteúdo, como o título de navegação (`volto.navtitle`).

Markedly Structured Text
MyST
    [MyST](https://myst-parser.readthedocs.io/en/latest/) é a variante de Markdown usada nesta documentação.

Sphinx
    [Sphinx](https://www.sphinx-doc.org/en/master/) gera esta documentação em HTML.
```
