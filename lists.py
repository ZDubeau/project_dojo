# ------------------ Project Dojo_Lists -------------------

# ---------------- Algorithms using lists -----------------

# ______________________________________________
''' 1. Fill a list with integers from 0 to 9 '''

import string
list_1 = []
for i in range(10):
    list_1.append(i)
print(list_1)

liste = list(range(10))
print(liste)
# _______________________________________________________
''' 2. Append to the list even integers from 10 to 20 '''

# First way to create a new list and merge it with list_1
list_2 = []
for i in range(10, 21, 2):
    list_2.append(i)
    i += 1
list_merge1 = list_1 + list_2
print(list_merge1)

# Second way without creating new List
for i in range(10, 21, 2):
    list_1.append(i)
print(list_1)
# ______________________________________________________
''' 3. Append to the list odd integers from 21 to 30 '''

# One way
list_3 = []
for i in range(21, 30, 2):
    list_3.append(i)
    i += 1
list_merge2 = list_merge1 + list_3
print(list_merge2)

# Another way
for i in range(21, 30, 2):
    list_1.append(i)
print(list_1)
# __________________________________________________
''' 4. Reverse the order of the list of integers '''

list_reverse = []
for i in range(len(list_merge2)):
    list_reverse.append(list_merge2[len(list_merge2)-1-i])
print(list_reverse)
# _____________________________________________________________________________
'''' 5. For each element of the integer list, print the index and the value '''

for i, v in enumerate(list_reverse):
    print('index: %s, value: %s' % (i, v))
    # print(f'index: {i}, value: {v}')# best way to print
# _____________________________________________
''' 6. Keep only elements with an odd value '''

list_odd = []
for i in list_reverse:
    if i % 2 != 0:  # odd numbers
        list_odd.append(i)
print(list_odd)
# _________________________________________________________________
''' 7. Create a list of all alphabet characters from 'a' to 'z' '''


list_alphabet = list(string.ascii_lowercase)  # Alphabet in lowercase
print(list_alphabet)
# __________________________________________________________________________________________________
''' 8. Print for each element of the list of integer its equivalent character at the: same index '''

# First way from Dominique
for number in list_odd:
    if number // len(list_alphabet) < 1:  # read until 26th letter of list
        value = list_alphabet[number]
    else:
        # read from 26th letter to end of list
        value = list_alphabet[number-len(list_alphabet)]
    print(f'index: {number}, character: {value}')

# Second way to find equivalent
last_list = []
for i in list_odd:
    last_list.append(list_alphabet[i % len(list_alphabet)])
# print(last_list)
for i, v in enumerate(last_list):
    print(f'index: {list_odd[i]}, character: {v} ')

# ---------------- THE END -------------------
