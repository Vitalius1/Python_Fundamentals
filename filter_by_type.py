sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']


# Choose which variable to test and what type it is.
var = bS
vartype = type(var)

# Check if the variable is of integer type
if vartype is int:
    if var >= 100:
        print "that is a big number!"
    else:
        print "that is a small number"
# Check if the variable is of string type
elif vartype is str:
    if len(var) >= 50:
        print "that is a long sentence"
    else:
        print "this is a short sentence"
# Check if the variable is of list type
elif isinstance(var, list):
    if len(var) >= 10:
        print "this is a big list"
    else:
        print "this is a short list"