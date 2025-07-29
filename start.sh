#!/bin/bash

chmod +x "$0"

SCRIPT="script_to_generate_schedule.py"

chmod +x "$SCRIPT"

echo "Baixando input.txt da branch main do repositório..."
wget -q --show-progress -O input.txt https://raw.githubusercontent.com/luk-z0/HolyricsScheduler/main/input.txt

if [ -f "generated_schedule.txt" ]; then
    echo "O arquivo generated_schedule.txt existe."
    read -p "Deseja deletá-lo antes de continuar? (s/n) " response
    case "$response" in
        [Ss]* )
            rm -f generated_schedule.txt
            echo "Arquivo deletado."
            ;;
        * )
            echo "Arquivo mantido."
            ;;
    esac
fi

python3 "$SCRIPT"

echo "Script executado. Verifique o arquivo gerado."