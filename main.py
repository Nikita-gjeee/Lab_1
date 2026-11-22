# main.py
import menu
import logic
#КОМЕНТ ДЛЯ ВЕТКИ MERGE
def main():
    while True:
        menu.show_menu()
        choice = menu.get_choice()

        if choice == "1":
            text = input("Введите текст: ")
            if text.strip():
                logic.add_note(text)
                print("Добавлено!")
            else:
                print("Пусто — не добавлено.")

        elif choice == "2":
            notes = logic.get_notes()
            if not notes:
                print("\nЗаписей нет.")
            else:
                print("\n--- ВСЕ ЗАПИСИ ---")
                for i, note in enumerate(notes, 1):
                    print(f"{i}. {note}")

        elif choice == "3":
            print("Выход. Всё забыто.")
            break
        else:
            print("Неверный ввод.")

if __name__ == "__main__":
    main()