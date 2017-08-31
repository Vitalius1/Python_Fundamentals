# Test case 1
# list_one = [1,2,5,6,2]
# list_two = [1,2,5,6,2]
# Test case 2
# list_one = [1,2,5,6,5]
# list_two = [1,2,5,6,5,3]
# Test case 3
list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
# Test case 4
# list_one = ['celery','carrots','bread','milk']
# list_two = ['celery','carrots','bread','cream']

if len(list_one) != len(list_two):
    print "The lists are different."
else:
    for i in range(0, len(list_one)):
        if list_one[i] != list_two[i]:
            print "The lists are different."
        elif i == len(list_one) - 1:
            print "The lists are the same."