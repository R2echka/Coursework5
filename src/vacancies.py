class Vacancy:
    """Класс вакансий, добавляемых из списка словарей"""

    def __init__(self, vacancy):
        self.name = vacancy["name"]
        if vacancy["salary"]:
            self.salary = vacancy["salary"]["from"]
        else:
            self.salary = None
        self.url = vacancy["url"]
        self.id = vacancy["id"]
        self.employer_name = vacancy["employer"]["name"]
        self.employer_id = vacancy["employer"]["id"]

    def __lt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary < other.salary
        else:
            print("Вы пытаетесь сравнить объекты разных классов")

    def __gt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary > other.salary
        else:
            print("Вы пытаетесь сравнить объекты разных классов")

    def __repr__(self):
        return f'{{"name": "{self.name}", "salary": {self.salary}, "url": "{self.url}"}}'
