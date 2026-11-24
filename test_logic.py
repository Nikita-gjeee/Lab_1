# test_logic.py
import logic  # Импортируем наш модуль, который тестируем

# --- Тест 1: пустой список ---
def test_notes_start_empty():
    logic.notes.clear()           # Очищаем список перед тестом
    assert logic.get_notes() == []  # Проверяем, что он пуст

# --- Тест 2: добавление одной записи ---
def test_add_single_note():
    logic.notes.clear()
    logic.add_note("Купить хлеб")
    assert len(logic.get_notes()) == 1
    assert logic.get_notes()[0] == "Купить хлеб"

# --- Тест 3: добавление нескольких записей ---
def test_add_multiple_notes():
    logic.notes.clear()
    logic.add_note("Первая")
    logic.add_note("Вторая")
    assert len(logic.get_notes()) == 2
    assert logic.get_notes() == ["Первая", "Вторая"]

def test_search_notes():
    logic.notes.clear()
    logic.add_note("Купить молоко")
    logic.add_note("Покормить кота")
    
    # Ищем "молоко"
    results = logic.search_notes("молоко")
    assert len(results) == 1
    assert results[0] == "Купить молоко"
