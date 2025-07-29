# README - Script de Geração de Programação de Culto

Este projeto contém um script Python para gerar a programação de culto em formato `.txt`, a partir de um arquivo `input.txt` com dados de músicas, versículos e informações do culto. Além disso, inclui um script Bash para facilitar a execução.

---

## Requisitos

* Python 3.6 ou superior

* Biblioteca `requests` instalada
  Para instalar, rode no terminal:

  ```bash
  pip install requests
  ```

* Sistema operacional Linux (testado em Ubuntu, Pop!_OS e similares)

---

## Arquivos

* `script_to_generate_schedule.py`: Script Python principal que lê o `input.txt`, busca versículos na API e gera o arquivo `programacao_culto.txt`.
* `rodar_programacao.sh`: Script Bash para rodar o script Python facilmente.
* `input.txt`: Arquivo de entrada que deve conter os dados do culto.

---

## Como usar

1. **Prepare o arquivo `input.txt`** na mesma pasta, seguindo o formato esperado (exemplo disponível no projeto).

2. **Dê permissão para executar o script bash** (apenas na primeira vez):

   ```bash
   chmod +x start.sh
   ```

3. **Execute o script bash para gerar a programação:**

   ```bash
   ./start.sh
   ```

4. Após a execução, o arquivo `generated_schedule.txt` será gerado na mesma pasta.

---

## Observações

* O script Python depende de conexão com a internet para buscar os versículos na [Bible API](https://bible-api.com/).
* Caso deseje alterar o nome do arquivo de saída ou o caminho, modifique a variável `program_output_path` dentro do script Python.
* Certifique-se que o diretório possui permissões de leitura e escrita para o usuário que está executando os scripts.

---

## Exemplo de entrada `input.txt`

```
DATA: 29/07/2025
BOAS_VINDAS: Pr. Elenildo
DIRIGENTE: Ir. Carlos
PRELUDIO: Minis. de Louvor
MOMENTO_INTERCESSAO: Momento de oração pelos irmãos
OPORTUNIDADES: Ir. Lucas, JUBASCC, Dcª. Conceição
DIZIMOS: Dc. Manoel
MENSAGEM_BIBLICA: Tema: A fé que salva

VERSICULOS:
Livro: Salmos
Capitulo: 136

Dirigente:1
Igreja:2
Dirigente:3
Igreja:4
Todos:26
```

## Exemplo de saída `generated_schedule.txt`

```
Data: @dia/mês/ano
Boas Vindas: Pr. Elenildo
Dirigente: Ir. Carlos
Prelúdio: Minis. de Louvor
Leitura Bíblica Alternada

Leitura Bíblica Alternada
Salmos 136: 1 - 26

Dirigente:
1. Dai graças ao Senhor, porque ele é bom; porque a sua benignidade dura para sempre.

Igreja:
2. Dai graças ao Deus dos deuses, porque a sua benignidade dura para sempre

Dirigente:
3. Dai graças ao Senhor dos senhores, porque a sua benignidade dura para sempre;

Igreja:
4. ao único que faz grandes maravilhas, porque a sua benignidade dura para sempre;

Todos: Todos:
26. Dai graças ao Deus dos céus, porque a sua benignidade dura para sempre.

Momento de Intercessão
Dc. Eduardo

Oportunidades
- Ir. Lucas
- JUBASCC
- Dcª. Conceição

Dízimos e Ofertas
Dc. João

Momento de Louvor

Mensagem Bíblica


Considerações Finais

Avisos
```
### Importe no Holyrics 

```
Música>Importar>Outros>TXT File
```

---

Pode usar a vontade!

---
