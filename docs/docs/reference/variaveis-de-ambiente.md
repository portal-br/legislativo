---
myst:
  html_meta:
    "description": "Variáveis de ambiente do Portal Modelo"
    "property=og:description": "Variáveis de ambiente do Portal Modelo"
    "property=og:title": "Variáveis de ambiente"
    "keywords": "Plone, PortalBrasil: Legislativo, variáveis de ambiente, Docker"
---

# Variáveis de ambiente

## Criação do site

Lidas por `make backend-create-site` e pelo comando `create-site` das imagens de contêiner.
Uma variável vazia ou ausente mantém o valor padrão.

| Variável | Padrão | Descrição |
|---|---|---|
| `SITE_ID` | `Plone` | Identificador do site na instância Zope. |
| `SITE_TITLE` | `Câmara Modelo` | Título do site. |
| `SITE_DESCRIPTION` | `Site da câmara modelo` | Descrição do site. |
| `SITE_AVAILABLE_LANGUAGES` | `pt-br` | Idiomas disponíveis, separados por vírgula. |
| `SITE_DEFAULT_LANGUAGE` | `pt-br` | Idioma padrão. |
| `SITE_PORTAL_TIMEZONE` | `America/Sao_Paulo` | Fuso horário do site. |
| `SITE_SETUP_CONTENT` | verdadeiro | Importa o conteúdo de exemplo. Aceita `true`, `false`, `1`, `0`, `yes`, `no`. |
| `DELETE_EXISTING` | falso | Apaga um site existente com o mesmo identificador antes de criá-lo. |

## Docker Compose

Usadas pelos arquivos `docker-compose.yml` e `docker-compose-demo.yml`.

| Variável | Padrão | Descrição |
|---|---|---|
| `STACK_HOSTNAME` | `portal-modelo.localhost` | Endereço em que a stack responde. |
| `PM_VERSION` | versão publicada | Versão das imagens de contêiner. |
| `DB_NAME` | `plone` | Nome do banco PostgreSQL (somente `docker-compose.yml`). |
| `DB_USER` | `plone` | Usuário do banco (somente `docker-compose.yml`). |
| `DB_PASSWORD` | valor de exemplo | Senha do banco (somente `docker-compose.yml`). Troque em produção. |
| `DB_HOST` | `db` | Servidor do banco (somente `docker-compose.yml`). |
| `DB_PORT` | `5432` | Porta do banco (somente `docker-compose.yml`). |
| `HONEYPOT_FIELD` | `your_email` | Nome do campo escondido usado contra spam nos formulários. |
