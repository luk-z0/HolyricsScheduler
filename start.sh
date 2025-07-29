#!/bin/bash

chmod +x "$0"

SCRIPT="script_to_generate_schedule.py"

chmod +x "$SCRIPT"

python3 "$SCRIPT"

echo "Script executado. Verifique o arquivo gerado."