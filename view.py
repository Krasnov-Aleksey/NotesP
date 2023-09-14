import presenter
import textNotes


def print_entry_id(id_entry):
    # Вывод записи по ключу
    notes_dict = presenter.get_notes_dict_pr()
    for key, value in notes_dict.items():
        if key == id_entry:
            print(key, value)
            return
    print(textNotes.entry_not_found)


def print_entry_data(data):
    # Вывод записи по дате
    count = 0
    notes_dict = presenter.get_notes_dict_pr()
    for key, value in notes_dict.items():
        if data == value[2]:
            print(key, value)
            count += 1
    if count == 0:
        print(textNotes.entry_not_found)


def main_menu():
    print(textNotes.main_menu)
    flag = True
    while (flag):
        choice = input(textNotes.select_menu_item)
        match choice:
            case "1":
                title_entry = input(textNotes.enter_title_note)
                body_entry = input(textNotes.enter_note_text)
                presenter.add_entry_pr(title_entry, body_entry)
                print(textNotes.note_added)
            case "2":
                id_entry = input(textNotes.enter_note_id)
                title_entry = input(textNotes.enter_new_note_title)
                body_entry = input(textNotes.enter_new_note_text)
                presenter.editing_entry_pr(id_entry, title_entry, body_entry)
                print(textNotes.note_changed)
            case "3":
                id_entry = input(textNotes.select_note_id_to_delete)
                presenter.delete_entry_pr(id_entry)
                print(textNotes.note_deleted)
            case "4":
                notes_dict = presenter.get_notes_dict_pr()
                for item in notes_dict.items():
                    print(item)
            case "5":
                id_entry = input(textNotes.enter_note_id)
                print_entry_id(id_entry)
            case "6":
                data = input(textNotes.enter_the_date_note)
                print_entry_data(data)
            case "7":
                presenter.load_file_pr(textNotes.path)
                print(textNotes.notes_loaded)
            case "8":
                presenter.save_file_pr(textNotes.path)
                print(textNotes.notes_saved)
            case "9":
                flag = False
            case _:
                print(textNotes.enter_correct_menu_item)
