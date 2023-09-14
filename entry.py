import datetime


class Entry:
    count = -1

    def __init__(self, id_entry=None,  title_entry=None, body_entry=None, data_entry=None):
        self.title_entry = title_entry
        self.body_entry = body_entry
        # self.data_entry = str(datetime.datetime.today())
        self.data_entry = data_entry
        if id_entry == None:
            Entry.count += 1
            self.id_entry = str(Entry.count)
        else:
            self.id_entry = id_entry
        # Entry.count += 1
        # self.id_entry = str(Entry.count)

    def get_id_entry(self):
        return self.id_entry

    def set_id_entry(self, id_entry):
        self.id_entry = id_entry

    def get_title_entry(self):
        return self.title_entry

    def set_title_entry(self, title_entry):
        self.title_entry = title_entry

    def get_body_entry(self):
        return self.body_entry

    def set_body_entry(self, body_entry):
        self.body_entry = body_entry

    def get_data_entry(self):
        return self.data_entry

    def set_data_entry(self, data_entry):
        self.data_entry = data_entry




