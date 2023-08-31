import json

import textNotes


def save_notes(notes: list):
    # Сохранение записи в файл
    json_list = []
    for item in notes:
        json_list.append(f"{item.id_entry};{item.title_entry};{item.body_entry};{item.data_entry}")
    filename = textNotes.path
    with open(filename, "w") as f:
        json.dump(json_list, f, indent=4)
