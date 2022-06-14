import itertools

users_file = 'users.csv'
hobbies_file = 'hobbies.csv'

users = []
hobbies = []
with open('users.csv', encoding='utf-8') as u:
    users = u.readlines()
with open('hobbies.csv', encoding='utf-8') as h:
    hobbies = h.readlines()

if len(users) < len(hobbies):  # users less than hobbies
    exit(1)

result = {x.strip(): y.strip() if type(y) == str else None for (x, y) in itertools.zip_longest(users, hobbies)}

with open('result.txt', 'wt', encoding='utf-8') as rf:
    rf.writelines((f'{key}: {val}\n' for key, val in result.items()))