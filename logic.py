# logic.py

notes = []  # список записей в памяти

def add_note(text):
    notes.append(text)

def get_notes():
    return notes

def search_notes(keyword):
    """Ищет записи, содержащие ключевое слово."""
    return [note for note in notes if keyword.lower() in note.lower()]