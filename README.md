---
Um gerenciador de conexões estilo ddns, porem com foco em atualização de um dns para dominios na cloudflare com base em api e zona para ambientes onde o ip é dinamico ou rotativo, mantendo assim o dns local atualizado com o ip obtido pelo ambiente onde o agente vai rodar.
---

# Requisitos

- Python 3.14.2 ou superior
- Pip 24.0 ou superior

# Instalação

## Instale as dependências necessarias
```bash
apk add --no-cache bash curl
```

## Baixe o script de instalação:

```bash
curl -fsSL "https://raw.githubusercontent.com/Nok-Tech/nok-dns/refs/heads/main/install.sh" -o install.sh
```

## Dê permissão de execução ao script:

```bash
chmod +x install.sh
```

## Execute o script de instalação:

```bash
sh install.sh
```

# Executa a aplicação
```bash
python3 -m nok-dns
```