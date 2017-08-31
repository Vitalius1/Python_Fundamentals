#Find first instance and replace
words = "It's thanksgiving day. It's my birthday,too!"
print words
print words.find("day") # finds the index position where a specific sequence starts first time in a string
words = words.replace("day", "month") # replacing all specified sequences in a string with a different sequence passed in as arguments when function is invoked 
print words

#Min and Max in a list
x = [2,54,-2,7,12,98]
print x
print max(x) # prints out the the element of a list with the bigest value
print min(x) # prints out the the element of a list with the smallest value

#First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
print x
print "First item in the list is:", x[0]   # prints the value of the element at index 0 which is the very first element in a list
print "Last item in the list is:", x[len(x)-1]   # prints the value of the last element in a list which is positioned at index equal to length of the list -1 because the indexes start at 0
y = [x[0], x[len(x)-1]]  # this just is creating a new list with elements from the first and last positions of any given list
print y

#New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
x.sort()   # sorts out a given list
print "now the sorted list looks like this:", x 
y = x[:len(x)/2]  # assigns to a new list "y" the left slice of list "x" all the way until the specified index but not including it
print "first half of list is:", y
x = x[len(x)/2:]  # assigns to a new list "x" the right slice of the list itslef starting from a given index including it
print "second half of list is:", x
x.insert(0,y)  # inserts inside the "x" list at a specified index the list "y"
print "new list created is:", x