---
myst:
  html_meta:
    "description": "Alvos do Makefile do Portal Modelo"
    "property=og:description": "Alvos do Makefile do Portal Modelo"
    "property=og:title": "Alvos do Makefile"
    "keywords": "Plone, PortalBrasil: Legislativo, Makefile, desenvolvimento"
---

# Alvos do Makefile

Os alvos abaixo são do `Makefile` da raiz do repositório.
Para ver a lista atualizada, rode `make help`.

## Instalação e execução

| Alvo | Descrição |
|---|---|
| `install` | Instala o backend e o frontend e cria o site. |
| `backend-install` | Cria o ambiente Python, instala o Plone e cria o site. |
| `frontend-install` | Instala as dependências do frontend. |
| `backend-create-site` | Cria um site Plone com o conteúdo de exemplo. |
| `backend-start` | Inicia o backend em `http://localhost:8080`. |
| `frontend-start` | Inicia o frontend em `http://localhost:3000`. |
| `backend-update-example-content` | Exporta o conteúdo do site para o conteúdo de exemplo do pacote. |
| `clean` | Remove a instalação. |

## Qualidade

| Alvo | Descrição |
|---|---|
| `format` | Formata o código do backend e do frontend. |
| `lint` | Verifica o código: ruff, mypy, ESLint, Prettier, Stylelint e TypeScript. |
| `test` | Roda os testes do backend e do frontend. |
| `backend-test` | Roda os testes do backend. |
| `frontend-test` | Roda os testes do frontend. |

## Contêineres

| Alvo | Descrição |
|---|---|
| `build-images` | Gera as imagens de contêiner do backend e do frontend. |
| `stack-create-site` | Cria o site na stack local do Docker Compose. |
| `stack-start` | Inicia a stack local em `http://legislativo.localhost`. |
| `stack-status` | Mostra o estado da stack local. |
| `stack-stop` | Para a stack local. |
| `stack-rm` | Remove a stack local e seus volumes. |
| `acceptance-images-build` | Gera as imagens usadas nos testes de aceitação. |
| `acceptance-containers-start` | Inicia os contêineres de aceitação. |
| `acceptance-containers-stop` | Para os contêineres de aceitação. |
