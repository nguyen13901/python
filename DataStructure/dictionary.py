#Dictionary: Key-Value pairs, Unordered, Mutable

my_dict = {"name": "Max", "age": 22, "city": "Manchester United"}
print(my_dict)

my_dict2 = dict(name = "Peter", age = 20, city = "Liverpool")
print(my_dict2)

value = my_dict['name']
print(value)

my_dict["email"] = "nguyen13901@gmail.com"
print(my_dict)

#del my_dict["email"]
#print(my_dict)

#print(my_dict.pop("city"))
#print(my_dict)

#rint(my_dict.popitem()) # delete last item

# for key in my_dict:
#     print(key)
#
# for key, value in my_dict.items():
#     print(key, value)
#
# for value in my_dict.values():
#     print(value)

# my_dict3 = my_dict.copy()
# my_dict4 = my_dict
# my_dict5 = dict(my_dict)
#
# my_dict["email"] = "nguyen13901@gmail.com"
# print("my_dict: ", id(my_dict))
# print("my_dict3: ", id(my_dict3))
# print("my_dict4: ", id(my_dict4))
# print("my_dict5: ", id(my_dict5))

my_dict.update(my_dict2)
print(my_dict)