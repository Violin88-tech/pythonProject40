import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    user_email: str
    user_gender: str
    user_phone_number: str
    month: str
    year: str
    day: str
    user_subject: str
    user_hobby: str
    user_picture: str
    user_current_address: str
    user_state: str
    user_city: str


test_user = User(
    first_name='Vika',
    last_name='Islenteva',
    user_email='email@gmail.com',
    user_gender='Female',
    user_phone_number='9920454526',
    month='June',
    year='2003',
    day='03',
    user_subject='Economics',
    user_hobby='Sports',
    user_picture='photo.jpg',
    user_current_address='Artistic driveway 4, sq.1',
    user_state='NCR',
    user_city='Noida',
)
