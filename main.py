from src.api.hh_api import HHAPI
from src.files.json_file import JSONFileHandler


def user_interface():
    """
    Консольный интерфейс взаимодействия с пользователем.
    Позволяет искать вакансии, сохранять их и просматривать.
    """
    api = HHAPI()
    file_handler = JSONFileHandler()  # можно передать имя файла, если нужно

    while True:
        print("\nВыберите действие:")
        print("1 — Найти вакансии")
        print("2 — Показать сохранённые вакансии")
        print("3 — Удалить вакансию по URL")
        print("4 — Выход")

        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            keyword = input("Введите ключевое слово для поиска: ").strip()
            vacancies = api.get_vacancies(keyword)
            if not vacancies:
                print("Ничего не найдено.")
                continue

            print(f"\nНайдено {len(vacancies)} вакансий:")
            for i, vac in enumerate(vacancies, 1):
                print(f"{i}. {vac.title} | {vac.company} | {vac.salary} руб.")
                print(f"   {vac.url}")

            save = input("Сохранить найденные вакансии в файл? (да/нет): ").lower()
            if save in ("да", "y", "yes"):
                file_handler.add_data([v.to_dict() for v in vacancies])
                print("Вакансии сохранены.")

        elif choice == "2":
            saved = file_handler.read_data()
            if not saved:
                print("Файл пуст.")
                continue

            print("\nСохранённые вакансии:")
            for i, vac in enumerate(saved, 1):
                print(f"{i}. {vac['title']} | {vac['company']} | {vac['salary']} руб.")
                print(f"   {vac['url']}")

        elif choice == "3":
            url = input("Введите URL вакансии для удаления: ").strip()
            file_handler.remove_data(url)
            print("Удаление завершено (если вакансия была — удалена).")

        elif choice == "4":
            print("До свидания!")
            break

        else:
            print("Неверный ввод. Пожалуйста, выберите пункт от 1 до 4.")


if __name__ == "__main__":
    user_interface()
