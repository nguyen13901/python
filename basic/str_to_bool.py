def str_to_bool(s):
    return s.lower() in ("yes", "true", "t", "1")


s = str_to_bool(input("Input a boolean: "))
print("You entered: ", s)
print("Data type: ", type(s))