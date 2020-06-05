# -------------- Project Dojo_Dicts -----------------

# ---------- Algorithms using dictionaries ----------

# ________________________________________________
''' 1. Create a dictionary with integer values '''

# First way to create a Dict
from datetime import date
import datetime
list_str = ['price', 'stock']
list_int = [12.5, 4]
dict_1 = dict(zip(list_str, list_int))
print(dict_1)

# Second way to create a Dict
dict_1 = {}
list_key = ['price', 'stock']
list_value = [12.5, 4]

for i in list_key:
    for v in list_value:
        dict_1[i] = v
print(dict_1)
# ________________________________________________
'''' 2. Create a dictionary with string values '''

# Convert a list to dict
list_str = ['item', 'Switch', 'brand', 'Nintendo']
dict_2 = dict()

for i, item in enumerate(list_str):
    if i % 2 == 0:
        dict_2[item] = list_str[i+1]
print(dict_2)
# ___________________________________________________________________________________________
''' 3. Create a dictionary with a person's details (first name, last name, birthday, job) '''


list_title = ['first_name', 'last_name', 'birthday', 'job']
list_data1 = ['John', 'Doe', datetime.date(1980, 1, 1), 'Engineer']

dict_person1 = dict(zip(list_title, list_data1))
print(dict_person1)
# ___________________________________________________________________________________________________________________________
''' 4. Add an address field to the person's details, which is another dictionary itself (street, postcode, city, country) '''

list_t1 = ['street', 'postcode', 'city', 'country']
list_adress = ['123 rue Victor Hugo', 38000, 'Grenoble', 'FR']

dict_adress = dict(zip(list_t1, list_adress))
dict_person1['address'] = dict_adress
print(dict_person1)
# _________________________________________________________________________
''' 5. Create a list of dictionaries with people's details (at least 2) '''

dict_adress2 = {}
list_dicts = []

list_data2 = ['Jane', 'Doe', datetime.date(1978, 3, 1), 'Baker']
list_adress2 = ['1 avenue Champs Elysées', 75000, 'Paris', 'FR']

dict_person2 = dict(zip(list_title, list_data2))
dict_adress2 = dict(zip(list_t1, list_adress2))
dict_person2['address'] = dict_adress2

list_dicts.append(dict_person1)  # with loop for
list_dicts.append(dict_person2)
print(list_dicts)
# _____________________________________________________________________
''' 6. Display the city for each person in the list of dictionaries '''

for dixs in list_dicts:
    print(dixs['first_name'], dixs['address']['city'], sep=': ')
# __________________________________________________________________________________
''' 7. Compute the average age from a list of dictionaries with people's details '''


sum_age = 0
for dixs in list_dicts:
    days_in_year = 365.2425
    age = (date.today() - dixs['birthday']).days / days_in_year
    sum_age += age

print(round(sum_age) // len(list_dicts))

# ---------------- THE END -----------------
