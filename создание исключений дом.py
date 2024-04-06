# class InvalidDataException(Exception):
#     pass
#
# class ProcessingException(Exception):
#     pass
#
# try:
#     raise InvalidDataException('Сержант')
# except InvalidDataException as e:
#     print(f'Ошибка: {e}')
#     raise


#     raise ProcessingException('Воин проиграл')
# except ProcessingException as e:
#     print(f'Внимание: {e}')
# finally:
#     print('исключений не произошло')


# try:
#     x = 10 /0
# except ZeroDivisionError as e:
#     print(f'Это не будет напечатано: {e}')
#     raise


try:
    res = x / y
except NameError as e:
    print(f'Не правильно: {e}')

print('Штатное завершение')


# try:
#     res = x /y
# except NameError as e:
#     print(f'Не правильно: {e}')
# else:
#     print('ура')
# finally:
#     print('Исключений не произошло')

#print('Штатное завершение')
























#def InvalidDataException(Exception):
# try:
#     raise InvalidDataException('Рядовой Райн')
# except InvalidDataException as e:
#     print(f'Ошибка {e}')
#     raise
#
#
# def greet_person(person_name):
#     if person_name == 'Robert':
#         raise InvalidDataException('ты не нравишьсяя')
#     print(f'Привет {person_name}')


# class InvalidData(Exception):
#     pass
#
#     # def greet_person(person_name):
#     #     if person_name == 'Robert':
# try:0
#     raise InvalidData("We don't like you, Robert")
# except InvalidData as e:
#     print(f'Ошибка {e}')
#     raise


# try:
#     raise ProcessingException("We don't like you, Robert")
# except ProcessingException as e:
#     print(f'Внимание {e}')






















# class ProcessingException(Exception):
#
#     def greet_person(person_name):
#         if person_name == 'Robert':
#             try:
#                 raise ProcessingException("We don't like you, Robert")
#
#             except ProcessingException as e:
#                 print(f'Внимание; {e}')
                    #raise




# greet_person('Dolly')

