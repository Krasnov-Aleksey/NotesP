from notes_dict import NotesDict

notes_dict = NotesDict()


def add_entry_pr(tittle_entry, bode_entry):
    notes_dict.add_entry(tittle_entry, bode_entry)


def editing_entry_pr(id_entry, title_entry, body_entry):
    bol = notes_dict.editing_entry(id_entry, title_entry, body_entry)
    return bol


def delete_entry_pr(id_entry):
    bol = notes_dict.delete_entry(id_entry)
    return bol


def get_notes_dict_pr():
    return notes_dict.get_note_dict()


def load_file_pr(path):
    bol = notes_dict.load_notes(path)
    return bol


def save_file_pr(path):
    notes_dict.save_notes(path)
