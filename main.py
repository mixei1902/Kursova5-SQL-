from src.config import config
from src.utils import get_vacancies, create_database, save_data_to_database, get_company


def main():
    employee_ids = [
        '2302207',  #
        '159880',  #
        '1102601',  #
        '1840223',  #
        '1641656',  #
        '1277564',  #
        '1228593',  #
        '9231282',  #
    ]
    params = config()
    company_list = get_company(employee_ids)
    vacansy_list = get_vacancies(employee_ids)
    create_database('hh_company', params=params)
    save_data_to_database(company_list, vacansy_list, 'hh_company', params)


if __name__ == '__main__':
    main()
