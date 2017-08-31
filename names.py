'''
PART I
'''
students = [
     {'first_name': 'Michael', 'last_name': 'Jordan'},
     {'first_name': 'John', 'last_name': 'Rosales'},
     {'first_name': 'Mark', 'last_name': 'Guillen'},
     {'first_name': 'KB', 'last_name': 'Tonel'}
]

def stud_list(arr):
    for value in arr:
        print value["first_name"], value["last_name"]

stud_list(students)

'''
PART II
'''

users = {
 'Students': [
     {'first_name': 'Michael', 'last_name': 'Jordan'},
     {'first_name': 'John', 'last_name': 'Rosales'},
     {'first_name': 'Mark', 'last_name': 'Guillen'},
     {'first_name': 'KB', 'last_name': 'Tonel'}
  ],
 'Instructors': [
     {'first_name': 'Michael', 'last_name': 'Choi'},
     {'first_name': 'Martin', 'last_name': 'Puryear'}
  ]
 }
def print_list (dictionary):
    for key, data in dictionary.items():
        print key
        counter = 1
        for value in data:
            print counter,"-", value["first_name"].upper(), value["last_name"].upper(), "-", len(value["first_name"]) + len(value["last_name"])
            counter += 1
print_list(users)
