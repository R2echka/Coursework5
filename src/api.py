import requests


class HeadHunterApi:
    """Класс для работы с апи hh.ru"""

    def __init__(self, companies):
        self.companies = companies
        self.url = "https://api.hh.ru/vacancies"
        self.params = {"employer_id": companies}
        self.vacancies = []

    def get_api(self):
        return requests.get(self.url, params=self.params)

    def get_vacancies(self):
        response = self.get_api()
        if response.status_code == 200:
            data = response.json()
            vacancies = data.get("items")
            self.vacancies.append(vacancies)
            return self.vacancies
        else:
            return []
