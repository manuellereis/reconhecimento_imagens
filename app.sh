#!/bin/bash

# Verifica se o ambiente virtual existe
if [ -d "venv" ]; then
    echo "\e[34m----------------------- Instalando Dependências do Sistema -----------------------\e[0m"
    
    sudo apt update
    sudo apt install -y libgl1 libglib2.0-0 build-essential cmake libdlib-dev libboost-all-dev \
        libopenblas-dev liblapack-dev libx11-dev python3-dev python3-pip

    echo "\e[34m----------------------- Ativando Ambiente Virtual -----------------------\e[0m"
    . venv/bin/activate || {
        echo "\e[31m[ERRO] Falha ao ativar o ambiente virtual.\e[0m"
        exit 1
    }

    echo "\e[34m----------------------- Instalando Dependências do Projeto -----------------------\e[0m"

    if uv pip install .; then
        clear

        echo "\e[32m[SUCESSO] Ambiente virtual ativado com sucesso.\e[0m"
        echo "\e[32m[SUCESSO] Dependências do sistema instaladas com sucesso.\e[0m"

        python3 scripts/recognition.py &

        echo "\e[32m[SUCESSO] Script de reconhecimento facial iniciado.\e[0m"

        # Banner
        echo "\e[1;30m██████╗  ██╗     "
        echo "\e[1;30m██╔══██╗ ██║     "
        echo "\e[1;30m██████╔╝ ██║     "
        echo "\e[1;30m██╔══██╗ ██║     "
        echo "\e[1;30m██████╔╝ ███████╗"
        echo "\e[1;30m╚═════╝  ╚══════╝"
        echo "BLACKLISTX — Segurança em primeiro lugar 🛡️\e[0m"

        wait  # Aguarda processos em background terminarem
    else
        echo "\e[31m[ERRO] Falha ao instalar dependências do projeto.\e[0m"
        exit 1
    fi

else
    echo "\e[31m[ERRO] O ambiente virtual 'venv' não foi encontrado. Execute: python3 -m venv venv\e[0m"
    exit 1
fi
