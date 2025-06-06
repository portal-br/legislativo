# Mudanças

<!-- towncrier release notes start -->
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


