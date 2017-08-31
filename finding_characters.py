word_list = ['hello','world','my','name','is','Anna','Jora']
char = 'o'
new_list = []

for word in word_list:
    for i in word:
        if char == i:
            new_list.append(word)
print new_list