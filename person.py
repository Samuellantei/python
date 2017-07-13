def get_age():
    age = int(raw_input("what is your age?"))
    return age

def get_name():
    return raw_input("what is your name?")

age = get_age()
name = get_name()
print "Hey; " + name + ", your are " + age + "years old, dude!"
