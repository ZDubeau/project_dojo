# -------------- Project Dojo_Functions ---------------

# ------------ Algorithms using functions -------------

# _______________________________________________________________________________________
''' 1. Define a function that generate a tuple containing attribute names and call it '''

# Define a Tuple function


def my_tuple():
    string = 'item', 'price', 'brand', 'stock', 'categories'
    return string


string = my_tuple()
print(string)
# ____________________________________________________________________________________
''' 2. Define a function that take values as arguments and generate a tuple containing
    data values (corresponding to the previous attribute names), and call it '''

# 1st way


def tuple_list(*argument):
    ''' We can pass multiple arguments(*)
        in function without predetermining
        the formal parameters using the this syntax '''
    return argument


arg = tuple_list('Switch', 299.0, 'Nintendo', 12,
                 ['video-games', 'entertainment'])
print(arg)

# 2nd way


def tuple_list(arg1, arg2, arg3, arg4, arg5):
    return arg1, arg2, arg3, arg4, arg5


z = tuple_list('Switch', 299.0, 'Nintendo', 12,
               ['video-games', 'entertainment'])
print(z)
# ____________________________________________________________________________
''' 3. Define a function that generate a list of tuple containing data values, 
    using the previous function '''


def ListOfTuple(*argument):
    listTuples = [arg]
    for elt in argument[0]:
        listTuples.append(elt)
    return listTuples


x = list(arg)
a = ('PS4', 499.0, 'Sony', 12, ['video-games', 'entertainment']),
('The Walking Dead, Tome 1', 18.5, None, 3, ['books', 'comics']),
('Weapons of Math Destruction', 29.9, None, 0, ['books', 'science']),
("The Dead Don't Die", 15.9, None, 12, ['movie', 'bluray'])

print(ListOfTuple(a))
# _______________________________________________________________________
''' 4. Define a function that take 2 tuples and return 1 dictionary: 
    the first tuple contains the keys, the second contains the values '''


def func_4():

    tuple_key = ('item', 'price', 'brand', 'stock', 'categories')
    tuple_value = ('Switch', 299.0, 'Nintendo', 12,
                   ['video-games', 'entertainment'])

    dict_tuples = dict(zip(tuple_key, tuple_value))

    return dict_tuples


print(func_4())
# ______________________________________________________________________________
''' 5. Define a function that take 1 tuple (keys) and 1 list of tuples (values), 
    and generate 1 list of dictionaries '''


def func_5(keys, values):

    list_dict = []
    for value in values:
        dict_1 = {}
        i = 0
        for key in keys:
            dict_1[key] = value[i]
            i += 1
        list_dict.append(dict_1)
    return list_dict


tuple_key = ('item', 'price', 'brand', 'stock', 'categories')
list_tuples_value = [('Switch', 299.0, 'Nintendo', 12, ['video-games', 'entertainment']),
                     ('PS4', 499.0, 'Sony', 12, [
                      'video-games', 'entertainment']),
                     ('The Walking Dead, Tome 1', 18.5,
                      None, 3, ['books', 'comics']),
                     ("The Dead Don't Die", 15.9, None, 12, ['movie', 'bluray'])]

print(func_5(tuple_key, list_tuples_value))
# _____________________________________________________________________________
''' 6. Define a function that take the list of dictionaries and a maximum price 
    and returns a list of the filtered dictionaries '''


def func_6(list_dict, maximum_price):

    list_result = []
    for dict_ in list_dict:
        if dict_['price'] <= maximum_price:
            list_result.append(dict_)
    return list_result


new_dict = {'item': 'Weapons of Math Destruction',
            'price': 29.9,
            'brand': None,
            'stock': 0,
            'categories': ['books', 'science']}
list_of_dict = func_5(tuple_key, list_tuples_value)
list_of_dict.append(new_dict)
print(func_6(list_of_dict, 30))
# ______________________________________________________________________________
''' 7. Define a function that take the list of dictionaries and a category name 
    and returns a list of the filtered dictionaries '''


def func_7(list_dict, name_categories):

    list_result = []
    for dict_ in list_dict:
        if name_categories in dict_['categories']:
            list_result.append(dict_)
    return list_result


print(func_7(list_of_dict, 'books'))

# ---------------- THE END -----------------
