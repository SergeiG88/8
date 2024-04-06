import warnings

# def greet_person(person_name):
#     if person_name == 'Robert':
#         warnings.warn('Опять этот Роберт....')
#     print(f'Hi there {person_name}')


# greet_person('Robert')
# print('Выполнение продолжается')
# for i in range(10):
#     print(f'i={i}')


# def greet_person(person_name):
#     if person_name == 'Robert':
#         warnings.warn('Опять этот Роберт....')
#     print(f'Hi there {person_name}')
#
# # warnings.simplefilter('ignore')
# warnings.simplefilter('error')
#
# greet_person('Robert')
# try:
#     greet_person('Robert')
#     print('Выполнение продолжается')
# except RuntimeWarning:
#     print('Поймали RuntimeWarning!!!')
# for i in range(10):
#     print(f'i={i}')


import warnings

def function_with_warning():
    try:
        print("Перед генерацией предупреждения")
        warnings.warn("Это важное предупреждение", UserWarning)
        print("После генерации предупреждения")
    except UserWarning as e:
        print(f"Предупреждение было перехвачено как {e}")

print("Пример 1: Фильтр 'error'")
warnings.simplefilter("default", UserWarning)
function_with_warning()
print()

print("Пример 2: Фильтр 'default'")
warnings.simplefilter("default", UserWarning)
function_with_warning()

