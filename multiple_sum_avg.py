# part1 A
# print out all odd numbers in a given range
for i in range(1, 101, 2):
    if i % 2 != 0:
        print i
'''
this iterates all numbers from 1 to 101(not including it so that we include 100 as the last number)
than we chech if the first number in the range is a odd number than print it and in order to jump to the next odd number we should use a step
of 2 every time
'''

# part1 B
# print out multiples of 5 in a given range
for i in range (6, 101):
    if i % 5 == 0:
        print i

# part2
# calculate the sum of all elements in a list
a = [1, 2, 5, 10, 255, 3]
sum = sum(a)
# sum = 0
# for i in a:
#     sum += i
print "the sum is:", sum

# part3
# return the average of the all elements in a list
b = [1, 2, 5, 10, 255, 3]
sum2 = sum(b)
print sum2

# for i in b:
#     sum += i
# print "the average is:", sum2/len(b)