#!/usr/bin/env bash

set -euo pipefail

# Instala python e pip
apk add --no-cache python3 py3-pip

# Cria links simbólicos para python3 e pip3
ln -sf python3 /usr/bin/python
ln -sf pip3 /usr/bin/pip

# Instala gcc para compilação de extensões
apk add --no-cache gcc

# Instala musl-dev
apk add --no-cache musl-dev

# Instala libffi-dev
apk add --no-cache libffi-dev

# Instala openssl-dev e openssl
apk add --no-cache openssl-dev openssl

# Instala python3-dev
apk add --no-cache python3-dev

# Baixa o repositorio
git clone git@github.com:Nok-Tech/nok-dns.git /opt/nok-dns

# Navega para o diretório do repositório
cd /opt/nok-dns

# Instala as dependências com pyproject.toml
pip install .
