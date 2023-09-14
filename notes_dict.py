import datetime
import json

from entry import Entry


class NotesDict:
    def __init__(self):
        self.notes_dict = {}

    def add_entry(self, title_entry, body_entry):
        # Добавить в словарь
        en = Entry(title_entry=title_entry, body_entry=body_entry)
        en.data_entry = str(datetime.datetime.today().strftime("%d.%m.%Y"))
        key_entry = 0
        for key in self.notes_dict.keys():
            key_entry = int(key)+1
        en.id_entry = str(key_entry)
        self.notes_dict[en.id_entry] = [en.title_entry, en.body_entry, en.data_entry]

    def load_notes(self, path):
        try:
            with open(path, "r", encoding="UTF-8") as f:
                json_read: dict = json.load(f)
            self.notes_dict = json_read
            return True
        except FileNotFoundError:
            return False

    def save_notes(self, path):
        # Сохранение записи в файл
        with open(path, "w", encoding="UTF-8") as f:
            json.dump(self.notes_dict, f, indent=4, ensure_ascii=False)

    def editing_entry(self, id_entry, title_entry, body_entry):
        # Редактировать словарь
        for key in self.notes_dict.keys():
            if key == id_entry:
                self.notes_dict[id_entry] = [title_entry, body_entry,
                                             str(datetime.datetime.today().strftime("%d.%m.%Y"))]
                return True

        return False

    def delete_entry(self, id_entry):
        # Удалить завись из словаря
        try:
            self.notes_dict.pop(id_entry)
            return True
        except:
            return False

    def get_note_dict(self):
        return self.notes_dict
