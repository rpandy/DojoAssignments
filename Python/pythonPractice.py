# #display dictionaries on different lines to differentiate the key:value pairs
#
# name_dictionary = {
#      "sw":"Sara Wong",
#      "mp":"Martin Puryear"
#      }
# for key in name_dictionary:
#     print name_dictionary[key]
#
# name_dictionary = {
#      "sw":"Sara Wong",
#      "mp":"Martin Puryear"
#      }
# for key, val in name_dictionary.items():
#     print key, val
#
# name_dictionary = {
#      "sw":"Sara Wong",
#      "mp":"Martin Puryear"
#      }
# for key, val in name_dictionary.items():
#     print name_dictionary["sw"]
# #same as using name_dictionary.item()
# name_dictionary = {
#      "sw":"Sara Wong",
#      "mp":"Martin Puryear"
#      }
# for key in name_dictionary:
#     print key, name_dictionary[key]  #printing key of sw or mp and the name_dictionary of sw and mp as Sara Wong and Martin Puryear respectively
#
#
#
#
# context = {
#     'questions': [
#     {'id':1, 'content': "Why is there a light in the fridge and not in the freezer?"},
#     {'id':2, 'content': "Why don't sheep shrink when it rains?"},
#     {'id':3, 'content': "Why are they called apartments when they are all stuck together?"},
#     {'id':4, 'content': "Why do cars drive on the parkway and park on the driveway?"}
#     ]
# }
#
# for key, data in context.items():
#     for value in data:
#         print "Question #",value["id"],":",value["content"]
#         print "-------"
#
#
# name_dictionary = {
#     "sw":"Sara Wong",
#     "mp":"Martin Puryear"
#     }
# for key in name_dictionary:
#     print name_dictionary[key]
print "**------------------**"

#iteration practice
superheros = {
    "quickster": "The Flash",
    "buster": "The Hulk",
    "flyer": "Silver Surfer",
    "detective": "Bat Man",
}
print "**------------------**"

#practice from lecture three session 1

print superheros
#we want the flash. still print superheros because we're looking at that dictionary
#the brackets [] with the key in them get us the value we want
print superheros["quickster"]
#when dealing with superheros and for loops. hero is the key of the dictionary.
for hero in superheros:
    print "the key is ", hero
    print "the value for", hero, "is", superheros[hero]


print "**------------------**"
#items
for hero in superheros.items():
    print hero
#unpacked tuple into two variables.
for key, value in superheros.items():
    print key,value
for key, value in superheros.items():
        print key * 3,value
print "**------------------**"
#iteritems
#only difference is on the backend and how the memory is cached
for key, value in superheros.iteritems():
    print key,value
for key, value in superheros.iteritems():
        print key * 3,value


print "**------------------**"
#lists in dictionaries
superheroes = {
    "quickster": ["The Flash", "Quick Silver"],
    "buster": ["The Hulk", "The Thing"],
    "flyer": ["Silver Surfer", "Iron Man", "Superman"],
    "detective": ["Bat Man", "The Owl"],
}

for hero_type, heroes in superheroes.items():
    print hero_type
    for hero in heroes:
        print ">>>>>", hero
print "**------------------**"

hero_string = "silver surfer Iron Man Superman"
# returns the spot that the word surfer starts in the string.
#first instance of the pattern. 
print hero_string.find("surfer")
