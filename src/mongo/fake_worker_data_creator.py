import random
from datetime import datetime, timedelta

workers_data = [
    {
        'user_name': 'David',
        'password': '1234',
        'name': 'דוד',
        'full_name': 'דוד',
        'id_number': '123456789',
        'phone_number': '0551231234',
        'date_of_birth': datetime(1998, 9, 3),
        'address': 'הרצל 13 רמת גן',
        'email': 'ggg@gmail.com',
        'marital_status': 'married',
        'children': 1,
        'role': 'אחמ"ש',
        'date_of_starting_work': datetime(2023, 2, 12),
        'work_status': 'active',
        'type_of_position': 'full_time',
        'hourly_wage': '70',
        'history': [
            {
                'date': datetime(2023, 2, 12),
                'role': 'מלצר',
                'hourly_wage': '45 + טיפים',
            },
            {
                'date': datetime(2023, 11, 1),
                'role': 'אחמ"ש',
                'hourly_wage': '70',
            },
        ],
        'created_at': datetime(2023, 2, 12),
        'work_grade': 9.2,
        'left_sick_days': 0,
        'entitled_sick_days': 0,
        'left_days_off': 0,
        'entitled_days_off': 0,
        'general_note': None,
        'note_history': None,
        'user_level': 'shiftManager',
    },
    {
        'user_name': 'Roey',
        'password': '1234',
        'name': 'רועי',
        'full_name': 'רועי אדם',
        'id_number': '123456788',
        'phone_number': '0551231233',
        'date_of_birth': datetime(2005, 7, 11),
        'address': 'לח"י 45 תל אביב',
        'email': 'roey@gmail.com',
        'marital_status': 'single',
        'children': None,
        'role': 'מלצר',
        'date_of_starting_work': datetime(2023, 4, 10),
        'work_status': 'active',
        'type_of_position': 'part_time',
        'hourly_wage': '45 + טיפים',
        'history': [
            {
                'date': datetime(2023, 4, 10),
                'type_of_position': 'full_time',
                'hourly_wage': '40 + טיפים',
            },
            {
                'date': datetime(2023, 7, 3),
                'type_of_position': 'part_time',
            },
            {
                'date': datetime(2023, 7, 5),
                'hourly_wage': '45 + טיפים',
            },
        ],
        'created_at': datetime(2023, 4, 10),
        'work_grade': 7.5,
        'left_sick_days': 0,
        'entitled_sick_days': 0,
        'left_days_off': 0,
        'entitled_days_off': 0,
        'general_note': 'לא עובד בימי ראשון',
        'note_history': [
            {
                'date': datetime(2023, 4, 10),
                'commenter': 'user_name',
                'note': 'עובד טוב!!!',
            },
            {
                'date': datetime(2023, 4, 1),
                'commenter': 'user_name',
                'note': 'התלוננו עליו שהוא ...',
            },
            {
                'date': datetime(2023, 4, 10),
                'commenter': 'דוד',
                'note': 'הוא רב עם עידו באמצע המשמרת',
            },
        ],
        'user_level': 'worker',
    },
    {
        'user_name': 'Roni',
        'password': '1234',
        'name': 'רוני',
        'full_name': 'רוני ברדריק',
        'id_number': '222222222',
        'phone_number': '0525381648',
        'date_of_birth': datetime(1999, 1, 28),
        'address': 'הרצל 13 רמת גן',
        'email': 'roni@gmail.com',
        'marital_status': 'single',
        'children': None,
        'role': 'businessOwner',
        'date_of_starting_work': datetime(2023, 2, 12),
        'work_status': 'active',
        'type_of_position': 'full_time',
        'hourly_wage': '70',
        'history': None,
        'created_at': datetime(2023, 2, 12),
        'work_grade': 9.2,
        'left_sick_days': 0,
        'entitled_sick_days': 0,
        'left_days_off': 0,
        'entitled_days_off': 0,
        'general_note': None,
        'note_history': None,
        'user_level': 'businessOwner',
    },
]

def get_random_shifts(worker):
    date_array = []
    current_date = worker['date_of_starting_work']
    end_date = datetime.now()

    while current_date < end_date:
        # Find the year in the date_array
        year_data = next((y for y in date_array if y['year'] == current_date.year), None)
        if not year_data:
            year_data = {'year': current_date.year, 'months': []}
            date_array.append(year_data)

        # Find the month in the year_data
        month_data = next((m for m in year_data['months'] if m['month_num'] == current_date.month), None)
        if not month_data:
            month_data = {
                'month_name': current_date.strftime('%B'),
                'month_num': current_date.month,
                'shifts': []
            }
            year_data['months'].append(month_data)

        # Generate a random start time between 07:00 and 19:00 (with random minutes)
        start_hour = random.randint(7, 19)
        start_minute = random.randint(0, 59)
        shift_start = datetime(
            current_date.year,
            current_date.month,
            current_date.day,
            start_hour,
            start_minute
        )

        # Generate a random duration between 4 and 8 hours
        shift_duration_hours = random.randint(4, 8)
        shift_duration_minutes = random.randint(0, 59)
        shift_end = shift_start + timedelta(hours=shift_duration_hours, minutes=shift_duration_minutes)

        # Ensure the shift doesn't end after midnight
        if shift_end.hour > 23 or (shift_end.hour == 23 and shift_end.minute > 0):
            shift_end = shift_start.replace(hour=23, minute=0)  # Shift end at 23:00 if it exceeds midnight

        total_time = shift_end - shift_start
        
        # Create the shift
        shift = {
            'start': shift_start,
            'end': shift_end,
            'total_time': str(total_time),
        }
        month_data['shifts'].append(shift)

        # Add a random gap between shifts (1 to 4 days)
        next_shift_gap = random.randint(1, 4)
        current_date += timedelta(days=next_shift_gap)

    return date_array

def create_workers_array():
    workers_array = []

    for worker in workers_data:
        workers_array.append({
            **worker,  # Unpacking the worker dictionary
            '_id': worker['user_name'] + '_' + worker['id_number'],
            'shifts': get_random_shifts(worker),
        })

    return workers_array

# # Example usage
# workers_array = create_workers_array()
# for worker in workers_array:
#     print(worker)
