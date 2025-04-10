# syntax=docker/dockerfile:1.9
ARG PB_VERSION
FROM ghcr.io/portal-br/core-builder:${PB_VERSION:-latest} AS builder

# Move skeleton folder
RUN <<EOT
    mv /app /app_base
EOT

# Install dependencies
RUN --mount=type=cache,target=/root/.cache \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync \
        --locked \
        --no-dev \
        --no-group test \
        --group container \
        --no-install-project

COPY . /src
WORKDIR /src

# Install package
RUN --mount=type=cache,target=/root/.cache \
    uv sync \
        --locked \
        --no-dev \
        --no-group test \
        --group container \
        --no-editable

# Move skeleton files to /app
RUN <<EOT
    mv /app_base/* /app
    rm -Rf /app_base
    mv scripts/create_site.py /app/scripts/create_site.py
    mv scripts/default.json /app/scripts/default.json
EOT

# Compile translation files
RUN <<EOT
    /app/bin/python /compile_mo.py
EOT

FROM ghcr.io/portal-br/core-prod:${PB_VERSION:-latest}

LABEL maintainer="PloneGov-BR <gov@plone.org.br>" \
      org.label-schema.name="ghcr.io/portal-br/legislativo-backend" \
      org.label-schema.description="Portal Modelo." \
      org.label-schema.vendor="PloneGov-BR"


ENV ALLOWED_DISTRIBUTIONS=portalmodelo

# Copy the pre-built `/app` directory to the runtime container
# and change the ownership to user app and group app in one step.
COPY --from=builder --chown=500:500 /app /app

RUN <<EOT
    ln -s /data /app/var
    chown -R 500:500 /data
EOT
