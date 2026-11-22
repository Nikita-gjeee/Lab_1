# logic.py

notes = []  # список записей в памяти

def add_note(text):
    notes.append(text)

def get_notes():
    return notes