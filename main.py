from src.config import config
from src.utils import get_vacancies, create_database, save_data_to_database, get_company


def main():
    employee_ids = [
        '1400150',  # Газпром
        '1740',  # яндекс
        '15478',  # ВК
        '1373',  # Аэрофлот
        '4181',  # ВТБ
        '78638',  # Тинькофф
        '2733062',  # Лина Цифровой Экономики
        '3095',  # Инфосистемы Джет
        '5060211',  # Группа Астра
        '4837406'  # Centicore
    ]
    params = config()
    company_list = get_company(employee_ids)
    vacansy_list = get_vacancies(employee_ids)
    create_database('hh_company', params=params)
    save_data_to_database(company_list, vacansy_list, 'hh_company', params)


if __name__ == '__main__':
    main()
