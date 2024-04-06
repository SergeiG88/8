def print_params(a = 1, b = 25, c = 3):
    return(a, b, c)
some_dict = {'a': 1, 'b': 25, 'c': 3}
param = print_params(**some_dict)
#print_params(b=25)
#print_params(c=[1,2,3])
print(param)

