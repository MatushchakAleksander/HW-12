import pickle

users = [
    {
        'name': 'Jacob',
        'password': '22&570M9',
    },
    {
        'name': 'Ivan',
        'password': '@3RS6f45'
    }
]
f = open('date.txt', 'wb')
pickle.dump(users, f)
print(pickle.dumps(users))

f.close()
