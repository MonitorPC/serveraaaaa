from flask import Flask
from data import db_session
from data import users
from users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.sqlite")
    user = User()
    user.surname = 'Scott'
    user.name = 'Ridley'
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'

    session = db_session.create_session()
    session.add(user)
    session.commit()

    user.surname = 'Riple'
    user.name = 'Alen'
    user.age = 27
    user.position = 'engineer'
    user.speciality = 'engineer'
    user.address = 'module_7'
    user.email = 'Ailien@mars.org'

    session = db_session.create_session()
    session.add(user)
    session.commit()

    user.surname = 'Busurman'
    user.name = 'Raile'
    user.age = 18
    user.position = 'doctor'
    user.speciality = 'surgeon'
    user.address = 'module_3'
    user.email = 'Chumnoy_doctor@mars.org'

    session = db_session.create_session()
    session.add(user)
    session.commit()

    app.run()


if __name__ == '__main__':
    main()
