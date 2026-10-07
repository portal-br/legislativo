# Mudanças

<!-- towncrier release notes start -->

## 4.0.0-alpha.4 (2026-10-06)

### Breaking

- Troca `@portalbrasil/core` pelo tema `@simplesconsultoria/volto-light-theme` e `volto-form-block` por `@plone/volto-form-block`, sobre o Volto 19.3.0 com pnpm 10. @ericof 

### Funcionalidade

- Adiciona o bloco Iframe, para incorporar páginas de outros sistemas. @ericof 
- Adiciona o bloco Múltiplos botões, com links exibidos como botões, cards ou imagens. @ericof 
- Links para arquivos em listagens e teasers abrem a página do arquivo, que exibe PDFs no navegador, em vez de baixar o arquivo. @ericof 
- Notícias e galerias novas começam com blocos prontos: notícias com a imagem principal, galerias com a listagem das próprias imagens. @ericof 

### Interno

- Migra o pacote para TypeScript em modo estrito, com testes em Vitest e checagem de tipos no `make lint`. O visualizador de PDF da visão de arquivo e a ativação do VLibras passam a ser implementados no próprio pacote. @ericof 

### Teste

- Testa as funcionalidades que o tema entrega ao Portal Modelo: bloco de imagem principal, variações de listagem e temas de bloco. @ericof 

## 4.0.0-alpha.3 (2025-06-05)


### Funcionalidade

- Visualizador de PDF na visão padrão de arquivo. @ericof [#12](https://github.com/portal-br/legislativo/issue/12)
- Atualiza @portalbrasil/core para versão 1.0.0-alpha.8. @ericof 


### Correção de Bug

- Corrige exibição do menu expandido. @ericof [#11](https://github.com/portal-br/legislativo/issue/11)

## 4.0.0-alpha.2 (2025-06-02)


### Interno

- Atualiza .eslintrc.js e tsconfig.json para mapearem o código desse pacote como @portalbrasil/legislativo. @ericof 
- Atualiza @plone/volto para versão 18.22.0. @ericof 
- Atualiza @portalbrasil/core para versão 1.0.0-alpha.7. @ericof 

## 4.0.0-alpha.1 (2025-04-09)


### Funcionalidade

- Adiciona dependência do volto-form-support @ericof [#1](https://github.com/portal-br/legislativo/issue/1)
- Atualiza @portalbrasil/core para versão 1.0.0-alpha.5 @ericof [#7](https://github.com/portal-br/legislativo/issue/7)
- Adiciona dependência do @portalbrasil/core @plonegovbr 
- Primeira versão do Portal Modelo@plonegovbr
