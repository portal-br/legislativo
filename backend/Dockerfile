# syntax=docker/dockerfile:1
ARG PLONE_VERSION=6.1.0
FROM plone/server-builder:${PLONE_VERSION} AS builder

WORKDIR /app


# Add local code
COPY scripts/ scripts/
COPY . src

# Install local requirements and pre-compile mo files
RUN <<EOT
    set -e
    bin/pip install uv hatch hatchling wheel
    VIRTUAL_ENV=/app bin/uv --directory src sync --frozen --active --no-editable
    bin/python /compile_mo.py
    rm -Rf src
EOT

FROM plone/server-prod-config:${PLONE_VERSION}

LABEL maintainer="PloneGov-BR <gov@plone.org.br>" \
      org.label-schema.name="portalbrasil-legislativo-backend" \
      org.label-schema.description="PortalBrasil: Legislativo." \
      org.label-schema.vendor="PloneGov-BR"

# Copy /app from builder
COPY --from=builder /app /app

RUN <<EOT
    set -e
    ln -s /data /app/var
EOT
