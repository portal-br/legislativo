# Mudanças

<!-- towncrier release notes start -->
## 4.0.0a4 (2026-10-06)

### Backend


#### Breaking

- Atualiza para Plone 6.2.2 e Python 3.14, troca `collective.volto.formsupport` por `plone.formblock` e adota o tema `sc-voltolighttheme`. @ericof 
- Remove a dependência de `portalbrasil.core`: a distribuição `portalmodelo`, a criação de sites, os serviços `@sites` e `@system` e a ferramenta de migração passam a fazer parte do pacote. @ericof 


#### Funcionalidade

- Adiciona o tipo de conteúdo Galeria, para publicar galerias de fotos. @ericof 
- Atualiza o conteúdo base, importado em todo site novo, e o conteúdo de exemplo. Adiciona o alvo `update-base-content` para exportar o conteúdo base. @ericof 
- Define as cores do tema padrão do Portal Modelo: verde, azul e amarelo da bandeira, com a fonte Inter. @ericof 
- Usa o `simple_publication_workflow` como fluxo de trabalho padrão; arquivos e imagens ficam sem fluxo de trabalho. @ericof 


#### Correção de Bug

- Corrige o nome do domínio dos catálogos de tradução para `portalbrasil.legislativo` e completa a tradução para português do Brasil. @ericof 


#### Interno

- Remove o `__init__.py` do namespace `portalbrasil`, que passa a ser um namespace implícito (PEP 420). @ericof 
- Reorganiza a instalação nos perfis `base`, `cmfdependencies` e `default`: o conteúdo básico do site é importado pelo perfil `default` e o conteúdo de exemplo, pela distribuição. @ericof 
- Verifica os tipos com mypy em modo estrito no `make lint` e na integração contínua. @ericof 


#### Teste

- Reescreve a suíte de testes do backend com pytest e `pytest-plone`, cobrindo a criação do site, os tipos de conteúdo, o fluxo de trabalho e os serviços. @ericof 



### Frontend

#### Breaking

- Troca `@portalbrasil/core` pelo tema `@simplesconsultoria/volto-light-theme` e `volto-form-block` por `@plone/volto-form-block`, sobre o Volto 19.3.0 com pnpm 10. @ericof 

#### Funcionalidade

- Adiciona o bloco Iframe, para incorporar páginas de outros sistemas. @ericof 
- Adiciona o bloco Múltiplos botões, com links exibidos como botões, cards ou imagens. @ericof 
- Links para arquivos em listagens e teasers abrem a página do arquivo, que exibe PDFs no navegador, em vez de baixar o arquivo. @ericof 
- Notícias e galerias novas começam com blocos prontos: notícias com a imagem principal, galerias com a listagem das próprias imagens. @ericof 

#### Interno

- Migra o pacote para TypeScript em modo estrito, com testes em Vitest e checagem de tipos no `make lint`. O visualizador de PDF da visão de arquivo e a ativação do VLibras passam a ser implementados no próprio pacote. @ericof 

#### Teste

- Testa as funcionalidades que o tema entrega ao Portal Modelo: bloco de imagem principal, variações de listagem e temas de bloco. @ericof 



### Projeto


#### Funcionalidade

- Adiciona o alvo `backend-update-base-content`, que exporta o conteúdo do site para o conteúdo base do pacote. @ericof 
- Publica a documentação e o Storybook no GitHub Pages: a documentação na raiz do site e o Storybook em `/storybook`. @ericof 


#### Correção de Bug

- Corrige a stack local do Docker Compose: `make stack-start`, `make stack-create-site` e `make acceptance-images-build` passam a versão do Python para o build do backend, e `make stack-rm` remove o volume da stack. @ericof 


#### Interno

- Regenera a estrutura do projeto a partir do template `project` do cookieplone, com a integração contínua nos workflows do `plone/meta@2.x` e o `dependabot.yml` em `.github/`. @ericof 


#### Documentação

- Reescreve a documentação em português do Brasil: tutorial de instalação, guias para criar um site, subir a demonstração com Docker Compose e adicionar formulários, referência de tipos de conteúdo, variáveis de ambiente e alvos do Makefile, e conceitos sobre a distribuição e a organização do projeto. O Vale passa a verificar a ortografia em português do Brasil. @ericof 



## 4.0.0a3 (2025-06-05)

### Backend


#### Funcionalidade

- Adiciona o comportamento de título de navegação a todos os tipos de conteúdo. @ericof [#9](https://github.com/portal-br/legislativo/issues/9)
- Atualiza portalbrasil.core para versão 1.0.0a8. @ericof 


#### Documentação

- Atualiza conteúdo de exemplo. @ericof 



### Frontend


#### Funcionalidade

- Visualizador de PDF na visão padrão de arquivo. @ericof [#12](https://github.com/portal-br/legislativo/issue/12)
- Atualiza @portalbrasil/core para versão 1.0.0-alpha.8. @ericof 


#### Correção de Bug

- Corrige exibição do menu expandido. @ericof [#11](https://github.com/portal-br/legislativo/issue/11)



### Projeto


#### Correção de Bug

- Corrige versão do PM no docker-compose-demo.yml @ericof [#10](https://github.com/portal-br/legislativo/issue/10)



## 4.0.0a2 (2025-06-02)

### Backend


#### Funcionalidade

- Atualiza conteúdo de exemplo do Portal Modelo. @ericof 


#### Interno

- Atualiza portalbrasil.core para versão 1.0.0a7. @ericof 



### Frontend


#### Interno

- Atualiza .eslintrc.js e tsconfig.json para mapearem o código desse pacote como @portalbrasil/legislativo. @ericof 
- Atualiza @plone/volto para versão 18.22.0. @ericof 
- Atualiza @portalbrasil/core para versão 1.0.0-alpha.7. @ericof 



### Projeto


#### Funcionalidade

- Suporta o uso de variáveis de ambiente nos arquivos Docker compose. @ericof 


#### Interno

- GHA: Uso de workflows compartilhados em plone/meta. @ericof 


#### Documentação

- Atualiza o arquivo README.md. @ericof 



## 4.0.0a1 (2025-04-09)

### Backend


#### Funcionalidade

- Adiciona dependência do collective.volto.formsupport @ericof [#1](https://github.com/portal-br/legislativo/issues/1)
- Cria conteúdo de exemplo @rbenevid [#3](https://github.com/portal-br/legislativo/issues/3)
- Atualiza portalbrasil.core para versão 1.0.0a5 @ericof [#7](https://github.com/portal-br/legislativo/issues/7)
- Adiciona dependência do portalbrasil.core @plonegovbr 
- Primeira versão do Portal Modelo @plonegovbr 


#### Correção de Bug

- Corrige o formulário de criação de um novo site @ericof [#2](https://github.com/portal-br/legislativo/issues/2)



### Frontend


#### Funcionalidade

- Adiciona dependência do volto-form-support @ericof [#1](https://github.com/portal-br/legislativo/issue/1)
- Atualiza @portalbrasil/core para versão 1.0.0-alpha.5 @ericof [#7](https://github.com/portal-br/legislativo/issue/7)
- Adiciona dependência do @portalbrasil/core @plonegovbr 
- Primeira versão do Portal Modelo@plonegovbr 



### Projeto


#### Interno

- Corrige build da stack local @ericof 
- GHA: Adiciona workflow para changelog @ericof 
- GHA: Adiciona workflow para release de imagens após criação de novas tags @ericof 
- Implementa log na raiz do projeto @ericof 


