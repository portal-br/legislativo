---
myst:
  html_meta:
    "description": "Como o repositório do Portal Modelo está organizado"
    "property=og:description": "Como o repositório do Portal Modelo está organizado"
    "property=og:title": "Organização do projeto"
    "keywords": "Plone, Volto, PortalBrasil: Legislativo, PortalBrasil: Intranet, organização"
---

# Organização do projeto

O repositório reúne o backend, o frontend, a documentação e os arquivos de implantação do Portal Modelo.

`backend/`
:   Pacote Python `portalbrasil.legislativo`: distribuição, perfis, serviços da API e testes.

`frontend/`
:   Add-on do Volto `@portalbrasil/legislativo`: configuração do site e componentes próprios, como a visão de arquivo com o visualizador de PDF.

`docs/`
:   Esta documentação.

`docker-compose*.yml`
:   Stacks do Docker Compose para demonstração, produção e desenvolvimento.

## Relação com o PortalBrasil: Intranet

O Portal Modelo e o [PortalBrasil: Intranet](https://github.com/portal-br/intranet) são gerados pelo mesmo template do [Cookieplone](https://github.com/plone/cookieplone) e compartilham a mesma forma em várias partes, adaptadas a cada projeto:

- a fábrica de sites e os utilitários de criação de site;
- os serviços `@sites` e `@system` da API;
- a ferramenta de migração, que informa a versão do pacote e dos perfis;
- os perfis `base` e `cmfdependencies`;
- a camada de testes e a estrutura da suíte de testes;
- os workflows de integração contínua.

O código é copiado e adaptado, não compartilhado como dependência: cada projeto evolui no seu ritmo.
O que é específico do Portal Modelo — a distribuição `portalmodelo`, o conteúdo de exemplo, o fluxo de trabalho público e a visão de arquivo — existe só aqui.

## Tema

O visual vem do tema [`sc-volto-light-theme`](https://github.com/simplesconsultoria/sc-volto-light-theme), construído sobre o Volto Light Theme.
Cabeçalho, rodapé, menu e seletor de tema são configurados pelos behaviors do site, sem componentes próprios no add-on.
