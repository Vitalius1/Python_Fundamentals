# Building the dictionary about my self
myself = {}
myself["name"] = "Vitalie Braga"
myself["age"] = "31"
myself["country of birth"] = "Moldova"
myself["favorite language"] = "Python"

# one way of accesing all key-value pairs in a dictionary
def info1(dictionary):
    for key in dictionary:
        print "My {} is {}.".format(key, dictionary[key])

# another way of accesing all key-value pairs in a dictionary
def info2(dictionary):
    for key,value in dictionary.iteritems():
        print "My {} is {}.".format(key, value)

info1(myself)
info2(myself)