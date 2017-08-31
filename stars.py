# First version of program which prints stars
def stars1(arr):
    for i in arr:
        print "*" * i
        
array = [4,5,10,20,5]
stars1(array)

# Second version of program which in case the element in a list is number it prints out that many stars and in case is a string prints out the lower case of the first character times on how many characters has that string
def stars2(arr):
    for i in range(len(arr)):
        if type(arr[i]) == int:
            print "*" * arr[i]
        elif type(arr[i]) == str:
            print arr[i][0].lower() * len(arr[i])
        
array = [4,"Vitalie",10,"Diana",5, "milk o"]
stars2(array)