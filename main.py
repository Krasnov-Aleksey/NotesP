import saveFile
from notes import Notes

notes1 = Notes()
# notes1.load_notes()
notes1.add_entry("Tittle0", "bode0")
notes1.add_entry("Tittle1", "bode1")
notes1.add_entry("Tittle2", "bode2")
notes1.print_entry()
# notes1.save_notes()
# notes1.editing_entry(3, "Tittle3","body3")
notes1.delete_entry(3)
print()
notes1.print_entry()
saveFile.save_notes(notes1.notes_list)



