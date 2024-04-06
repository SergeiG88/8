def print_params(a = 1, b = 'строка', c = True, x = 12, y = 'qwer', z = 10):
    return(a, b, c, x, y, z)
values_list = [1, 'строка', True]
#values_list_2_ = [2, 42]
values_dict = {'x': 12, 'y': 'qwer', 'z': 10}
param = print_params(*values_list, *values_list_2_, **values_dict)
print(param)