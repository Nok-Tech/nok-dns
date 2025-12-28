#!/bin/sh

set -eu

REPO_URL="${REPO_URL:-https://github.com/Nok-Tech/nok-dns.git}"
INSTALL_DIR="${INSTALL_DIR:-/opt/nok-dns}"

if ! command -v apk >/dev/null 2>&1; then
  echo "Este instalador suporta Alpine Linux (apk)." >&2
  exit 1
fi

apk add --no-cache python3 py3-pip git ca-certificates gcc musl-dev libffi-dev openssl-dev openssl python3-dev

python3 -m pip install -U pip >/dev/null 2>&1 || true

if [ -d "$INSTALL_DIR/.git" ]; then
  git -C "$INSTALL_DIR" remote set-url origin "$REPO_URL"
  GIT_TERMINAL_PROMPT=0 git -C "$INSTALL_DIR" pull --ff-only
else
  rm -rf "$INSTALL_DIR"
  GIT_TERMINAL_PROMPT=0 git clone --depth 1 "$REPO_URL" "$INSTALL_DIR"
fi

cd "$INSTALL_DIR"
python3 -m pip install .
