from src.api import HeadHunterApi
from src.DBManager import DBManager
from src.interface import create_db, save_to_db
from src.vacancies import Vacancy

companies_id = [
    "9140614",
    "8639172",
    "988247",
    "5912899",
    "11456714",
    "2439690",
    "5173502",
    "4204313",
    "10819001",
    "11028611",
]


def main():
    vacancies = HeadHunterApi(companies_id)
    if vacancies.get_vacancies() != [[]]:
        user_input = input("Введите ключевое слово для поиска вакансий: ")
        for vacancy in vacancies.get_vacancies()[0]:
            vac = Vacancy(vacancy)
            create_db("HHApi")
            save_to_db("HHApi", vac)
        DBMan = DBManager("HHApi", "postgres", "5893", "localhost")
        companies_and_vacancies_count = DBMan.get_companies_and_vacancies_count()
        all_vacancies = DBMan.get_all_vacancies()
        avg_salary = DBMan.get_avg_salary()
        vacancies_with_higher_salary = DBMan.get_vacancies_with_higher_salary()
        vacancies_with_keyword = DBMan.get_vacancies_with_keyword(user_input)

        print(
            f"""Компании и их количество вакансий: {companies_and_vacancies_count}
        Все вакансии: {all_vacancies}
        Средняя зарплата по вакансиям: {avg_salary}
        Вакансии с зарплатой выше среднего: {vacancies_with_higher_salary}
        Вакансии с ключевым словом в названии {vacancies_with_keyword}"""
        )


if __name__ == "__main__":
    main()
