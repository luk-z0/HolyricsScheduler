import requests


def parse_metadata(lines):
    metadata = {
        "date": "",
        "welcome_pastor": "",
        "dirigente": "",
        "prelude": "",
        "intercession_moment": "",
        "opportunities": [],
        "deacon": "",
        "biblical_message": "",
        "musics": [],
    }
    for line in lines:
        if line.startswith("DATA:"):
            metadata["date"] = line.split("DATA:", 1)[1].strip()
        elif line.startswith("BOAS_VINDAS:"):
            metadata["welcome_pastor"] = line.split("BOAS_VINDAS:", 1)[1].strip()
        elif line.startswith("DIRIGENTE:"):
            metadata["dirigente"] = line.split("DIRIGENTE:", 1)[1].strip()
        elif line.startswith("PRELUDIO:"):
            metadata["prelude"] = line.split("PRELUDIO:", 1)[1].strip()
        elif line.startswith("MOMENTO_INTERCESSAO:"):
            metadata["intercession_moment"] = line.split("MOMENTO_INTERCESSAO:", 1)[
                1
            ].strip()
        elif line.startswith("OPORTUNIDADES:"):
            ops_str = line.split("OPORTUNIDADES:", 1)[1].strip()
            metadata["opportunities"] = [
                op.strip() for op in ops_str.split(",") if op.strip()
            ]
        elif line.startswith("DIZIMOS:"):
            metadata["deacon"] = line.split("DIZIMOS:", 1)[1].strip()
        elif line.startswith("MENSAGEM_BIBLICA:"):
            metadata["biblical_message"] = line.split("MENSAGEM_BIBLICA:", 1)[1].strip()
        elif line.startswith("MUSICAS:"):
            ops_str = line.split("MUSICAS:", 1)[1].strip()
            metadata["musics"] = [op.strip() for op in ops_str.split(",") if op.strip()]
    return metadata


def read_input_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    metadata_lines = []
    music_lines = []
    verses_lines = []

    section = "metadata"
    for line in lines:
        stripped = line.strip()
        if stripped == "MUSICAS:":
            section = "musics"
            continue
        elif stripped == "VERSICULOS:":
            section = "verses"
            continue
        if section == "metadata":
            metadata_lines.append(stripped)
        elif section == "musics":
            music_lines.append(stripped)
        elif section == "verses":
            verses_lines.append(stripped)

    metadata = parse_metadata(metadata_lines)

    songs = []
    for line in music_lines:
        if line and line[0].isdigit():
            parts = line.split(". ", 1)
            if len(parts) == 2:
                songs.append(parts[1])

    if len(verses_lines) < 2:
        raise ValueError("Invalid format in VERSICULOS section")

    book = verses_lines[0].replace("Livro:", "").strip()
    chapter = verses_lines[1].replace("Capitulo:", "").strip()

    verse_entries = []
    for ref in verses_lines[2:]:
        if not ref.strip():
            continue
        role, number = ref.split(":")
        verse_entries.append((role.strip(), number.strip()))

    return metadata, songs, book, chapter, verse_entries


def fetch_verse(book, chapter, verse):
    reference = f"{book} {chapter}:{verse}"
    url = f"https://bible-api.com/{reference}?translation=almeida"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("text", "").strip()
    else:
        return "[Error fetching verse]"


def generate_file(metadata, book, chapter, verse_entries):
    verse_numbers = [int(v[1]) for v in verse_entries]
    first_verse = min(verse_numbers)
    last_verse = max(verse_numbers)

    leitura_biblica_header = f"{book} {chapter}: {first_verse} - {last_verse}"

    alternated_lines = []
    todos_line = None

    for role, num in verse_entries:
        verse_text = fetch_verse(book, chapter, num)
        line = f"{num}. {verse_text}"

        if role.lower() == "todos":
            todos_line = f"{role}:\n{num}. {verse_text}"
        else:
            alternated_lines.append(f"{role}:\n{num}. {verse_text}")

    leitura_alternada_text = "\n\n".join(alternated_lines)
    if todos_line:
        leitura_alternada_text += f"\n\nTodos: {todos_line}"

    oportunidades_text = "\n".join([f"- {o}" for o in metadata["opportunities"]])

    program_text = f"""
Data: @dia/mês/ano
Boas Vindas: {metadata["welcome_pastor"]}
Dirigente: {metadata["dirigente"]}
Prelúdio: {metadata["prelude"]}
//{metadata["musics"][0]}
Leitura Bíblica Alternada

Leitura Bíblica Alternada
{leitura_biblica_header}

{leitura_alternada_text}

Momento de Intercessão
{metadata["intercession_moment"]}

Oportunidades
{oportunidades_text}

Dízimos e Ofertas
{metadata["deacon"]}

Momento de Louvor
"""

    for music in metadata["musics"][1:]:
        program_text += f"//{music}\n"

    program_text += f"""

Mensagem Bíblica
{metadata["biblical_message"] if metadata["biblical_message"] else ""}

Considerações Finais

Avisos
"""

    return program_text.strip()


def main():
    input_path = "input.txt"
    program_output_path = "generated_schedule.txt"

    try:
        metadata, songs, book, chapter, verse_entries = read_input_file(input_path)
    except Exception as e:
        print(f"Error reading input file: {e}")
        return

    program = generate_file(metadata, book, chapter, verse_entries)

    with open(program_output_path, "w", encoding="utf-8") as f:
        f.write(program)

    print(f"Programação do culto salva em '{program_output_path}'")


if __name__ == "__main__":
    main()
