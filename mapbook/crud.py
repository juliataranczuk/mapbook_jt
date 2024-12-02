


def hello(user:str):
    print(f'Witaj {user}!!')

def read_users(users:list)->None:
    for user in users[1:]:
        print(f'Twój znajomy {user['name']}, z miejscowości {user['city']} opublikował {user['posts']} postów')


def remove_user(userlist:list)->None:
    user_to_find: str = input('podaj imie do usunięcia:')
    for user in userlist:
        if user['name'] == user_to_find:
            print(f'usuwam:{user}')
            userlist.remove(user)

def update_user(userlist:list)->None:
    user_to_find: str = input('podaj imie do modyfikacji')
    for user in userlist:
        if user['name'] == user_to_find:
            new_name: str=input('proszę podać nowe imię znajomego')
            new_posts: int=int(input('podaj nową liczbę postów'))
            new_city: str=input('podajnowe miasto')
            user['name'] = new_name
            user['posts'] = new_posts
            user['city']=new_city

