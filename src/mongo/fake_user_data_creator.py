from datetime import datetime

users_data = [
    {
        'user_name': 'David',
        'password': '1234',
        'email': 'ggg@gmail.com',
        'phone_number': '0551231234',
        'id_number': '222222222',
        'created_at': datetime(2023, 4, 10),
        'companies': ['lizCafeteria_2023-04-10 00:00:00', 'coffee_nyc_2023-04-10 00:00:00'],
    },
    {
        'user_name': 'Roey',
        'password': '1234',
        'email': 'ggg@gmail.com',
        'phone_number': '0551231234',
        'id_number': '222222222',
        'created_at': datetime(2023, 4, 10),
        'companies': ['lizCafeteria_2023-04-10 00:00:00'],
    },
    {
        'user_name': 'Roni',
        'password': '1234',
        'email': 'ggg@gmail.com',
        'phone_number': '0551231234',
        'id_number': '222222222',
        'created_at': datetime(2023, 4, 10),
        'companies': ['lizCafeteria_2023-04-10 00:00:00', 'coffee_nyc_2023-04-10 00:00:00'],
    },
]

def create_users_array():
    users_array = []

    for user in users_data:
        users_array.append({
            **user,
            '_id': user['user_name'] + '_' + user['id_number'],
        })

    return users_array
