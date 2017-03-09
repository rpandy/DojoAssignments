#display dictionaries on different lines to differentiate the key:value pairs

name_dictionary = {
     "sw":"Sara Wong",
     "mp":"Martin Puryear"
     }
for key in name_dictionary:
    print name_dictionary[key]

name_dictionary = {
     "sw":"Sara Wong",
     "mp":"Martin Puryear"
     }
for key, val in name_dictionary.items():
    print key, val

name_dictionary = {
     "sw":"Sara Wong",
     "mp":"Martin Puryear"
     }
for key, val in name_dictionary.items():
    print name_dictionary["sw"]
#same as using name_dictionary.item()
name_dictionary = {
     "sw":"Sara Wong",
     "mp":"Martin Puryear"
     }
for key in name_dictionary:
    print key, name_dictionary[key]  #printing key of sw or mp and the name_dictionary of sw and mp as Sara Wong and Martin Puryear respectively




context = {
    'questions': [
    {'id':1, 'content': "Why is there a light in the fridge and not in the freezer?"},
    {'id':2, 'content': "Why don't sheep shrink when it rains?"},
    {'id':3, 'content': "Why are they called apartments when they are all stuck together?"},
    {'id':4, 'content': "Why do cars drive on the parkway and park on the driveway?"}
    ]
}

for key, data in context.items():
    for value in data:
        print "Question #",value["id"],":",value["content"]
        print "-------"


name_dictionary = {
    "sw":"Sara Wong",
    "mp":"Martin Puryear"
    }
for key in name_dictionary:
    print name_dictionary[key]
