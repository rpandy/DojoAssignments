# students = [
#     {'first_name': 'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'},
#     {'first_name': 'Mark', 'last_name': 'Guillen'},
#     {'first_name': 'KB', 'last_name': 'Tonel'}
# ]
#
#     #run a for loop through the
#     #for val in students: #prints all four key value pairs
#     #prints the first key of every list item
# for i in students:
#     for key, val in i.iteritems():
#         print key, val
#
#
# print "**------------------**"
#
# students = [
#     {'first_name': 'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'},
#     {'first_name': 'Mark', 'last_name': 'Guillen'},
#     {'first_name': 'KB', 'last_name': 'Tonel'}
# ]
# #prints the first key of every list item
# for i in students:
#     for key, val in i.iteritems():
#         print val
#
# print "**------------------**"

#
# students = [
#     {'first_name': 'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'},
#     {'first_name': 'Mark', 'last_name': 'Guillen'},
#     {'first_name': 'KB', 'last_name': 'Tonel'}
# ]
# for i in students:
#     print i["first_name"] + " " + i["last_name"]
#
# print "**------------------**"
#
# students = [
#     {'first_name': 'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'},
#     {'first_name': 'Mark', 'last_name': 'Guillen'},
#     {'first_name': 'KB', 'last_name': 'Tonel'}
# ]
# #prints the first key of every list item
# print students

print "**------------------**"

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
def showStudents(arr):
    for i in students:
        print i["first_name"] + " " + i["last_name"]

showStudents(students)

print "**------------------**"

#PART 2

users = {
    'Students': [
        {'first_name': 'Michael', 'last_name': 'Jordan'},
        {'first_name': 'John', 'last_name': 'Rosales'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ],
    'Instructors': [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'John', 'last_name': 'Rosales'},
    ]
}
def showStudentsAndInstructors(users):
    for role in users:
        counter = 0
        print role
        for person in users[role]:
            counter += 1
            first_name = person['first_name']
            last_name = person['last_name']
            length = len(person['first_name'] + person['last_name'])
            print "{} - {} {} - {}".format(counter, first_name,last_name, length)
showStudentsAndInstructors(users)
