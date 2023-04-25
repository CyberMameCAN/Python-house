""" リストの値を先頭に移動するスクリプト例 """

mylist = [
        "Kawada",
        "Take",
        "Yokoyama",
        "Kameda",
        ]

index = mylist.index("Kameda")
_name = mylist.pop(index)
mylist.insert(0, _name)
print(mylist)
