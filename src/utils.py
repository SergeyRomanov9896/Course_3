import json


def get_vacancies(path: str) -> list[dict]:
    """
    Возвращает данные по вакансиям hh.ru
        path: Путь к файлу data/hh_vacancies.json
    """
    with open(path, encoding="UTF-8") as file:
        data = json.load(file)
        return data.get("items", [])


def get_unique_companies(vacancies) -> list[dict]:

    companies = {}

    for vacancy in vacancies:
        employer = vacancy["employer"]
        employer_id = employer["id"]

        companies[employer_id] = {
            "id": employer_id,
            "name": employer["name"],
            "alternate_url": employer["alternate_url"],
        }
    return list(companies.values())


if __name__ == "__main__":
    tap = ()

    vacanci = get_vacancies("data/hh_vacancies.json")
    unique_comp = get_unique_companies(vacanci)

    company = unique_comp[0]

    company_data = (
        company["id"],
        company["name"],
        company["alternate_url"],
    )
print(company_data)
