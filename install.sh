#!/bin/sh

set -eu

apk add --no-cache python3 py3-pip git gcc musl-dev libffi-dev openssl-dev openssl python3-dev

# Cria links simbólicos para python3 e pip3
ln -sf python3 /usr/bin/python
ln -sf pip3 /usr/bin/pip

# Baixa o repositorio
git clone https://github.com/Nok-Tech/nok-dns.git /opt/nok-dns

# Navega para o diretório do repositório
cd /opt/nok-dns

# Instala as dependências com pyproject.toml
python3 -m pip install .
