import pickle
"""ピクルのサンプル"""
# x = [10, 20, 30]

# with open('./data.pickle', 'wb') as f:
#     pickle.dump(x, f)

# with open('./data.pickle', 'rb') as f:
#     x = pickle.load(f)
# print(x)

from DataClass import User

user = User('Suzuki', 21)
with open('./data.pickle', 'wb') as f:
    pickle.dump(user, f)

with open('./data.pickle', 'rb') as f:
    user = pickle.load(f)

print(user)
