# Portal Modelo 🚀
## PortalBrasil: Legislativo

[![Testes](https://github.com/portal-br/legislativo/actions/workflows/main.yml/badge.svg)](https://github.com/portal-br/legislativo/actions/workflows/main.yml)

Ferramenta de portais para casas do legislativo brasileiro

## Quick Start 🏁

### Prerequisites ✅

Ensure you have the following installed:

- UV 🐍
- Node 22 🟩
- pnpm 🧶
- Docker 🐳

### Installation 🔧

1. Clone the repository:

```shell
git clone git@github.com:portal-br/legislativo.git
cd portalbrasil-legislativo
```

2. Install both Backend and Frontend:

```shell
make install
```

### Fire Up the Servers 🔥

1. Create a new Plone site on your first run:

```shell
make backend-create-site
```

2. Start the Backend at [http://localhost:8080/](http://localhost:8080/):

```shell
make backend-start
```

3. In a new terminal, start the Frontend at [http://localhost:3000/](http://localhost:3000/):

```shell
make frontend-start
```

Voila! Your Plone site should be live and kicking! 🎉

### Local Stack Deployment 📦

Deploy a local `Docker Compose` environment that includes:

- Docker images for Backend and Frontend 🖼️
- A stack with a Traefik router and a Postgres database 🗃️
- Accessible at [http://portal-modelo.localhost](http://portal-modelo.localhost) 🌐

Execute the following:

```shell
make stack-start
make stack-create-site
```

And... you're all set! Your Plone site is up and running locally! 🚀

## Project Structure 🏗️

This monorepo consists of three distinct sections: `backend`, `frontend`, and `devops`.

- **backend**: Houses the API and Plone installation, utilizing pip instead of buildout, and includes a policy package named portalbrasil.legislativo.
- **frontend**: Contains the React (Volto) package.
- **devops**: Encompasses Docker Stack, Ansible playbooks, and Cache settings.

### Why This Structure? 🤔

- All necessary codebases to run the site are contained within the repo (excluding existing addons for Plone and React).
- Specific GitHub Workflows are triggered based on changes in each codebase (refer to .github/workflows).
- Simplifies the creation of Docker images for each codebase.
- Demonstrates Plone installation/setup without buildout.

## Code Quality Assurance 🧐

To automatically format your code and ensure it adheres to quality standards, execute:

```shell
make check
```

It is possible to only run `format`:

```shell
make format
```

or `lint`:

 ```shell
make lint
```

Linters can be run individually within the `backend` or `frontend` folders.

## Internationalization 🌐

Generate translation files for Plone and Volto with ease:

```shell
make i18n
```

## Credits and Acknowledgements 🙏

Generated using [Cookieplone (0.8.4)](https://github.com/plone/cookieplone) and [cookieplone-templates (86480b4)](https://github.com/plone/cookieplone-templates/commit/86480b44baa3953c98534071089ac3c6b656f3f5) on 2025-03-14 15:47:43.801432. A special thanks to all contributors and supporters!
