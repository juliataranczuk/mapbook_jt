users:list=[
    {'name':'Julia', 'posts':1, 'city':'Zamość'},
    {'name':'Dominik', 'posts':3, 'city':'Poznań'},
    {'name':'Szymon z wąsem', 'posts':5, 'city':'Toruń'},
    {'name':'Szymon', 'posts':7, 'city':'Łódź'},
    {'name':'Patryk', 'posts':9, 'city':'Kielce'},
    {'name':'Patrycja', 'posts':20, 'city':'Mińsk Mazowiecki'},
    {'name':'Patrycja', 'posts':33, 'city':'Kraśnik'},
    {'name':'Karolina', 'posts':12, 'city':'Warszawa'},
    {'name':'Amelia', 'posts':2, 'city':'Toruń'},
    {'name':'Kinga', 'posts':6, 'city':'Iława'},

]
#TODO please update user list



print(f'Witaj {users[0]["name"]}!!')
for user in users[1:]:
    print(f'Twój znajomy {user['name']}, z miasta {user['city']}, opublikował {user['posts']}  postów')

# for idx,_ in enumerate(users[1:]):
#     print(f'Twój znajomy {users[idx]}, opublikował {postow[idx]} postów')