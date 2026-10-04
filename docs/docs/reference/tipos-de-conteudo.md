---
myst:
  html_meta:
    "description": "Tipos de conteúdo e behaviors do Portal Modelo"
    "property=og:description": "Tipos de conteúdo e behaviors do Portal Modelo"
    "property=og:title": "Tipos de conteúdo"
    "keywords": "Plone, PortalBrasil: Legislativo, tipos de conteúdo, behaviors"
---

# Tipos de conteúdo

O Portal Modelo usa os tipos de conteúdo do Plone, ajustados para o Volto.
A tabela lista cada tipo, a classe que o implementa e se ele pode ser adicionado em qualquer pasta.

| Tipo | Classe | Adicionável em qualquer lugar |
|---|---|---|
| Collection | `plone.app.contenttypes.content.Collection` | não |
| Document | `plone.volto.content.FolderishDocument` | sim |
| Event | `plone.volto.content.FolderishEvent` | sim |
| File | `plone.app.contenttypes.content.File` | sim |
| Folder | `plone.app.contenttypes.content.Folder` | não |
| Galeria | `portalbrasil.legislativo.content.galeria.Galeria` | sim |
| Image | `plone.app.contenttypes.content.Image` | sim |
| Link | `plone.app.contenttypes.content.Link` | sim |
| News Item | `plone.volto.content.FolderishNewsItem` | sim |
| Plone Site | `Products.CMFPlone.Portal.PloneSite` | não |

Páginas, eventos e notícias são *folderish*: podem conter outros conteúdos.

## Galeria

A Galeria é um tipo do Portal Modelo para publicar fotos, como as de uma sessão solene ou de um evento.
Ela aceita apenas imagens, aparece na navegação e guarda versões a cada edição.
Podem adicionar galerias os administradores do site, o dono da pasta e quem tem o papel de colaborador, pela permissão `portalbrasil.legislativo: Add Galeria`.

## Fluxo de trabalho

O fluxo de trabalho padrão é o `simple_publication_workflow` do Plone, com os estados privado, pendente e publicado.
Arquivos e imagens não têm fluxo de trabalho próprio: seguem a visibilidade da pasta em que estão.

## Visão de arquivo

A visão padrão do tipo File mostra o link de download com o tamanho do arquivo.
Para arquivos PDF, a página também exibe o documento no navegador.
Links para arquivos em listagens e teasers abrem essa página, em vez de baixar o arquivo.

## {term}`behavior`s

Todos os tipos, exceto o site, têm o título de navegação (`volto.navtitle`), que permite usar um título mais curto nos menus.

| Tipo | Behaviors |
|---|---|
| Collection | `plone.namefromtitle`, `plone.collection`, `plone.shortname`, `plone.excludefromnavigation`, `plone.dublincore`, `plone.richtext`, `plone.relateditems`, `plone.locking`, `volto.navtitle` |
| Document | `plone.basic`, `volto.preview_image_link`, `volto.kicker`, `plone.categorization`, `plone.publication`, `plone.ownership`, `plone.relateditems`, `plone.shortname`, `volto.navtitle`, `plone.excludefromnavigation`, `volto.blocks`, `plone.constraintypes`, `plone.namefromtitle`, `plone.versioning`, `plone.locking` |
| Event | `plone.eventbasic`, `plone.eventrecurrence`, `plone.eventlocation`, `plone.eventattendees`, `plone.eventcontact`, `plone.basic`, `volto.preview_image_link`, `volto.kicker`, `plone.categorization`, `plone.publication`, `plone.ownership`, `plone.shortname`, `volto.navtitle`, `plone.excludefromnavigation`, `plone.relateditems`, `volto.blocks`, `plone.constraintypes`, `plone.namefromtitle`, `plone.textindexer`, `plone.versioning`, `plone.locking` |
| File | `plone.categorization`, `plone.publication`, `plone.ownership`, `volto.preview_image_link`, `volto.kicker`, `plone.shortname`, `volto.navtitle`, `plone.relateditems`, `plone.namefromfilename`, `plone.versioning`, `plone.locking` |
| Folder | `plone.dublincore`, `plone.namefromtitle`, `plone.excludefromnavigation`, `plone.shortname`, `plone.constraintypes`, `plone.relateditems`, `plone.nextprevioustoggle`, `volto.navtitle` |
| Galeria | `volto.navtitle`, `plone.namefromtitle`, `volto.preview_image_link`, `plone.excludefromnavigation`, `plone.shortname`, `plone.dublincore`, `plone.relateditems`, `plone.versioning`, `plone.locking`, `volto.blocks` |
| Image | `volto.kicker`, `plone.categorization`, `plone.publication`, `plone.ownership`, `plone.shortname`, `volto.navtitle`, `plone.relateditems`, `plone.namefromfilename`, `plone.versioning`, `plone.locking` |
| Link | `plone.basic`, `volto.preview_image_link`, `volto.kicker`, `plone.categorization`, `plone.publication`, `plone.ownership`, `plone.shortname`, `volto.navtitle`, `plone.excludefromnavigation`, `plone.namefromtitle`, `plone.versioning`, `plone.locking` |
| News Item | `plone.basic`, `volto.preview_image_link`, `volto.kicker`, `plone.categorization`, `plone.publication`, `plone.ownership`, `plone.shortname`, `volto.navtitle`, `plone.excludefromnavigation`, `plone.relateditems`, `volto.blocks`, `plone.constraintypes`, `plone.namefromtitle`, `plone.versioning`, `plone.locking` |
| Plone Site | `plonegovbr.socialmedia.settings`, `sc.voltolighttheme.themeselector`, `sc.voltolighttheme.siteheader`, `sc.voltolighttheme.footer`, `volto.preview_image_link`, `plone.basic`, `plone.categorization`, `plone.relateditems`, `plone.locking`, `plone.excludefromnavigation`, `volto.blocks`, `kitconcept.sticky_menu` |

Os behaviors do site configuram o cabeçalho, o rodapé, o seletor de tema e as redes sociais.
