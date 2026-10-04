---
myst:
  html_meta:
    "description": "Blocos do Portal Modelo"
    "property=og:description": "Blocos do Portal Modelo"
    "property=og:title": "Blocos"
    "keywords": "Plone, Volto, PortalBrasil: Legislativo, blocos"
---

# Blocos

Além dos blocos do Volto e do tema, o Portal Modelo traz blocos próprios.

## Múltiplos botões

O bloco **Múltiplos botões** (`multiButtons`) mostra uma lista de links lado a lado, como atalhos para a ouvidoria, a agenda ou o portal da transparência.
Ele também pode ser usado dentro do bloco de grade.

| Campo | Descrição |
|---|---|
| Exibição | `Botões`, `Cards` ou `Imagens` |
| Lista de botões | Os links do bloco; os campos de cada botão dependem da exibição |
| Colunas | Número máximo de botões por linha, de 1 a 6. Telas pequenas mostram um botão por linha |
| Ocupar toda a largura | Os botões dividem a largura do bloco. Desmarcado, todos ficam com a largura do mais largo |
| Cor de fundo | Um dos temas de bloco do site |

Campos de cada botão, por exibição:

| Exibição | Campos |
|---|---|
| Botões | rótulo, link, ícone, abrir em nova aba |
| Cards | rótulo, descrição, link, abrir em nova aba |
| Imagens | rótulo para leitores de tela, imagem, texto alternativo, link, abrir em nova aba |

Na exibição por imagens, a imagem e o texto alternativo são obrigatórios: o texto alternativo descreve o que o botão faz para quem usa leitor de tela.
Um botão sem link aparece esmaecido e não pode ser clicado.
