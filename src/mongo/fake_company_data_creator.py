from datetime import datetime

companies_data = [
    {
        'name': 'lizCafeteria',
        'password': '1234',
        'created_at': datetime(2023, 4, 10),
    },
    {
        'name': 'coffee_nyc',
        'password': '1234',
        'created_at': datetime(2023, 4, 10),
    },
    {
        'name': 'fake',
        'password': '1234',
        'created_at': datetime(2023, 4, 10),
    },
]

def create_companies_array():
    companies_array = []

    for company in companies_data:
        companies_array.append({
            **company,
            '_id': company['name'] + '_' + str(company['created_at']),
        })

    return companies_array
