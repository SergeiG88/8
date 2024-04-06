#def print_params(a = 1, b = 'строка', c = True):
 #   return(a, b, c)
#some_list = [1, 'строка', True]
#param = print_params(*some_list)
#print(param)


#def print_params():
 #   print('print_params')



#def print_params(a = 1, b = 25, c = [1,2,3]):
 #   return(a, b, c)
#some_list = [1, 25, [1,2,3]]
#param = print_params(*some_list)
#print(param)



#def print_params(a, b, c):
 #   return(a, b, c)
#values_list = [1, 'строка']
#values_dict = {'c': 4}
#param = print_params(*values_list, **values_dict)
#print(param)



#def print_params(a, b, c):
 #   return(a, b, c)
#values_list_2 = [2, 'строка']
#param = print_params(*values_list_2, 42)
#print(param)



def test(a = 1, b = 25, c = 3):
    return(a, b, c)
games_list = [1, 25, 3]
test2 = test(*games_list)
print(test2)




