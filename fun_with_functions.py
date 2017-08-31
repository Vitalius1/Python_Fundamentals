#function check odd or even numbers in specified range
def odd_even(start, end):
    for i in range(start, end + 1):
        if i % 2 == 0:
            print "The number is:", i, "This is an even number."
        else:
            print "The number is:", i, "This is an odd number."
odd_even(1, 20)

#function multiply the items in a list by a given number
def multiply(arr, num):
    for i in range(len(arr)):
        arr[i] *= num
    return arr
array = [2,4,6,8,5]
print multiply(array, 5)

#function haker layerd multiply
def layerd_multiply(arr):
    new_array = []
    for i in range(len(arr)):
        elem = []
        for j in range(arr[i]):
            elem.append(1)
        new_array.append(elem)
    return new_array
print layerd_multiply(multiply([2,3,4], 2))