# Sort the list into different types of the elements it has.
# my_list = [2,3,1,7,4,12]
# my_list = ['magical','unicorns']
# my_list = ['magical unicorns',-19,'hello',19,'world']
# my_list = [-9,9]
my_list = ['magical unicorns',20,'hello',19,'world']
new_str = ""
sum = None
s = 0
for i in my_list:
    if type(i) is str:
        new_str = new_str + " " + i
    elif type(i) is int or float:
        s += i
        sum = s
if new_str:
    print "String is:", new_str
if sum or sum == 0:
    print "The sum is:", sum
if new_str and sum is not None:
    print "The original list is of a mixed type."
elif new_str and sum is None:
    print "The initial list is of string type."
elif not new_str and sum is not None:
    print "The initial list is of integer type."