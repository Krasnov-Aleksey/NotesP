import datetime
import textNotes
from entry import Entry
import json


class Notes:

    def __init__(self):
        self.notes_list = []

    def get_notes_list(self):
        return self.notes_list

    def save_notes(self):
        # Сохранение записи в файл
        json_list = []
        for item in self.notes_list:
            json_list.append(f"{item.id_entry};{item.title_entry};{item.body_entry};{item.data_entry}")
        # TODO  убрать в отдельный класс
        filename = textNotes.path
        with open(filename, "w") as f:
            json.dump(json_list, f, indent=4)

    def load_notes(self):
        # Чтение заметки из файла
        # TODO добавить исключение, убрать в отдельный класс
        # TODO если сначала добавляешь а потом загружаешь id не меняется поправить
        filename = textNotes.path
        with open(filename, "r") as f:
            json_read = json.load(f)

        json_list: list = list(json_read)

        for i in range(0, len(json_list)):
            json_str: str = json_list[i]
            new_json_list: list = json_str.split(";")
            en = Entry()
            en.id_entry = new_json_list[0]
            en.title_entry = new_json_list[1]
            en.body_entry = new_json_list[2]
            en.data_entry = new_json_list[3]
            self.notes_list.append(en)

    def add_entry(self, title_entry, body_entry):
        # Добавление записи в лист
        en = Entry()
        en.set_title_entry(title_entry)
        en.set_body_entry(body_entry)
        en.set_data_entry(str(datetime.datetime.today()))
        self.notes_list.append(en)
        if Notes.check_id(self, en.get_id_entry()):
            # Если id уже есть ищет максимальную id и добавляет id+1
            max_id = 0
            for item in self.notes_list:
                if max_id < int(item.id_entry):
                    max_id = int(item.id_entry)
            en.set_id_entry(max_id+1)

    def editing_entry(self, id_entry, title_entry, body_entry):
        # Редактирование записи
        # TODO убрать print
        for i in range(0, len(self.notes_list)):
            item = self.notes_list[i]
            if id_entry == item.id_entry:
                en = Entry()
                en.set_id_entry(id_entry)
                en.set_title_entry(title_entry)
                en.set_body_entry(body_entry)
                en.set_data_entry(str(datetime.datetime.today()))

                self.notes_list.pop(i)
                self.notes_list.insert(i, en)
                return
        print(textNotes.id_not_found)

    def delete_entry(self, id_entry):
        # Удаление записи
        for i in range(0, len(self.notes_list)):
            item = self.notes_list[i]
            if id_entry == int(item.id_entry):
                self.notes_list.pop(i)
                return
        print(textNotes.id_not_found)

    def print_entry(self):
        # Вывод всех записей
        for item in self.notes_list:
            # TODO убрать print сделать return вывод убрать в view
            print(item.id_entry, item.title_entry, item.body_entry, item.data_entry)

    def print_entry_id(self, id_entry):
        # Вывод записи по id
        # TODO убрать Print сделать return вывод убрать в view
        for item in self.notes_list:
            if id_entry == item.id_entry:
                return print(item.id_entry, item.title_entry, item.body_entry, item.data_entry)
        print("Запись не найдена")

    def print_entry_data(self, data):
        # Вывод записи по дате
        # TODO убрать print добавить год и месяц вывод убрать в view
        count = 0
        for item in self.notes_list:
            new_data = datetime.datetime.strptime(item.data_entry, "%Y-%m-%d %H:%M:%S.%f")
            if data == new_data.day:
                print(item.title_entry)
                count += 1

        if count == 0:
            print("Запись не найдена")

    def check_id(self, id_entry):
        # Проверка на id есть или нет
        for item in self.notes_list:
            if item.id_entry == id_entry:
                return True
        return False
