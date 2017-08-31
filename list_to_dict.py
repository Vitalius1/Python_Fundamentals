name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "dogs"]

# First function which takes 2 lists and makes a dictionary.
def list_to_dict (list1, list2):
    new_dict = {}
    list_of_tuples = zip(list1, list2)
    new_dict = dict(list_of_tuples)
    return new_dict

print list_to_dict(name, favorite_animal)

# Second function which takes 2 lists and makes a dictionary with the keys being the elements in the longer list
def list_to_dict2 (list3, list4):
    new_dict2 = {}
    if len(list3) >= len(list4):
        list_of_tuples2 = zip(list3, list4)
    else:
        list_of_tuples2 = zip(list4, list3)
    new_dict2 = dict(list_of_tuples2)
    return new_dict2

print list_to_dict2 (name, favorite_animal)