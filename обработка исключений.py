def string_to_ins(s):
    try:
        return int(s)
    except ValueError:
        return f"Ошибка: невозможно преобразовать '{s}' в целое число"


def read_file(filename):
    try:
        with open(filename, 'r') as file: return file.read()
    except FileNotFoundError:
        return f"ошибка: файл '{filename}' не найден"
    except IOError:
        return f"ошибка ввода/вывода при работе с файлом '{filename}"


def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "ошибка: деление на ноль"
    except TypeError:
        return "ошибка: аргументы должы быть числами"


def access_list_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return f"ошибка: индекс {index} вне диапозона списка"
    except TypeError:
        return "ошибка: индекс должен быть целым числом"
