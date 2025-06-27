from src.api.hh_api import HeadHunterAPI
from src.models.vacancy import Vacancy
from src.storage.json_saver import JSONSaver

def user_interaction():
    hh_api = HeadHunterAPI()
    saver = JSONSaver()

    keyword = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество топ-вакансий: "))
    filter_words = input("Ключевые слова для фильтрации: ").lower().split()

    data = hh_api.get_vacancies(keyword)
    vacancies = Vacancy.cast_to_object_list(data)

    filtered = [v for v in vacancies if any(word in v.description.lower() for word in filter_words)]
    top = sorted(filtered, reverse=True)[:top_n]

    for v in top:
        print(v)
        saver.add_vacancy(v)

if __name__ == "__main__":
    user_interaction()
