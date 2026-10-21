# Mudanças

<!-- towncrier release notes start -->

## 4.0.0a5 (2026-10-21)


### Correção de Bug

- Atualiza o `sc-voltolighttheme` para 1.0.0a12: os formulários de tema, cabeçalho e rodapé e os perfis de instalação passam a aparecer em português. @ericof [#16](https://github.com/portal-br/legislativo/issues/16)
- A atualização do site (`@upgrade` ou `@@plone-upgrade`) passa a executar os passos de upgrade do `sc-voltolighttheme`, do `plonegovbr.socialmedia`, do `plone.formblock` e do próprio Portal Modelo; antes, só os add-ons do núcleo do Plone eram atualizados. @ericof 

## 4.0.0a4 (2026-10-06)


### Breaking

- Atualiza para Plone 6.2.2 e Python 3.14, troca `collective.volto.formsupport` por `plone.formblock` e adota o tema `sc-voltolighttheme`. @ericof 
- Remove a dependência de `portalbrasil.core`: a distribuição `portalmodelo`, a criação de sites, os serviços `@sites` e `@system` e a ferramenta de migração passam a fazer parte do pacote. @ericof 


### Funcionalidade

- Adiciona o tipo de conteúdo Galeria, para publicar galerias de fotos. @ericof 
- Atualiza o conteúdo base, importado em todo site novo, e o conteúdo de exemplo. Adiciona o alvo `update-base-content` para exportar o conteúdo base. @ericof 
- Define as cores do tema padrão do Portal Modelo: verde, azul e amarelo da bandeira, com a fonte Inter. @ericof 
- Usa o `simple_publication_workflow` como fluxo de trabalho padrão; arquivos e imagens ficam sem fluxo de trabalho. @ericof 


### Correção de Bug

- Corrige o nome do domínio dos catálogos de tradução para `portalbrasil.legislativo` e completa a tradução para português do Brasil. @ericof 


### Interno

- Remove o `__init__.py` do namespace `portalbrasil`, que passa a ser um namespace implícito (PEP 420). @ericof 
- Reorganiza a instalação nos perfis `base`, `cmfdependencies` e `default`: o conteúdo básico do site é importado pelo perfil `default` e o conteúdo de exemplo, pela distribuição. @ericof 
- Verifica os tipos com mypy em modo estrito no `make lint` e na integração contínua. @ericof 


### Teste

- Reescreve a suíte de testes do backend com pytest e `pytest-plone`, cobrindo a criação do site, os tipos de conteúdo, o fluxo de trabalho e os serviços. @ericof
