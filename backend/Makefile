### Defensive settings for make:
#     https://tech.davis-hansson.com/p/make/
SHELL:=bash
.ONESHELL:
.SHELLFLAGS:=-xeu -o pipefail -O inherit_errexit -c
.SILENT:
.DELETE_ON_ERROR:
MAKEFLAGS+=--warn-undefined-variables
MAKEFLAGS+=--no-builtin-rules

# We like colors
# From: https://coderwall.com/p/izxssa/colored-makefile-for-golang-projects
RED=`tput setaf 1`
GREEN=`tput setaf 2`
RESET=`tput sgr0`
YELLOW=`tput setaf 3`

IMAGE_NAME_PREFIX=ghcr.io/portal-br/legislativo
IMAGE_TAG=latest
SEED=$(shell date +'%Y%m%d-%H%M%S')

# Python checks
UV?=uv

# installed?
ifeq (, $(shell which $(UV) ))
  $(error "UV=$(UV) not found in $(PATH)")
endif

PLONE_SITE_ID=Plone
BACKEND_FOLDER=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
PB_VERSION=$(shell cat $(BACKEND_FOLDER)/version.txt)
BASE_CONTENT_FOLDER=${BACKEND_FOLDER}/src/portalbrasil/legislativo/setuphandlers/basecontent
EXAMPLE_CONTENT_FOLDER=${BACKEND_FOLDER}/src/portalbrasil/legislativo/distributions/legislativo/content

VENV_FOLDER=$(BACKEND_FOLDER)/.venv
BIN_FOLDER=$(VENV_FOLDER)/bin

# Environment variables to be exported
export ALLOWED_DISTRIBUTIONS := portalmodelo
export PYTHONWARNINGS := ignore
export DOCKER_BUILDKIT := 1

all: build

# Add the following 'help' target to your Makefile
# And add help text after each target name starting with '\#\#'
.PHONY: help
help: ## This help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

###########################################
# Install & Config
###########################################
instance/etc/zope.ini instance/etc/zope.conf: ## Create instance configuration
	@echo "$(GREEN)==> Create instance configuration$(RESET)"
	@uvx cookiecutter -f --no-input --config-file instance.yaml gh:plone/cookiecutter-zope-instance

.PHONY: config
config: instance/etc/zope.ini

.PHONY: sync
sync: ## Sync project dependencies
	@echo "$(GREEN)==> Sync project dependencies$(RESET)"
	@uv sync

.PHONY: install
install: sync config ## Install Plone and dependencies

$(VENV_FOLDER): sync ## Install Plone and dependencies

.PHONY: clean
clean: ## Clean environment
	@echo "$(RED)==> Cleaning environment and build$(RESET)"
	@rm -rf $(VENV_FOLDER) pyvenv.cfg .installed.cfg instance .venv .pytest_cache .ruff_cache constraints* requirements*

.PHONY: remove-data
remove-data: ## Remove all content
	@echo "$(RED)==> Removing all content$(RESET)"
	rm -rf $(VENV_FOLDER) instance/var


###########################################
# Environment
###########################################
.PHONY: start
start: $(VENV_FOLDER) instance/etc/zope.ini ## Start a Plone instance on localhost:8080
	@uv run runwsgi instance/etc/zope.ini

.PHONY: console
console: $(VENV_FOLDER) instance/etc/zope.ini ## Start a console into a Plone instance
	@uv run zconsole debug instance/etc/zope.conf

.PHONY: create-site
create-site: $(VENV_FOLDER) instance/etc/zope.ini ## Create a new site from scratch
	@uv run zconsole run instance/etc/zope.conf ./scripts/create_site.py

###########################################
# Content
###########################################
.PHONY: update-base-content
update-base-content: $(VENV_FOLDER) ## Export base content inside package
	@echo "$(GREEN)==> Export base content into $(BASE_CONTENT_FOLDER) $(RESET)"
	if [ -d $(BASE_CONTENT_FOLDER)/content ]; then rm -r $(BASE_CONTENT_FOLDER)/* ;fi
	@uv run plone-exporter instance/etc/zope.conf $(PLONE_SITE_ID) $(BASE_CONTENT_FOLDER)

.PHONY: update-example-content
update-example-content: $(VENV_FOLDER) ## Export example content inside package
	@echo "$(GREEN)==> Export example content into $(EXAMPLE_CONTENT_FOLDER) $(RESET)"
	if [ -d $(EXAMPLE_CONTENT_FOLDER)/content ]; then rm -r $(EXAMPLE_CONTENT_FOLDER)/* ;fi
	@uv run plone-exporter instance/etc/zope.conf $(PLONE_SITE_ID) $(EXAMPLE_CONTENT_FOLDER)

###########################################
# QA
###########################################
.PHONY: lint
lint: ## Check and fix code base according to Plone standards
	@echo "$(GREEN)==> Lint codebase$(RESET)"
	@uvx ruff@latest check --fix --config $(BACKEND_FOLDER)/pyproject.toml
	@uvx pyroma@latest -d .
	@uvx check-python-versions@latest .
	@uvx zpretty@latest --check src

.PHONY: format
format: ## Check and fix code base according to Plone standards
	@echo "$(GREEN)==> Format codebase$(RESET)"
	@uvx ruff@latest check --select I --fix --config $(BACKEND_FOLDER)/pyproject.toml
	@uvx ruff@latest format --config $(BACKEND_FOLDER)/pyproject.toml
	@uvx zpretty@latest -i src

## Add bobtemplates features (check bobtemplates.plone's documentation to get the list of available features)
add: $(VENV_FOLDER)
	@uvx plonecli add -b .mrbob.ini $(filter-out $@,$(MAKECMDGOALS))

###########################################
# i18n
###########################################
.PHONY: i18n
i18n: $(VENV_FOLDER) ## Update locales
	@echo "$(GREEN)==> Updating locales$(RESET)"
	@uv run python -m portalbrasil.legislativo.locales

###########################################
# Tests
###########################################
.PHONY: test
test: $(VENV_FOLDER) ## run tests
	@uv run pytest

.PHONY: test-coverage
test-coverage: $(VENV_FOLDER) ## run tests with coverage
	@uv run pytest --cov=portalbrasil.legislativo --cov-report term-missing

###########################################
# Docker Images
###########################################
.PHONY: build-image
build-image:  ## Build Docker Images
	@echo "$(GREEN)==> Building $(IMAGE_NAME_PREFIX)-backend:$(IMAGE_TAG) $(RESET)"
	@docker build . --platform linux/amd64 -t $(IMAGE_NAME_PREFIX)-backend:$(IMAGE_TAG) --progress plain -f Dockerfile --build-arg PB_VERSION=$(PB_VERSION)
	@echo "$(GREEN)==> Building $(IMAGE_NAME_PREFIX)-demo:$(IMAGE_TAG) $(RESET)"
	@docker build .  --platform linux/amd64 --pull=false -t $(IMAGE_NAME_PREFIX)-demo:$(IMAGE_TAG) -f Dockerfile.demo --build-arg IMAGE_TAG=$(IMAGE_TAG) --build-arg SEED=$(SEED)
