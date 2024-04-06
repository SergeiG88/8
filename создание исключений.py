# def greet_person(person_name):
#     if person_name == 'Robert':
#         # Создаем объект исключения и райзим его
#         raise BaseException("We don't like you, Robert")
#     print(f'Hi there {person_name}')
#
greet_person('Dolly')
#greet_person('Robert')


try:0
    raise NameError('Привет Там')
except NameError as exc:
    print(f'Исключение типа {type(exc)} пролетало мимо! его параметры {exc.args}')
    # Обратите внимание на "пустой" оператор - будет переброшенно исключение текущего скоупа
    raise


# try:
#     raise NameError('Привет Там')
# except NameError as exc:
#     print(f'Исключение типа {type(exc)}')
#     raise TypeError('Привет и тут')


# class HerrDiedError(Exception):
#     pass
#
#
# class GameOverError(Exception):
#     pass
#
# try:
#     raise HerrDiedError('Рядовой Райн')
# except HerrDiedError as exc:
#     print(f'Поймано исключение {exc}')
#     raise GameOverError('Миссия провалена')