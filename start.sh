#!/bin/bash

chmod +x "$0"

SCRIPT="script_to_generate_schedule.py"

chmod +x "$SCRIPT"

echo "Baixando input.txt da branch main do repositório..."
wget -q --show-progress -O input.txt https://raw.githubusercontent.com/luk-z0/HolyricsScheduler/main/input.txt

python3 "$SCRIPT"

echo "Script executado. Verifique o arquivo gerado."